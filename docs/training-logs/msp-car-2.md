# Training run for Minneapolis STEM Partners

Car #2 had 15045 images

wc -l ~/mycar/data/msp-car-2/*.catalog
15045
# ls -1 ~/mycar/data/msp-car-2/images | wc -l
15045

```sh
(donkey) arl@arl1:~/mycar$ donkey train --tub=./data/msp-car-2 --model=./models/msp-car-2.h5
________             ______                   _________              
___  __ \_______________  /___________  __    __  ____/_____ ________
__  / / /  __ \_  __ \_  //_/  _ \_  / / /    _  /    _  __ `/_  ___/
_  /_/ // /_/ /  / / /  ,<  /  __/  /_/ /     / /___  / /_/ /_  /    
/_____/ \____//_/ /_//_/|_| \___/_\__, /      \____/  \__,_/ /_/     
                                 /____/                              

using donkey v4.2.1 ...
loading config file: ./config.py
loading personal config over-rides from myconfig.py
"get_model_by_type" model Type is: linear
Created KerasLinear
2021-07-26 20:22:54.320076: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2021-07-26 20:22:54.338339: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.338783: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 20:22:54.338925: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 20:22:54.339823: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 20:22:54.340834: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 20:22:54.340981: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 20:22:54.341775: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 20:22:54.342170: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 20:22:54.343898: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 20:22:54.344043: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.344546: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.344933: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 20:22:54.345163: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2021-07-26 20:22:54.349277: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3592950000 Hz
2021-07-26 20:22:54.349572: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5575e341a9f0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-07-26 20:22:54.349585: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-07-26 20:22:54.349717: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.350124: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 20:22:54.350160: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 20:22:54.350171: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 20:22:54.350180: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 20:22:54.350191: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 20:22:54.350200: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 20:22:54.350210: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 20:22:54.350220: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 20:22:54.350282: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.350723: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.351106: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 20:22:54.351127: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 20:22:54.423106: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-07-26 20:22:54.423133: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2021-07-26 20:22:54.423138: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2021-07-26 20:22:54.423354: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.423819: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.424248: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 20:22:54.424632: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 9890 MB memory) -> physical GPU (device: 0, name: NVIDIA GeForce RTX 2080 Ti, pci bus id: 0000:09:00.0, compute capability: 7.5)
2021-07-26 20:22:54.425999: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5575e52b18b0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2021-07-26 20:22:54.426009: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): NVIDIA GeForce RTX 2080 Ti, Compute Capability 7.5
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
img_in (InputLayer)             [(None, 224, 224, 3) 0                                            
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 110, 110, 24) 1824        img_in[0][0]                     
__________________________________________________________________________________________________
dropout (Dropout)               (None, 110, 110, 24) 0           conv2d_1[0][0]                   
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 53, 53, 32)   19232       dropout[0][0]                    
__________________________________________________________________________________________________
dropout_1 (Dropout)             (None, 53, 53, 32)   0           conv2d_2[0][0]                   
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 25, 25, 64)   51264       dropout_1[0][0]                  
__________________________________________________________________________________________________
dropout_2 (Dropout)             (None, 25, 25, 64)   0           conv2d_3[0][0]                   
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 23, 23, 64)   36928       dropout_2[0][0]                  
__________________________________________________________________________________________________
dropout_3 (Dropout)             (None, 23, 23, 64)   0           conv2d_4[0][0]                   
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 21, 21, 64)   36928       dropout_3[0][0]                  
__________________________________________________________________________________________________
dropout_4 (Dropout)             (None, 21, 21, 64)   0           conv2d_5[0][0]                   
__________________________________________________________________________________________________
flattened (Flatten)             (None, 28224)        0           dropout_4[0][0]                  
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 100)          2822500     flattened[0][0]                  
__________________________________________________________________________________________________
dropout_5 (Dropout)             (None, 100)          0           dense_1[0][0]                    
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 50)           5050        dropout_5[0][0]                  
__________________________________________________________________________________________________
dropout_6 (Dropout)             (None, 50)           0           dense_2[0][0]                    
__________________________________________________________________________________________________
n_outputs0 (Dense)              (None, 1)            51          dropout_6[0][0]                  
__________________________________________________________________________________________________
n_outputs1 (Dense)              (None, 1)            51          dropout_6[0][0]                  
==================================================================================================
Total params: 2,973,828
Trainable params: 2,973,828
Non-trainable params: 0
__________________________________________________________________________________________________
None
Using catalog /home/arl/mycar/data/msp-car-2/catalog_22.catalog

Records # Training 11696
Records # Validation 2924
Epoch 1/100
2021-07-26 20:22:55.471623: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 20:22:55.802565: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 20:22:56.515413: W tensorflow/stream_executor/gpu/asm_compiler.cc:116] *** WARNING *** You are using ptxas 9.1.108, which is older than 9.2.88. ptxas 9.x before 9.2.88 is known to miscompile XLA code, leading to incorrect results or invalid-address errors.

You do not need to update to CUDA 9.2.88; cherry-picking the ptxas binary is sufficient.
2021-07-26 20:22:56.559204: W tensorflow/stream_executor/gpu/redzone_allocator.cc:314] Internal: ptxas exited with non-zero error code 65280, output: ptxas fatal   : Value 'sm_75' is not defined for option 'gpu-name'

Relying on driver to perform ptx compilation. 
Modify $PATH to customize ptxas location.
This message will be only logged once.
92/92 [==============================] - ETA: 0s - loss: 0.6304 - n_outputs0_loss: 0.3238 - n_outputs1_loss: 0.3066 
Epoch 00001: val_loss improved from inf to 0.59133, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 29s 310ms/step - loss: 0.6304 - n_outputs0_loss: 0.3238 - n_outputs1_loss: 0.3066 - val_loss: 0.5913 - val_n_outputs0_loss: 0.3121 - val_n_outputs1_loss: 0.2793
Epoch 2/100
92/92 [==============================] - ETA: 0s - loss: 0.5150 - n_outputs0_loss: 0.2730 - n_outputs1_loss: 0.2419
Epoch 00002: val_loss improved from 0.59133 to 0.39368, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 11s 117ms/step - loss: 0.5150 - n_outputs0_loss: 0.2730 - n_outputs1_loss: 0.2419 - val_loss: 0.3937 - val_n_outputs0_loss: 0.2108 - val_n_outputs1_loss: 0.1828
Epoch 3/100
92/92 [==============================] - ETA: 0s - loss: 0.3885 - n_outputs0_loss: 0.2088 - n_outputs1_loss: 0.1797
Epoch 00003: val_loss improved from 0.39368 to 0.34087, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 11s 117ms/step - loss: 0.3885 - n_outputs0_loss: 0.2088 - n_outputs1_loss: 0.1797 - val_loss: 0.3409 - val_n_outputs0_loss: 0.1923 - val_n_outputs1_loss: 0.1486
Epoch 4/100
92/92 [==============================] - ETA: 0s - loss: 0.3449 - n_outputs0_loss: 0.1870 - n_outputs1_loss: 0.1579
Epoch 00004: val_loss improved from 0.34087 to 0.30588, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 11s 119ms/step - loss: 0.3449 - n_outputs0_loss: 0.1870 - n_outputs1_loss: 0.1579 - val_loss: 0.3059 - val_n_outputs0_loss: 0.1771 - val_n_outputs1_loss: 0.1288
Epoch 5/100
92/92 [==============================] - ETA: 0s - loss: 0.3161 - n_outputs0_loss: 0.1763 - n_outputs1_loss: 0.1397
Epoch 00005: val_loss improved from 0.30588 to 0.28650, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 113ms/step - loss: 0.3161 - n_outputs0_loss: 0.1763 - n_outputs1_loss: 0.1397 - val_loss: 0.2865 - val_n_outputs0_loss: 0.1722 - val_n_outputs1_loss: 0.1143
Epoch 6/100
92/92 [==============================] - ETA: 0s - loss: 0.2876 - n_outputs0_loss: 0.1633 - n_outputs1_loss: 0.1243
Epoch 00006: val_loss improved from 0.28650 to 0.26754, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 110ms/step - loss: 0.2876 - n_outputs0_loss: 0.1633 - n_outputs1_loss: 0.1243 - val_loss: 0.2675 - val_n_outputs0_loss: 0.1623 - val_n_outputs1_loss: 0.1053
Epoch 7/100
92/92 [==============================] - ETA: 0s - loss: 0.2612 - n_outputs0_loss: 0.1508 - n_outputs1_loss: 0.1103
Epoch 00007: val_loss improved from 0.26754 to 0.25034, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.2612 - n_outputs0_loss: 0.1508 - n_outputs1_loss: 0.1103 - val_loss: 0.2503 - val_n_outputs0_loss: 0.1551 - val_n_outputs1_loss: 0.0952
Epoch 8/100
92/92 [==============================] - ETA: 0s - loss: 0.2476 - n_outputs0_loss: 0.1435 - n_outputs1_loss: 0.1041
Epoch 00008: val_loss improved from 0.25034 to 0.24291, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 109ms/step - loss: 0.2476 - n_outputs0_loss: 0.1435 - n_outputs1_loss: 0.1041 - val_loss: 0.2429 - val_n_outputs0_loss: 0.1524 - val_n_outputs1_loss: 0.0905
Epoch 9/100
92/92 [==============================] - ETA: 0s - loss: 0.2283 - n_outputs0_loss: 0.1323 - n_outputs1_loss: 0.0960
Epoch 00009: val_loss improved from 0.24291 to 0.22718, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 110ms/step - loss: 0.2283 - n_outputs0_loss: 0.1323 - n_outputs1_loss: 0.0960 - val_loss: 0.2272 - val_n_outputs0_loss: 0.1450 - val_n_outputs1_loss: 0.0821
Epoch 10/100
92/92 [==============================] - ETA: 0s - loss: 0.2183 - n_outputs0_loss: 0.1267 - n_outputs1_loss: 0.0916
Epoch 00010: val_loss did not improve from 0.22718
92/92 [==============================] - 10s 109ms/step - loss: 0.2183 - n_outputs0_loss: 0.1267 - n_outputs1_loss: 0.0916 - val_loss: 0.2305 - val_n_outputs0_loss: 0.1471 - val_n_outputs1_loss: 0.0834
Epoch 11/100
92/92 [==============================] - ETA: 0s - loss: 0.2022 - n_outputs0_loss: 0.1187 - n_outputs1_loss: 0.0835
Epoch 00011: val_loss improved from 0.22718 to 0.21581, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 110ms/step - loss: 0.2022 - n_outputs0_loss: 0.1187 - n_outputs1_loss: 0.0835 - val_loss: 0.2158 - val_n_outputs0_loss: 0.1375 - val_n_outputs1_loss: 0.0783
Epoch 12/100
92/92 [==============================] - ETA: 0s - loss: 0.1921 - n_outputs0_loss: 0.1085 - n_outputs1_loss: 0.0836
Epoch 00012: val_loss did not improve from 0.21581
92/92 [==============================] - 10s 110ms/step - loss: 0.1921 - n_outputs0_loss: 0.1085 - n_outputs1_loss: 0.0836 - val_loss: 0.2185 - val_n_outputs0_loss: 0.1382 - val_n_outputs1_loss: 0.0802
Epoch 13/100
92/92 [==============================] - ETA: 0s - loss: 0.1826 - n_outputs0_loss: 0.1056 - n_outputs1_loss: 0.0770
Epoch 00013: val_loss did not improve from 0.21581
92/92 [==============================] - 10s 110ms/step - loss: 0.1826 - n_outputs0_loss: 0.1056 - n_outputs1_loss: 0.0770 - val_loss: 0.2198 - val_n_outputs0_loss: 0.1394 - val_n_outputs1_loss: 0.0804
Epoch 14/100
92/92 [==============================] - ETA: 0s - loss: 0.1771 - n_outputs0_loss: 0.1009 - n_outputs1_loss: 0.0762
Epoch 00014: val_loss did not improve from 0.21581
92/92 [==============================] - 10s 111ms/step - loss: 0.1771 - n_outputs0_loss: 0.1009 - n_outputs1_loss: 0.0762 - val_loss: 0.2167 - val_n_outputs0_loss: 0.1389 - val_n_outputs1_loss: 0.0778
Epoch 15/100
92/92 [==============================] - ETA: 0s - loss: 0.1676 - n_outputs0_loss: 0.0959 - n_outputs1_loss: 0.0718
Epoch 00015: val_loss improved from 0.21581 to 0.20899, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 112ms/step - loss: 0.1676 - n_outputs0_loss: 0.0959 - n_outputs1_loss: 0.0718 - val_loss: 0.2090 - val_n_outputs0_loss: 0.1345 - val_n_outputs1_loss: 0.0745
Epoch 16/100
92/92 [==============================] - ETA: 0s - loss: 0.1608 - n_outputs0_loss: 0.0910 - n_outputs1_loss: 0.0698
Epoch 00016: val_loss did not improve from 0.20899
92/92 [==============================] - 10s 110ms/step - loss: 0.1608 - n_outputs0_loss: 0.0910 - n_outputs1_loss: 0.0698 - val_loss: 0.2097 - val_n_outputs0_loss: 0.1348 - val_n_outputs1_loss: 0.0748
Epoch 17/100
92/92 [==============================] - ETA: 0s - loss: 0.1534 - n_outputs0_loss: 0.0870 - n_outputs1_loss: 0.0664
Epoch 00017: val_loss improved from 0.20899 to 0.20324, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 112ms/step - loss: 0.1534 - n_outputs0_loss: 0.0870 - n_outputs1_loss: 0.0664 - val_loss: 0.2032 - val_n_outputs0_loss: 0.1329 - val_n_outputs1_loss: 0.0703
Epoch 18/100
92/92 [==============================] - ETA: 0s - loss: 0.1490 - n_outputs0_loss: 0.0846 - n_outputs1_loss: 0.0644
Epoch 00018: val_loss improved from 0.20324 to 0.19965, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1490 - n_outputs0_loss: 0.0846 - n_outputs1_loss: 0.0644 - val_loss: 0.1997 - val_n_outputs0_loss: 0.1309 - val_n_outputs1_loss: 0.0688
Epoch 19/100
92/92 [==============================] - ETA: 0s - loss: 0.1452 - n_outputs0_loss: 0.0828 - n_outputs1_loss: 0.0624
Epoch 00019: val_loss improved from 0.19965 to 0.19877, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1452 - n_outputs0_loss: 0.0828 - n_outputs1_loss: 0.0624 - val_loss: 0.1988 - val_n_outputs0_loss: 0.1294 - val_n_outputs1_loss: 0.0694
Epoch 20/100
92/92 [==============================] - ETA: 0s - loss: 0.1353 - n_outputs0_loss: 0.0747 - n_outputs1_loss: 0.0606
Epoch 00020: val_loss did not improve from 0.19877
92/92 [==============================] - 10s 110ms/step - loss: 0.1353 - n_outputs0_loss: 0.0747 - n_outputs1_loss: 0.0606 - val_loss: 0.2004 - val_n_outputs0_loss: 0.1312 - val_n_outputs1_loss: 0.0692
Epoch 21/100
92/92 [==============================] - ETA: 0s - loss: 0.1319 - n_outputs0_loss: 0.0731 - n_outputs1_loss: 0.0588
Epoch 00021: val_loss improved from 0.19877 to 0.19564, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1319 - n_outputs0_loss: 0.0731 - n_outputs1_loss: 0.0588 - val_loss: 0.1956 - val_n_outputs0_loss: 0.1252 - val_n_outputs1_loss: 0.0704
Epoch 22/100
92/92 [==============================] - ETA: 0s - loss: 0.1299 - n_outputs0_loss: 0.0713 - n_outputs1_loss: 0.0585
Epoch 00022: val_loss improved from 0.19564 to 0.19422, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1299 - n_outputs0_loss: 0.0713 - n_outputs1_loss: 0.0585 - val_loss: 0.1942 - val_n_outputs0_loss: 0.1259 - val_n_outputs1_loss: 0.0683
Epoch 23/100
92/92 [==============================] - ETA: 0s - loss: 0.1231 - n_outputs0_loss: 0.0684 - n_outputs1_loss: 0.0548
Epoch 00023: val_loss improved from 0.19422 to 0.19270, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1231 - n_outputs0_loss: 0.0684 - n_outputs1_loss: 0.0548 - val_loss: 0.1927 - val_n_outputs0_loss: 0.1245 - val_n_outputs1_loss: 0.0682
Epoch 24/100
92/92 [==============================] - ETA: 0s - loss: 0.1239 - n_outputs0_loss: 0.0673 - n_outputs1_loss: 0.0566
Epoch 00024: val_loss did not improve from 0.19270
92/92 [==============================] - 10s 110ms/step - loss: 0.1239 - n_outputs0_loss: 0.0673 - n_outputs1_loss: 0.0566 - val_loss: 0.1969 - val_n_outputs0_loss: 0.1283 - val_n_outputs1_loss: 0.0686
Epoch 25/100
92/92 [==============================] - ETA: 0s - loss: 0.1200 - n_outputs0_loss: 0.0650 - n_outputs1_loss: 0.0550
Epoch 00025: val_loss did not improve from 0.19270
92/92 [==============================] - 10s 111ms/step - loss: 0.1200 - n_outputs0_loss: 0.0650 - n_outputs1_loss: 0.0550 - val_loss: 0.1990 - val_n_outputs0_loss: 0.1284 - val_n_outputs1_loss: 0.0706
Epoch 26/100
92/92 [==============================] - ETA: 0s - loss: 0.1171 - n_outputs0_loss: 0.0636 - n_outputs1_loss: 0.0535
Epoch 00026: val_loss did not improve from 0.19270
92/92 [==============================] - 10s 111ms/step - loss: 0.1171 - n_outputs0_loss: 0.0636 - n_outputs1_loss: 0.0535 - val_loss: 0.1929 - val_n_outputs0_loss: 0.1250 - val_n_outputs1_loss: 0.0678
Epoch 27/100
92/92 [==============================] - ETA: 0s - loss: 0.1167 - n_outputs0_loss: 0.0638 - n_outputs1_loss: 0.0529
Epoch 00027: val_loss did not improve from 0.19270
92/92 [==============================] - 10s 112ms/step - loss: 0.1167 - n_outputs0_loss: 0.0638 - n_outputs1_loss: 0.0529 - val_loss: 0.1937 - val_n_outputs0_loss: 0.1269 - val_n_outputs1_loss: 0.0668
Epoch 28/100
92/92 [==============================] - ETA: 0s - loss: 0.1123 - n_outputs0_loss: 0.0610 - n_outputs1_loss: 0.0513
Epoch 00028: val_loss improved from 0.19270 to 0.19161, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 112ms/step - loss: 0.1123 - n_outputs0_loss: 0.0610 - n_outputs1_loss: 0.0513 - val_loss: 0.1916 - val_n_outputs0_loss: 0.1230 - val_n_outputs1_loss: 0.0686
Epoch 29/100
92/92 [==============================] - ETA: 0s - loss: 0.1086 - n_outputs0_loss: 0.0584 - n_outputs1_loss: 0.0501
Epoch 00029: val_loss improved from 0.19161 to 0.18655, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 110ms/step - loss: 0.1086 - n_outputs0_loss: 0.0584 - n_outputs1_loss: 0.0501 - val_loss: 0.1865 - val_n_outputs0_loss: 0.1216 - val_n_outputs1_loss: 0.0650
Epoch 30/100
92/92 [==============================] - ETA: 0s - loss: 0.1093 - n_outputs0_loss: 0.0593 - n_outputs1_loss: 0.0500
Epoch 00030: val_loss did not improve from 0.18655
92/92 [==============================] - 10s 109ms/step - loss: 0.1093 - n_outputs0_loss: 0.0593 - n_outputs1_loss: 0.0500 - val_loss: 0.1936 - val_n_outputs0_loss: 0.1240 - val_n_outputs1_loss: 0.0696
Epoch 31/100
92/92 [==============================] - ETA: 0s - loss: 0.1077 - n_outputs0_loss: 0.0578 - n_outputs1_loss: 0.0499
Epoch 00031: val_loss did not improve from 0.18655
92/92 [==============================] - 10s 110ms/step - loss: 0.1077 - n_outputs0_loss: 0.0578 - n_outputs1_loss: 0.0499 - val_loss: 0.1889 - val_n_outputs0_loss: 0.1222 - val_n_outputs1_loss: 0.0667
Epoch 32/100
92/92 [==============================] - ETA: 0s - loss: 0.1026 - n_outputs0_loss: 0.0551 - n_outputs1_loss: 0.0475
Epoch 00032: val_loss improved from 0.18655 to 0.18343, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 111ms/step - loss: 0.1026 - n_outputs0_loss: 0.0551 - n_outputs1_loss: 0.0475 - val_loss: 0.1834 - val_n_outputs0_loss: 0.1206 - val_n_outputs1_loss: 0.0629
Epoch 33/100
92/92 [==============================] - ETA: 0s - loss: 0.1022 - n_outputs0_loss: 0.0545 - n_outputs1_loss: 0.0477
Epoch 00033: val_loss did not improve from 0.18343
92/92 [==============================] - 10s 110ms/step - loss: 0.1022 - n_outputs0_loss: 0.0545 - n_outputs1_loss: 0.0477 - val_loss: 0.1843 - val_n_outputs0_loss: 0.1191 - val_n_outputs1_loss: 0.0652
Epoch 34/100
92/92 [==============================] - ETA: 0s - loss: 0.0995 - n_outputs0_loss: 0.0529 - n_outputs1_loss: 0.0466
Epoch 00034: val_loss improved from 0.18343 to 0.18117, saving model to ./models/msp-car-2.h5
92/92 [==============================] - 10s 110ms/step - loss: 0.0995 - n_outputs0_loss: 0.0529 - n_outputs1_loss: 0.0466 - val_loss: 0.1812 - val_n_outputs0_loss: 0.1166 - val_n_outputs1_loss: 0.0646
Epoch 35/100
92/92 [==============================] - ETA: 0s - loss: 0.0989 - n_outputs0_loss: 0.0526 - n_outputs1_loss: 0.0463
Epoch 00035: val_loss did not improve from 0.18117
92/92 [==============================] - 10s 110ms/step - loss: 0.0989 - n_outputs0_loss: 0.0526 - n_outputs1_loss: 0.0463 - val_loss: 0.1835 - val_n_outputs0_loss: 0.1177 - val_n_outputs1_loss: 0.0657
Epoch 36/100
92/92 [==============================] - ETA: 0s - loss: 0.0972 - n_outputs0_loss: 0.0514 - n_outputs1_loss: 0.0458
Epoch 00036: val_loss did not improve from 0.18117
92/92 [==============================] - 10s 111ms/step - loss: 0.0972 - n_outputs0_loss: 0.0514 - n_outputs1_loss: 0.0458 - val_loss: 0.1838 - val_n_outputs0_loss: 0.1198 - val_n_outputs1_loss: 0.0641
Epoch 37/100
92/92 [==============================] - ETA: 0s - loss: 0.0959 - n_outputs0_loss: 0.0509 - n_outputs1_loss: 0.0450
Epoch 00037: val_loss did not improve from 0.18117
92/92 [==============================] - 10s 109ms/step - loss: 0.0959 - n_outputs0_loss: 0.0509 - n_outputs1_loss: 0.0450 - val_loss: 0.1830 - val_n_outputs0_loss: 0.1191 - val_n_outputs1_loss: 0.0639
Epoch 38/100
92/92 [==============================] - ETA: 0s - loss: 0.0934 - n_outputs0_loss: 0.0496 - n_outputs1_loss: 0.0438
Epoch 00038: val_loss did not improve from 0.18117
92/92 [==============================] - 10s 110ms/step - loss: 0.0934 - n_outputs0_loss: 0.0496 - n_outputs1_loss: 0.0438 - val_loss: 0.1845 - val_n_outputs0_loss: 0.1185 - val_n_outputs1_loss: 0.0660
Epoch 39/100
92/92 [==============================] - ETA: 0s - loss: 0.0923 - n_outputs0_loss: 0.0477 - n_outputs1_loss: 0.0446
Epoch 00039: val_loss did not improve from 0.18117
92/92 [==============================] - 10s 110ms/step - loss: 0.0923 - n_outputs0_loss: 0.0477 - n_outputs1_loss: 0.0446 - val_loss: 0.1818 - val_n_outputs0_loss: 0.1186 - val_n_outputs1_loss: 0.0632
WARNING: CPU random generator seem to be failing, disable hardware random number generation
WARNING: RDRND generated: 0xffffffff 0xffffffff 0xffffffff 0xffffffff
(donkey) arl@arl1:~/mycar$
```
## Checking the models

```sh
ls -l models/*
```

returns

```
ls -l models/*
-rw-r--r-- 1 arl arl    32317 Jul 26 20:30 models/database.json
-rw-r--r-- 1 arl arl 35773936 Jul 26 20:17 models/msp-car-1-gpu.h5
-rw-r--r-- 1 arl arl    27506 Jul 26 20:17 models/msp-car-1-gpu.png
-rw-r--r-- 1 arl arl    23659 Jul 26 19:57 models/msp-car-1.png
-rw-r--r-- 1 arl arl 35773936 Jul 26 20:29 models/msp-car-2.h5
-rw-r--r-- 1 arl arl    25670 Jul 26 20:30 models/msp-car-2.png
-rw-r--r-- 1 arl arl    22616 Feb  2  2020 models/mypilot.h5_loss_acc_0.040245.png
-rw-r--r-- 1 arl arl    26687 Feb  2  2020 models/mypilot.h5_loss_acc_0.042222.png
-rw-r--r-- 1 arl arl 11939744 Feb  2  2020 models/ref-model.h5
```