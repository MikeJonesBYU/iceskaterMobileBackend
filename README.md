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

