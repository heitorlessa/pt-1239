# Background

Minimal project to reproduce [Lambda Powertools issue 1239](https://github.com/awslabs/aws-lambda-powertools-python/issues/1239), where metrics aren't being created when 9 dimensions are used.

# Reproduce

Make sure you have the following tools installed first.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

```bash
sam build --use-container
sam deploy --guided
```

After deploying, set `ENDPOINT` environment variable with the value of `HelloWorldApi` CloudFormation Output.

> Bash example

```bash
ENDPOINT="https://o4w3zen6mj.execute-api.eu-west-1.amazonaws.com/Prod/hello/"
```

Within the same shell, use your preferred HTTP client to send a few requests to generate metric values.

> Generating 100 data points (1 per sec)

```bash
for i in $(seq 1 1000); do curl ${ENDPOINT} && sleep 1; done
```