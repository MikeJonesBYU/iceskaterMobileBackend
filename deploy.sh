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
pip3 install cycler==0.10.0 --no-deps  --upgrade --target ./cycler-dep
pip3 install joblib==0.14.0 --no-deps  --upgrade --target ./joblib-dep
pip3 install kiwisolver==1.1.0 --no-deps  --upgrade --target ./kiwisolver-dep
pip3 install numpy==1.17.3 --no-deps  --upgrade --target ./numpy-dep
pip3 install matplotlib==3.1.1 --no-deps  --upgrade --target ./matplotlib-dep
pip3 install pandas==0.25.2 --no-deps  --upgrade --target ./pandas-dep
pip3 install pyparsing==2.4.2 --no-deps  --upgrade --target ./pyparsing-dep
pip3 install scipy==1.3.1 --no-deps  --upgrade --target ./scipy-dep
pip3 install shap==0.31.0 --no-deps  --upgrade --target ./shap-dep
pip3 install six==1.12.0 --no-deps  --upgrade --target ./six-dep
pip3 install tqdm==4.36.1 --no-deps  --upgrade --target ./tqdm-dep
pip3 install python-dateutil==2.8.0 --no-deps  --upgrade --target ./shap-dep
pip3 install pytz==2019.3 --no-deps  --upgrade --target ./six-dep
pip3 install scikit-learn==0.21.3 --no-deps  --upgrade --target ./tqdm-dep

echo "Modifying File Access."
chmod 644 $(find . -type f)
chmod 755 $(find . -type d)


zip -r ../cycler.zip -r ./cycler-dep

echo "Creating zip deployment files for project."
zip -g ../deployment-package.zip main.py
zip -g ../deployment-package.zip RF_new.pkl
zip -g ../deployment-package.zip -r orion/
zip -g ../deployment-package.zip -r Model/
zip -g ../deployment-package.zip -r BuildObjectHelpers/
echo "Done."