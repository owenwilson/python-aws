# python aws

- the following folders and scripts are used to deploy **AWS services**

## recommended aws regions

- These regions Norte de Virginia (us-east-1), Ohio (us-east-2) y Oregón (us-west-2) offer low costs for resources such as **EC2,S3,RDS**

|AZ|REGION|
|--|------|
|`Norte de Virginia`|`(us-east-1)`|
|`Ohio`|`(us-east-2)`|
|`Oregon`|`(us-west-2)`|

## aws cli

- review the following configuration and installation examples
- recomemend use aws key and secret key
- output format json

```sh
aws configure
```

## installing uv

- check [the uv documentation](https://docs.astral.sh/uv/getting-started/installation/)

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## python3 venv

```sh
python3 -m venv venv
```

- activate venv

```sh
source venv/bin/activate
```

- desactive

```sh
deactivate
```

## reference

- check [the aws docs boto3](https://docs.aws.amazon.com/boto3/latest/)