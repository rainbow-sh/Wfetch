#!/bin/bash

# Exit when any command fails
set -e
set -o pipefail

# Keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# Echo an error message before exiting
trap 'ERROR_CODE=$?; FAILED_COMMAND=$LAST_COMMAND; tput setaf 1; echo "ERROR: command \"$FAILED_COMMAND\" failed with exit code $ERROR_CODE"; put sgr0;' ERR INT TERM

# Curl install
if ! test -d "wfetch"; then
    git clone "https://github.com/Gcat101/Wfetch.git" > /dev/null
    cd ./Wfetch 
fi

echo "Installing package requirements..."
# Silencing command output and only printing errors
/usr/bin/python3 -m pip install -r ./requirements.txt > /dev/null

echo "Installing package..."
# Moving into ./wfetch directory
cd ./wfetch
# Copying binary to path
cp ./wfetch.py /usr/local/bin/wfetch
# Copy icons to opt
cp -r ./icons /opt/wfetch

echo "Cleaning up..."
# Moving to parent directory
cd ../../ 
# Deleting the copied github folder
rm -rf ./wfetch
echo -e "Package Installed! \n"

echo -e "Please add this line to your shell profile (You are using $SHELL):"
echo "'export WEATHER_CLI_API=<your OWM api key>'"
exit
