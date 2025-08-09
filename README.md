# aws-ci-cd-sample-app
CI-CD Implementation using AWS Managed services like code pipeline, code build and code deploy
This is a Project where Iam using GIT as my source where the code changes are are committed and pushed to GIT HUB.
Once the Code is pushed into the GIT HUB with code commit, the AWS Managed service CODE PIPELINE acts as a orchestrator
where it monitors the GIT HUB and intiates the CODE BUILD service once there is any code commit.

CODE BUILD:

CODE BUILD is an AWS Managed service where it is used to BUILD the code and the resultant artifact/image  is pushed to the DOCKER HUB.
Once the CODE BUILD service pushes the image to the DOCKER HUB, then the CODE PIPELINE Service triggers the CODE DEPLOY

CODE DEPLOY:

CODE DEPLOY is an AWS Managed service where it used to deploy the images to the target EC2/ECS.
In our project we are going to deploy the container image to EC2.
Here while deploying the container image we will attach the polocies to the EC2 instance and to the CODE DEPLOY service to interact each other.
We will install CODE DEPLOY agent into the EC2 Machine in order to listen to the CODE DEPLOY.
We will use TAGS as an identifier for our target EC2 Machine to easily finds the CODE DEPLOY service to push the conatainer Image.

We will install the DOCKER into the EC2 Instance to Manage and the DOCKER Container in the EC2 Machine.



                   USER  ---->  GIT HUB  ----> CODE BUILD ---> DOCKER HUB --->  CODE DEPLOY ----> AMAZON EC2
                                               --------------------------------------------
                                                              CODE PIPELINE   


