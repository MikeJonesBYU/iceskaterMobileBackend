# Perform these to package the deployment for AWS Lambda


This is the right step: https://towardsdatascience.com/how-to-build-an-aws-lambda-for-data-science-cec62deaf0e9
Don't try to package and zip the project & its dependencies like AWS first suggests. Unfortunately, the file is way over the 250MB limit & there's other problems. The next best thing is to use a Docker image.

## Notes
I've had a hard time figuring this out. Unfortunately it came to the end and I ran out of time. This is what I've learned:

## Elastic Container Service
Signin then go to https://console.aws.amazon.com/ecr/repositories/private/390539340647/backend_dependencies?region=us-east-1
This is the Container Registry which holds our image that the lambda will use to run our project.
Although intimidating Docker is pretty simple, the tricky part is getting it to play nice with our AWS.

## Building the image using the Dockerfile
When you get to the ECR section and see the "backend_dependencies" private repo, click on "View push commands" in the top right after you select the repo. This gives you all the instructions you need to login, build the Docker image, and push the image to our registry. 

## Testing the container with AWS Lambda
To then test it go to: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/event_classifier?tab=code
This is our lambda that runs the event_classifier. Then press "Deploy new image", Select the image that you just pushed up, then go to the "Test" tab and press Test. Resolve all errors. 

I created a test event which has json of the session test of Colorado Springs Skater File AK1_09. I suggest testing with a simplier one first.

## Update June 11 2021, Miki:
There are functional containers in the ECR now, and they work exactly like Travis specified. For simplicity, I'll list the required commands here:

First, to log in to AWS from the command line (make sure you have aws-cli!):

0: aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 390539340647.dkr.ecr.us-east-1.amazonaws.com

The login only has to be done once. It will expire after some time (5+ hours?), after which you need to log in again. Next, build the image using docker:

1: docker build -t backend_dependencies:<optional_tag> .

Tag the image so that it can be pushed to ECR:

2: docker tag backend_dependencies:<the_same_optional_tag/latest> 390539340647.dkr.ecr.us-east-1.amazonaws.com/backend_dependencies:<the_same_optional_tag/latest>

Finally, push to ECR:

3: docker push 390539340647.dkr.ecr.us-east-1.amazonaws.com/backend_dependencies:<the_same_optional_tag/latest>

The tag can be left blank, but it can help identify containers afterwards. For example, I've been using version numbers 1.0, 1.1, ... 2.0, etc. Whenever the first number changes, I achieved a stable version that accomplished some milestone. That way I can go back to that version if I need to. 
For the commands, if a tag is specified when building, the same tag should be used for the rest of the commands. If no tag is specified, "latest" should be used as the tag.

####Debugging tips

It is somewhat slow of a process to always upload the image to AWS, switch out the container on that end, and test it there.
There is a faster way to do it locally. You still want to build it with command 1. from above, after which you can do the following:

1: docker run -p -i -t 9000:8080  backend_dependencies:<tag/latest> 

From a separate terminal:

2: curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @test_file_location

The URL is a mystery, but it works. The -d option allows us to specify input, and @test_file_location is the input. For example, if the file is in the same directory, you could just use -d @test.txt. 
If it's somewhere else, just specify the path: @dir/subdir/test.txt.

Hopefully this helps!