#!/bin/sh
file="../deployment-package.zip"
directory="./package"
if [ -f "$file" ] ; then
    rm "$file"
fi

if [ -f "$directory" ] ; then
    rm -rf "$directory"
fi

echo "Installing Runtime Dependencies into Package directory."
pip3 install --upgrade --target ./package cython
pip3 install --upgrade --target ./package -r requirements.txt
echo "Modifying File Access."
chmod 644 $(find . -type f)
chmod 755 $(find . -type d)
echo "Creating zip deployment file."
zip -r ../deployment-package.zip -r package/
zip -g ../deployment-package.zip main.py
zip -g ../deployment-package.zip RF_new.pkl
zip -g ../deployment-package.zip -r orion/
zip -g ../deployment-package.zip -r Model/
zip -g ../deployment-package.zip -r BuildObjectHelpers/
echo "Done."