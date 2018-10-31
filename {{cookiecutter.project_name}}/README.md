# {{cookiecutter.project_name}}


## Pre-requisites
- Python 3.6.5 (take a look at [`pyenv`](https://github.com/pyenv/pyenv))

## How to run locally

- Clone this repo
- Create a Python 3.6.5 virtual env: `mkvirtualenv {{cookiecutter.project_name}} --python=python3.6.5`
- Install dependencies: `pip install -r src/requirements-dev.txt`
- Install Local DynamoDB: `sudo make install-ddb`
- Start local DynamoDB instance: `make start-ddb -C src/`
- Run tests: `make test -C src/`
- Start local app server: `make run -C src/`

You can access using `http://localhost:8000`


## CI/CD pipeline

### Create CloudFormation stack

```
aws cloudformation deploy --stack-name {{cookiecutter.project_name}} --template-file pipeline.yaml --capabilities CAPABILITY_IAM
```

### Setup CodeCommit integration

Use the CodeCommit endpoint provided by the CloudFormation stack output.

```
git remote add codecommit [codecommit-url]
```

Tips for setting up CodeCommit credentials: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html
