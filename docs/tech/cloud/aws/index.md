# Amazon Web Services

![OldManYellsAtCloud](_OldManYellsAtCloud.svg)

Terraform Generator: <https://terragen.dev/>

## AWS PowerShell Module

[AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html)

Windows

``` ps1
Install-Module -Name AWS.Tools.Installer
Install-AWSToolsModule AWS.Tools.EC2,AWS.Tools.S3 -CleanUp
```

Linux

``` ps1
Install-Module -Name AWSPowerShell.NetCore
```

## Public IPs

A [JSON file](https://ip-ranges.amazonaws.com/ip-ranges.json) for all public [AWS IP ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) is avaiable for download.

Example Output

``` json
{
  "syncToken": "1648221200",
  "createDate": "2022-03-25-15-13-20",
  "prefixes": [
    {
      "ip_prefix": "3.5.140.0/22",
      "region": "ap-northeast-2",
      "service": "AMAZON",
      "network_border_group": "ap-northeast-2"
    }
    ]
}
```

It is also possible to query the public IP ranges with the AWS PowerShell module:

``` ps1
Get-AWSPublicIpAddressRange -ServiceKey ec2 -Region  eu-west-1,eu-central-1
```

Example Output

``` txt
IpPrefix           : 54.247.0.0/16
IpAddressFormat    : Ipv4
Region             : eu-west-1
Service            : EC2
NetworkBorderGroup : eu-west-1
```

## Regions

| AWS Region Code    | AWS Region Name                        | Comment                                                  |
|--------------------|----------------------------------------|----------------------------------------------------------|
| us-east-1          | US East (N. Virginia)                  | Launched 2006                                                     |
| us-east-2          | US East (Ohio)                         | Launched 2016                                                     |
| us-west-1          | US West (N. California)                | Launched 2009                                                     |
| us-west-2          | US West (Oregon)                       | Launched 2011                                                     |
| ca-central-1       | Canada (Montreal)                      | Launched 2016                                                     |
| eu-north-1         | EU (Stockholm)                         | Launched 2018                                                     |
| eu-west-3          | EU (Paris)                             | Launched 2017                                                     |
| eu-west-2          | EU (London)                            | Launched 2016                                                     |
| eu-west-1          | EU (Ireland)                           | Launched 2007                                                     |
| eu-central-1       | EU (Frankfurt)                         | Launched 2014                                                     |
| eu-south-1         | EU (Milan)                             | Launched 2020                                                     |
| ap-south-1         | Asia Pacific (Mumbai)                  | Launched 2016                                                     |
| ap-northeast-1     | Asia Pacific (Tokyo)                   | Launched 2011                                                     |
| ap-northeast-2     | Asia Pacific (Seoul)                   | Launched 2016                                                     |
| ap-northeast-3     | Asia Pacific (Osaka-Local)             | Launched 2018                                                     |
| ap-southeast-1     | Asia Pacific (Singapore)               | Launched 2010                                                     |
| ap-southeast-2     | Asia Pacific (Sydney)                  | Launched 2012                                                     |
| ap-southeast-3     | Asia Pacific (Jakarta)                 | Launched 2021                                                     |
| ap-east-1          | Asia Pacific (Hong Kong) SAR           | Launched 2019                                                     |
| sa-east-1          | South America (SÃ£o Paulo)             | Launched 2011                                                     |
| cn-north-1         | China (Beijing)                        | Launched 2014                                                     |
| cn-northwest-1     | China (Ningxia)                        | Launched 2017                                                     |
| us-gov-east-1      | GovCloud (US-East)                     | Launched 2018                                                     |
| us-gov-west-1      | GovCloud (US-West)                     | Launched 2011                                                     |
| us-gov-secret-1    | AWS Secret Region (US-Secret)          | Launched 2017                                                     |
| us-gov-topsecret-1 | AWS Top Secret-East Region (US-Secret) | Launched 2014                                                     |
| us-gov-topsecret-2 | AWS Top Secret-West Region (US-Secret) | Launched 2021                                                     |
| me-south-1         | Middle East (Bahrain)                  | Launched 2019                                                     |
| af-south-1         | Africa (Cape Town)                     | Launched 2020                                                     |
| eu-east-1          | EU (Spain)                             | Under Constructions Expected in late 2022 or early 2023  |
| eu-central-2       | EU (Zurich)                            | Under Constructions Expected in 2022                     |
| ap-south-2         | Asia Pacific (Hyderabad)               | Under Constructions Expected in mid 2022                 |
| ap-southeast-3     | Asia Pacific (Melbourne)               | Under Constructions Expected in second half of 2022      |
| me-south-2         | Middle East (United Arab Emirates)     | Under Constructions Expected in first half of 2022       |
| eu-north-1         | EU (Estonia)                           | Projection                                               |
| eu-south-1         | EU (Cyprus)                            | Projection                                               |
| me-west-1          | Middle East (Tel Aviv)                 | Under Constructions Expected in first half of 2023      |
| ru-central-1       | Russia (TBD)                           | Projection                                               |
| ap-southeast-4     | Asia Pacific (Auckland)                | Under Constructions Expected in 2024                    |
| ca-west-1          | Canada (Calgary)                       | Under Constructions Expected in late 2023 or early 2024 |
