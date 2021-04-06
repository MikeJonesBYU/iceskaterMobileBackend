# Perform these to package the deployment for AWS Lambda

1. pip3 install --target ./package -r requirements.txt : project root
2. chmod 644 $(find . -type f) : do in project root
3. chmod 755 $(find . -type d) : do in project root
4. cd package
5. zip -r ../my-deployment-package.zip .
6. zip -g ../my-deployment-package.zip -r .
