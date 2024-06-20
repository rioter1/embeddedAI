As per https://developer.qualcomm.com/software/qualcomm-neural-processing-sdk/learning-resources/image-segmentation-deeplab-neural-processing-sdk/deeplab-v3-neural-processing-sdk-ubuntu

the inputs to Deeplab network have to undergo preprocessing to convert them into .RAW format  
the code preprocess.py take input images and outputs the .raw images  

After that the .raw images need to be grayscaled. the grayscale.py takes care of that

to download the deeplab model  

```bash
wget http://download.tensorflow.org/models/deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz
tar -xzvf deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz
```
To convert the .pb file to .dlc format, Activate the virtual environment which was used during snpe installation  

```bash
snpe-tensorflow-to-dlc –graph deeplabv3_mnv2_pascal_train_aug/frozen_inference_graph.pb -i sub_7 1,513,513,3 --out_node ArgMax --dlc deeplabv3.dlc --allow_unconsumed_nodes
```

For Quantizing this model using snpe Post Training Quantization (PTQ)  

Put raw images a .txt format 

```bash
find $(pwd)/preprocessed -name '*.raw' > input_list.txt
```

Quantize

```bash
snpe-dlc-quantize --input_dlc model.dlc --input_list input_list.txt --output_dlc quantized_model.dlc
```

