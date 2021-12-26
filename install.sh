#!bin/bash

# exit when any command fails
set -e
set -o pipefail

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'ERROR_CODE=$?; FAILED_COMMAND=$LAST_COMMAND; tput setaf 1; echo "ERROR: command \"$FAILED_COMMAND\" failed with exit code $ERROR_CODE"; put sgr0;' ERR INT TERM


echo "Installing package requirements..."
# silencing command output and only printing errors
/usr/bin/python3 -m pip install -r ./requirements.txt > /dev/null

echo "Installing package..."
# Moving into ./wfetch directory
cd ./wfetch
# Copying binary to path
sudo cp -a ./wfetch.py /usr/local/bin/wfetch

echo "Cleaning up..."
# moving to parent directory
cd ../../ 
# Deleting the copied github folder
rm -rf ./wfetch
echo -e "Package Installed! \n"

echo -e "Please add this line to your shell profile (You are using $SHELL):"
echo "'export WEATHER_CLI_API=<your OWM api key>'"
exit