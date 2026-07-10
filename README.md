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

- installation [uv package](https://docs.astral.sh/uv/getting-started/installation/)
- the [uv](https://pydevtools.com/handbook/explanation/uv-complete-guide/) complete guide

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```sh
cd python-aws
```

```sh
uv venv
```

- output

```text
Using CPython 3.14.6 interpreter at: /usr/bin/python
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

- deactivate venv

```sh
deactivate
```

## python3 venv

- check [python3 virtual environment documentation](https://docs.python.org/3/library/venv.html)

```sh
python3 -m venv .venv
```

- activate venv

```sh
source .venv/bin/activate
```

- deactivate

```sh
deactivate
```

## reference

- check [the installation guide](https://docs.aws.amazon.com/boto3/latest/)
- check [the aws docs boto3](https://docs.aws.amazon.com/boto3/latest/reference/services/s3.html)
