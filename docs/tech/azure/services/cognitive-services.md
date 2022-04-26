# Cogntive Services

## Text Translation

Create a CognitiveServices resource from the type TextTranslation:

``` ps1
Import-Module Az.CognitiveServices
$resourceGroup = "rg-Translate"
$AccountName = "acs-translation"
New-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $AccountName -Type TextTranslation -SkuName F0 -Location westeurope
Start-Sleep -s 15
Add-AzCognitiveServicesAccountNetworkRule -ResourceGroupName $resourceGroup -Name $AccountName -IpAddressOrRange "200.0.0.0/24","28.2.0.0/16"
Write-Host("Ocp-Apim-Subscription-Key: " + (Get-AzCognitiveServicesAccountKey -ResourceGroupName $resourceGroup -Name $AccountName).Key1)
Write-Host("Ocp-Apim-Subscription-Region: " + (Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $AccountName).Location)
Write-Host("Endpoint: "+(Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $AccountName).Endpoint +"translate")
```

Test the translation service with this python script:

``` py
import requests, uuid

# Input variables (get this from your azure translate resource)
location = "westeurope"
key = ""
url = "https://api.cognitive.microsofttranslator.com/translate"

# Translate text in various languages
def translate(text:'str', output:'dict'=[])-> 'dict':
    body = [{ 'text': text}]
    params = {'api-version': '3.0', 'from': 'en', 'to': ['de', 'ru', 'yue', 'tlh-Latn', 'ko', 'ku', 'mn-Cyrl', 'mn-Mong', 'ne', 'th', 'yua', 'ja', 'el']} #https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support
    headers = {'Ocp-Apim-Subscription-Key': key, 'Ocp-Apim-Subscription-Region': location, 'Content-type': 'application/json', 'X-ClientTraceId': str(uuid.uuid4())}
    request = requests.post(url, params=params, headers=headers, json=body)
    result = request.json()[0]['translations']
    dict = {}
    print("-----------------------------------------------\n| ClientTraceId:\t" + str(uuid.uuid4()))
    print("| Chars to translate:\t" + str(len(result)))
    print("| Input:\t\t" + text + "\n-----------------------------------------------")
    for language in result:
        print(language['to'] + "\t" + language['text'])
        dict[language['to']] = language['text']

    return dict

translate("This is a test azure translation test!")
```

Import [this](_texttranslate-postman.json) to Postman and add a valid Ocp-Apim-Subscription-Key to make the following example work:

``` json
{
    "info": {
        "_postman_id": "e9ea56cc-e63d-468a-a88a-5d0a3761faab",
        "name": "MS Translator",
        "schema": < https: //schema.getpostman.com/json/collection/v2.1.0/collection.json>
    },
    "item": [{
        "name": "Translate from EN to various",
        "protocolProfileBehavior": {
            "disabledSystemHeaders": {
                "content-length": true
            }
        },
        "request": {
            "auth": {
                "type": "apikey",
                "apikey": [{
                        "key": "value",
                        "value": "",
                        "type": "string"
                    },
                    {
                        "key": "key",
                        "value": "Ocp-Apim-Subscription-Key",
                        "type": "string"
                    }
                ]
            },
            "method": "POST",
            "header": [{
                    "key": "Content-Type",
                    "value": "application/json",
                    "type": "text"
                },
                {
                    "key": "Ocp-Apim-Subscription-Region",
                    "value": "westeurope",
                    "type": "text"
                }
            ],
            "body": {
                "mode": "raw",
                "raw": "[{'Text':'Hello, what is your name?'}]",
                "options": {
                    "raw": {
                        "language": "json"
                    }
                }
            },
            "url": {
                "raw": < https: //api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=de&to=ru&to=yue&to=tlh-Latn&to=ko&to=ku>,
                    "protocol": "https",
                "host": [
                    "api",
                    "cognitive",
                    "microsofttranslator",
                    "com"
                ],
                "path": [
                    "translate"
                ],
                "query": [{
                        "key": "api-version",
                        "value": "3.0"
                    },
                    {
                        "key": "from",
                        "value": "en"
                    },
                    {
                        "key": "to",
                        "value": "de"
                    },
                    {
                        "key": "to",
                        "value": "ru"
                    },
                    {
                        "key": "to",
                        "value": "yue"
                    },
                    {
                        "key": "to",
                        "value": "tlh-Latn"
                    },
                    {
                        "key": "to",
                        "value": "ko"
                    },
                    {
                        "key": "to",
                        "value": "ku"
                    },
                    {
                        "key": "to",
                        "value": "mn-Mong"
                    },
                    {
                        "key": "to",
                        "value": "ne"
                    },
                    {
                        "key": "to",
                        "value": "th"
                    },
                    {
                        "key": "to",
                        "value": "yua"
                    }
                ]
            }
        },
        "response": []
    }]
}
```

