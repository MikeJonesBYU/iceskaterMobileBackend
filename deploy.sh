#!/bin/sh
file="../deployment-package.zip"

if [ -f "$file" ] ; then
    rm "$file"
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
pip3 install python-dateutil==2.8.0 --no-deps  --upgrade --target ./dateutil-dep
pip3 install pytz==2019.3 --no-deps  --upgrade --target ./pytz-dep
pip3 install scikit-learn==0.21.3 --no-deps  --upgrade --target ./scikit-dep

echo "Modifying File Access."
chmod 644 $(find . -type f)
chmod 755 $(find . -type d)

echo "Zipping up dependencies."
zip -FSr ../cycler.zip ./cycler-dep
zip -FSr ../joblib.zip ./joblib-dep
zip -FSr ../kiwisolver.zip ./kiwisolver-dep
zip -FSr ../numpy.zip ./numpy-dep
zip -FSr ../matplotlib.zip ./matplotlib-dep
zip -FSr ../pandas.zip ./pandas-dep
zip -FSr ../pyparsing.zip ./pyparsing-dep
zip -FSr ../scipy.zip ./scipy-dep
zip -FSr ../shap.zip ./shap-dep
zip -FSr ../six.zip ./six-dep
zip -FSr ../tqdm.zip ./tqdm-dep
zip -FSr ../dateutil.zip ./dateutil-dep
zip -FSr ../pytz.zip ./pytz-dep
zip -FSr ../scikit.zip ./scikit-dep

echo "Cleaning house."
rm -rf ./cycler-dep
rm -rf ./joblib-dep
rm -rf ./kiwisolver-dep
rm -rf ./numpy-dep
rm -rf ./matplotlib-dep
rm -rf ./pandas-dep
rm -rf ./pyparsing-dep
rm -rf ./scipy-dep
rm -rf ./shap-dep
rm -rf ./six-dep
rm -rf ./tqdm-dep
rm -rf ./dateutil-dep
rm -rf ./pytz-dep
rm -rf ./scikit-dep

echo "Creating zip deployment files for project."
zip -g ../deployment-package.zip main.py
zip -g ../deployment-package.zip RF_new.pkl
zip -g ../deployment-package.zip -r orion/
zip -g ../deployment-package.zip -r Model/
zip -g ../deployment-package.zip -r BuildObjectHelpers/
echo "Done."