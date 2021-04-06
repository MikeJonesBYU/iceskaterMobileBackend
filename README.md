Perform these to package the deployment for AWS Lambda

pip3 install --target ./package -r requirements.txt
chmod 644 $(find . -type f) : do in project root
chmod 755 $(find . -type d) : do in project root
cd package
zip -r ../my-deployment-package.zip .
zip -g ../my-deployment-package.zip -r .
