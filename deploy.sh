#!/bin/sh
file="../deployment-package.zip"
batch_1="../dependency_batch_1.zip"
batch_2="../dependency_batch_2.zip"
batch_3="../dependency_batch_3.zip"
batch_4="../dependency_batch_4.zip"
folder_batch_1="dependencies_batch_1/"
folder_batch_2="dependencies_batch_2/"
folder_batch_3="dependencies_batch_3/"
folder_batch_4="dependencies_batch_4/"


directory="./package"
if [ -f "$file" ] ; then
    rm "$file"
fi

if [ -f "$batch_1" ] ; then
    rm "$batch_1"
fi

if [ -f "$batch_2" ] ; then
    rm "$batch_2"
fi

if [ -f "$batch_3" ] ; then
    rm "$batch_3"
fi

if [ -f "$batch_4" ] ; then
    rm "$batch_4"
fi

if [ -d "$directory" ] ; then
    rm -rf "$directory"
fi

if [ -d "$folder_batch_1" ] ; then
    rm -rf "$folder_batch_1"
fi

if [ -d "$folder_batch_2" ] ; then
    rm -rf "$folder_batch_2"
fi

if [ -d "$folder_batch_3" ] ; then
    rm -rf "$folder_batch_3"
fi

if [ -d "$folder_batch_4" ] ; then
    rm -rf "$folder_batch_4"
fi



echo "Installing Runtime Dependencies into batch directories."
pip3 install --no-deps  --upgrade --target ./dependencies_batch_1 -r requirements_batch_1.txt
pip3 install --no-deps  --upgrade --target ./dependencies_batch_2 -r requirements_batch_2.txt
pip3 install --no-deps  --upgrade --target ./dependencies_batch_3 -r requirements_batch_3.txt
pip3 install --no-deps  --upgrade --target ./dependencies_batch_4 -r requirements_batch_4.txt
echo "Modifying File Access."
chmod 644 $(find . -type f)
chmod 755 $(find . -type d)
echo "Creating zip deployment files for dependencies."
zip -r ../dependency_batch_1.zip -r dependencies_batch_1/
zip -r ../dependency_batch_2.zip -r dependencies_batch_2/
zip -r ../dependency_batch_3.zip -r dependencies_batch_3/
zip -r ../dependency_batch_4.zip -r dependencies_batch_4/
echo "Creating zip deployment files for project."
zip -g ../deployment-package.zip main.py
zip -g ../deployment-package.zip RF_new.pkl
zip -g ../deployment-package.zip -r orion/
zip -g ../deployment-package.zip -r Model/
zip -g ../deployment-package.zip -r BuildObjectHelpers/
echo "Done."