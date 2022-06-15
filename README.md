## Quick start Docker/AWS Video Tutorial
This is a video about Docker, how it is used in the project and an example of how to build/push the image to an AWS lambda function. Email me at jeremysl123@gmail.com with further questions. Also, let me know if you want access to a Udemy course about docker.
https://youtu.be/tiPr9KrqvjU

## Elastic Container Registry (ECR)
https://console.aws.amazon.com/ecr/repositories/private/390539340647/backend_dependencies?region=us-east-1
This is the Container Registry which holds the image that the lambda will use to run our project.

## Making a new ECR
In case this project ever needs additional docker image registries, this document might help.
https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

## Building and Pushing the Docker Image to AWS:
First, log in to AWS from the command line (make sure you have aws-cli!):

0: aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 390539340647.dkr.ecr.us-east-1.amazonaws.com

The login only has to be done once. It will expire after some time (5+ hours?), after which you need to log in again. 

Next, build the image using docker (make sure this is done in the backend folder):

1: docker build -t backend_dependencies:<optional_tag> .

Tag the image so that it can be pushed to ECR:

2: docker tag backend_dependencies:<the_same_optional_tag/latest> 390539340647.dkr.ecr.us-east-1.amazonaws.com/backend_dependencies:<the_same_optional_tag/latest>

Finally, push to ECR:

3: docker push 390539340647.dkr.ecr.us-east-1.amazonaws.com/backend_dependencies:<the_same_optional_tag/latest>

The tag can be left blank, but it can help identify containers afterwards. For example, I've been using version numbers 1.0, 1.1, ... 2.0, etc. Whenever the first number changes, I achieved a stable version that accomplished some milestone. That way I can go back to that version if I need to. 
For the commands, if a tag is specified when building, the same tag should be used for the rest of the commands. If no tag is specified, "latest" should be used as the tag.

To then deploy the image, go to: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/event_classifier?tab=code
This is our lambda that runs the event_classifier. Then press "Deploy new image", Select the image that you just pushed up or get the URI from the ECR.

#### Debugging tips

It is somewhat slow of a process to always upload the image to AWS, switch out the container on that end, and test it there.
There is a faster way to do it locally. You still want to build it with command 1. from above, after which you can do the following:

1: docker run -t -i -p 9000:8080  backend_dependencies:<tag/latest> 

From a separate terminal:

2: curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @test_file_location

The URL is a mystery, but it works. The -d option allows us to specify input, and @test_file_location is the input. For example, if the file is in the same directory, you could just use -d @test.txt. 
If it's somewhere else, just specify the path: @dir/subdir/test.txt.

Hopefully, this helps!
