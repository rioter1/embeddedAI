# This Readme is meant to help setup and install Snapdragon neural processing (SNPE) SDK on a linux system. Once working correctly, it should be able to convert a tensorflow protobuf file (.pb) to a .dlc deep lab container file. This dlc file is used to run deep learning applications on snapdragon processor. 

# Presently only python 3.8 is supported to run snpe
sudo apt-get update   
sudo apt-get install python3.8 python3-distutils libpython3.8   

sudo apt-get install python3.8-venv  
python3.8 -m venv "<PYTHON3.8_VENV_ROOT>"  
source <PYTHON3.8_VENV_ROOT>/bin/activate  

# Download SNPE from https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai

unzip -X vX.Y.Z.zip  

# install dependencies.
source snpe-vX.Y.Z/bin/dependencies.sh  
source snpe-X.Y.Z/bin/check_python_depends.sh  

# Installing tensorflow
# you will need to install 2 different versions of tensorflow, tf-gpu==1.15 and tf-gpu==2.10




 

