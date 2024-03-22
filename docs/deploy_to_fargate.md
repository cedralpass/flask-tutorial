# Deploy to Fargate
## Amazon ECR
We first have an ECR repository created
```flask-container```
## Docker container build
We have a Docker file in root ```Dockerfile.aws``` which has one detail to build for AMD64, required for our Fargate cluster not running on M1 Chips.

# Steps
## Build Docker Image using docker file
```
docker build -t flask-container . -f Dockerfile.aws
```

## Tag Docker File with latest tag
```
docker tag flask-container:latest <account>.dkr.ecr.us-west-2.amazonaws.com/flask-container:latest
```
## Deploy docker file to ECR

```
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-west-2.amazonaws.com
docker push <account>.dkr.ecr.us-west-2.amazonaws.com/flask-container:latest    
```
## Build Fargate Service
Followed this blog to build the service
[Deploying a Docker container with ECS and Fargate](https://aws.plainenglish.io/deploying-a-docker-container-in-aws-using-fargate-5a19a140b018)

# Back to Readme
[back](../README.md)