## Speech Service

Azure offers a service to convert text to speech and speech to text. Here are some examples on how this works.

I followed this guide: <https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/index-speech-to-text>.

Here are the steps i took to make it work.

**Convert input to wav**

Make sure the input is a wav file. You can use FFMPEG for this task e.g.

``` sh
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav
```

For more options view my [FFMPEG notes](https://0xfab1.net/tech/tools/ffmpeg/) or visit <https://ffmpeg.org/documentation.html>

**Install required tools**

``` ps1
Install-Package Microsoft.CognitiveServices.Speech # If not possible, run: Register-PackageSource -Name MyNuGet -Location https://www.nuget.org/api/v2 -ProviderName NuGet
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco install -y vscode # vscode
choco install -y dotnet # .NET
Start-Process "vscode:extension/ms-dotnettools.csharp"
dotnet add package Microsoft.CognitiveServices.Speech # Speech Package
```

**Create new Csharp Project**

``` ps1
New-Item -Path SpeechTest -Type Directory 
cd SpeechTest
dotnet new console
```

**Create new azure speech service resource**

I create this manually as I was to lazy to script this:
Fill out the form: <https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne>
And you are ready to go.

**Code of Program.cs**

The program is not optimized, kept simple and is based on the example provided by the microsoft guide.
Change the parts where comments are added to make it work for you.

```csharp
using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;

namespace SpeechTest
{
    class Program
    {
        async static Task Main(string[] args)
        {
            var speechConfig = SpeechConfig.FromSubscription("Cognitive Service API KEY1", "WestEurope"); //change
            speechConfig.SpeechRecognitionLanguage = "de-de"; // change
            using var audioConfig = AudioConfig.FromWavFileInput("Path\\File.wav"); // change

            using (var recognizer = new SpeechRecognizer(speechConfig, audioConfig))
            {
                recognizer.Recognizing += (s, e) => { Console.WriteLine($"RECOGNIZING: Text={e.Result.Text}"); };

                recognizer.Recognized += (s, e) => {
                    var result = e.Result;
                    Console.WriteLine($"Reason: {result.Reason.ToString()}");

                    switch (result.Reason)
                    {
                        case ResultReason.RecognizedSpeech:
                            Console.WriteLine($"Final result: Text: {result.Text}.");
                            File.AppendAllText("Output.txt", Environment.NewLine);
                            File.AppendAllText("Output.txt", result.Text);
                            break;
                        case ResultReason.NoMatch:
                            Console.WriteLine($"NOMATCH: Speech could not be recognized.");
                            break;
                        case ResultReason.Canceled:
                            var cancellation = CancellationDetails.FromResult(result);
                            Console.WriteLine($"CANCELED: Reason={cancellation.Reason}");
                            if (cancellation.Reason == CancellationReason.Error)
                            {
                                Console.WriteLine($"CANCELED: ErrorCode={cancellation.ErrorCode}");
                                Console.WriteLine($"CANCELED: ErrorDetails={cancellation.ErrorDetails}");
                                Console.WriteLine($"CANCELED: Did you update the subscription info?");
                            }
                            break;
                    }
                };

                recognizer.Canceled += (s, e) => { Console.WriteLine($"\n    Canceled. Reason: {e.Reason.ToString()}, CanceledReason: {e.Reason}"); };
                recognizer.SessionStarted += (s, e) => { Console.WriteLine("\n    Session started event."); };
                recognizer.SessionStopped += (s, e) => { Console.WriteLine("\n    Session stopped event."); };

                await recognizer.StartContinuousRecognitionAsync().ConfigureAwait(false);

                do { Console.WriteLine("Press Enter to stop");
                } while (Console.ReadKey().Key != ConsoleKey.Enter);

                await recognizer.StopContinuousRecognitionAsync().ConfigureAwait(false);
            }
        }
    }
}
```

Run the code with:

``` ps1
dotnet run
```

This example output shows how the program first checks word for word and once the sentence  is over commits a sentence. Sometimes content of the sentence changes based on the following word(s). The example is analyzing a story by Nils Holgersson in german language:

![speechtotext](_speechtotext.webp)
