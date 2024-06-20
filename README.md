


```markdown
SNPE SDK Setup and Installation Guide

This guide is intended to help set up and install the 
Snapdragon Neural Processing Engine (SNPE) SDK on a Linux system. 
Once configured correctly, you should be able to convert a 
TensorFlow protobuf file (.pb) to a .dlc Deep Learning Container file.  
This DLC file is used to run deep learning applications on Snapdragon processors.

## Prerequisites

### Supported Python Version

Currently, only Python 3.8 is supported to run SNPE.

```bash
sudo apt-get update
sudo apt-get install python3.8 python3-distutils libpython3.8
sudo apt-get install python3.8-venv
python3.8 -m venv "<PYTHON3.8_VENV_ROOT>"
source <PYTHON3.8_VENV_ROOT>/bin/activate
```

## Download and Install SNPE

Download SNPE from [Qualcomm's website](https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai).

```bash
unzip -X vX.Y.Z.zip
```

## Install Dependencies

```bash
source snpe-vX.Y.Z/bin/dependencies.sh
source snpe-X.Y.Z/bin/check_python_depends.sh
```

## Installing TensorFlow

You will need to install two different versions of TensorFlow: `tf-gpu==1.15` and `tf-gpu==2.10.1`. 
Additionally, you will need to install `tflite` version 2.3 along 
with `tf-2.10.1`.
```bash
pip install tensorflow-gpu==2.10.1 
```
The reason for using two versions of TensorFlow is to obtain frozen
graphs (pb files) from TensorFlow checkpoints (.meta, .index, .data). 

This process is described 
(https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/exporting_models.md).

The above code will work for TensorFlow 1.15 as it requires `tf.slim` and `tf.contrib`, which will cause errors if you use TensorFlow 2.0 and above.

If you already have cuda, cudnn tensorrt  installed, just install  
tensorflow using pip    
```bash
pip install tensorflow-gpu==2.10.1
```
If you face issues while installing any nvidia software,  
Installing tensorflow, cuda, tensorrt and cudnn are described here
https://github.com/rioter1/nvidia_installation  


## Download TensorFlow Models

You can use the following link to download TensorFlow models and 
clone the object detection framework: 
(https://developer.qualcomm.com/sites/default/files/docs/snpe/convert_mobilenetssd.html).

Or execute the following:

```bash
mkdir ~/tfmodels
cd ~/tfmodels
git clone https://github.com/tensorflow/models.git
git checkout ad386df597c069873ace235b931578671526ee00
```

This will provide you with all the model repositories supported by TensorFlow.

# Convert a Quantized SSD .meta to protobuf
you need a seperate virtual enviornment for tensorflow 1.15  
for this code to run .  
```bash
python3 -m venv tf1.15
source tf1.15/bin/activate
pip install tensorflow-gpu==1.15 
```

```bash
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz
tar xzvf ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz
echo export_train.sh
```

In `export_train.sh`, paste the following and change paths to where your weights file exists:

```bash
#!/bin/bash
INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH=<path_to>/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03/pipeline.config
TRAINED_CKPT_PREFIX=<path_to>/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03/model.ckpt
EXPORT_DIR=<path_to>/exported

pushd ~/tfmodels/models/tfmodels/research
python object_detection/export_inference_graph.py \
--input_type=${INPUT_TYPE} \
--pipeline_config_path=${PIPELINE_CONFIG_PATH} \
--trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
--output_directory=${EXPORT_DIR}
popd
```

After creating `export_train.sh`, 

```bash
chmod u+x export_train.sh
./export_train.sh
```
The output of the above script will be a frozen (.pb) file.

# convert a pb file to a dlc file
# Revert back to tensorflow==2.10 environment where snpe is installed
Once you have your pb file, execute below to get yor dlc file
```bash 
snpe-tensorflow-to-dlc --input_network <path_to>/exported/frozen_inference_graph.pb --input_dim Preprocessor/sub 1,300,300,3 --out_node detection_classes --out_node detection_boxes --out_node detection_scores ---output_path mobilenet_ssd.dlc --allow_unconsumed_nodes   
```
