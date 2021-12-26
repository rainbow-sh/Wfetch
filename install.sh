# INSTALL SCRIPT

/usr/bin/python3 -m pip install -r ./requirements.txt # Installing requirements from requirements.txt
cd ./src/wfetch # Cd-ing into src/wfetch directory
mv ./wfetch.py ./wfetch # Removing .py from the wfetch.py name
cp -a ./. /usr/local/bin # Copying all of the files to path
cd ../../../ # Un-cding
rm -rf ./wfetch # Deleting the copied github folder