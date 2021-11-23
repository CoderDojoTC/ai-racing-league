# Dans Basement Training Log

I have a very small track in my basement.  I put down a single white line about 3/4 inch wide using white electrical tape.  The background was a marble blue expoy floor with a lot of color variation.  The surface was very reflective and there were lights in the ceiling with lots of glare.  I drove the car around 10 times in each direction and collected around 4,500 images.

## Catalogs

I manually edited the catlog files and then edited the manifest.json file to modify the paths:

```
{"paths": ["catalog_3.catalog", "catalog_4.catalog", "catalog_5.catalog", "catalog_6.catalog", "catalog_7.catalog"]
```

```sh
wc -l data/dans-basement/*.catalog
```

```
   781 data/dans-basement/catalog_3.catalog
  1000 data/dans-basement/catalog_4.catalog
  1000 data/dans-basement/catalog_5.catalog
  1000 data/dans-basement/catalog_6.catalog
   750 data/dans-basement/catalog_7.catalog
  4531 total
```

This matched the ```ls -1 ~/mycar/data/dans-basement/images | wc -l``` command that counted the number of images.

I time the training time on the NIVID RTX 2080 and got the model trained in about 1.5 minutes.
```
$ time donkey train --tub=./data/dans-basement --model=./models/dans-basement.h5
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
2021-07-26 21:05:34.259364: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2021-07-26 21:05:34.278301: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.278898: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 21:05:34.279098: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:05:34.280320: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:05:34.281822: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 21:05:34.282037: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 21:05:34.283140: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 21:05:34.283726: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 21:05:34.285524: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:05:34.285676: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.286176: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.286568: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 21:05:34.286793: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2021-07-26 21:05:34.290920: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3592950000 Hz
2021-07-26 21:05:34.291228: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x557d8a05bbb0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-07-26 21:05:34.291241: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-07-26 21:05:34.291374: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.291795: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 21:05:34.291830: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:05:34.291842: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:05:34.291852: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 21:05:34.291862: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 21:05:34.291872: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 21:05:34.291881: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 21:05:34.291891: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:05:34.291955: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.292398: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.292782: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 21:05:34.292805: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:05:34.366898: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-07-26 21:05:34.366930: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2021-07-26 21:05:34.366937: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2021-07-26 21:05:34.367194: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.367855: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.368446: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:05:34.368971: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 9911 MB memory) -> physical GPU (device: 0, name: NVIDIA GeForce RTX 2080 Ti, pci bus id: 0000:09:00.0, compute capability: 7.5)
2021-07-26 21:05:34.370680: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x557d8bec8fa0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2021-07-26 21:05:34.370693: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): NVIDIA GeForce RTX 2080 Ti, Compute Capability 7.5
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
Using catalog /home/arl/mycar/data/dans-basement/catalog_7.catalog

Records # Training 3364
Records # Validation 842
Epoch 1/100
2021-07-26 21:05:35.291438: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:05:35.613762: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:05:36.322576: W tensorflow/stream_executor/gpu/asm_compiler.cc:116] *** WARNING *** You are using ptxas 9.1.108, which is older than 9.2.88. ptxas 9.x before 9.2.88 is known to miscompile XLA code, leading to incorrect results or invalid-address errors.

You do not need to update to CUDA 9.2.88; cherry-picking the ptxas binary is sufficient.
2021-07-26 21:05:36.376195: W tensorflow/stream_executor/gpu/redzone_allocator.cc:314] Internal: ptxas exited with non-zero error code 65280, output: ptxas fatal   : Value 'sm_75' is not defined for option 'gpu-name'

Relying on driver to perform ptx compilation. 
Modify $PATH to customize ptxas location.
This message will be only logged once.
27/27 [==============================] - ETA: 0s - loss: 0.2495 - n_outputs0_loss: 0.1717 - n_outputs1_loss: 0.0778
Epoch 00001: val_loss improved from inf to 0.14744, saving model to ./models/dans-basement.h5
27/27 [==============================] - 8s 301ms/step - loss: 0.2495 - n_outputs0_loss: 0.1717 - n_outputs1_loss: 0.0778 - val_loss: 0.1474 - val_n_outputs0_loss: 0.1291 - val_n_outputs1_loss: 0.0183
Epoch 2/100
27/27 [==============================] - ETA: 0s - loss: 0.1487 - n_outputs0_loss: 0.1265 - n_outputs1_loss: 0.0223
Epoch 00002: val_loss improved from 0.14744 to 0.09815, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 120ms/step - loss: 0.1487 - n_outputs0_loss: 0.1265 - n_outputs1_loss: 0.0223 - val_loss: 0.0981 - val_n_outputs0_loss: 0.0777 - val_n_outputs1_loss: 0.0205
Epoch 3/100
27/27 [==============================] - ETA: 0s - loss: 0.1075 - n_outputs0_loss: 0.0893 - n_outputs1_loss: 0.0182
Epoch 00003: val_loss improved from 0.09815 to 0.07897, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 117ms/step - loss: 0.1075 - n_outputs0_loss: 0.0893 - n_outputs1_loss: 0.0182 - val_loss: 0.0790 - val_n_outputs0_loss: 0.0687 - val_n_outputs1_loss: 0.0102
Epoch 4/100
27/27 [==============================] - ETA: 0s - loss: 0.0917 - n_outputs0_loss: 0.0759 - n_outputs1_loss: 0.0158
Epoch 00004: val_loss improved from 0.07897 to 0.07055, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0917 - n_outputs0_loss: 0.0759 - n_outputs1_loss: 0.0158 - val_loss: 0.0705 - val_n_outputs0_loss: 0.0610 - val_n_outputs1_loss: 0.0096
Epoch 5/100
27/27 [==============================] - ETA: 0s - loss: 0.0880 - n_outputs0_loss: 0.0734 - n_outputs1_loss: 0.0146
Epoch 00005: val_loss did not improve from 0.07055
27/27 [==============================] - 3s 105ms/step - loss: 0.0880 - n_outputs0_loss: 0.0734 - n_outputs1_loss: 0.0146 - val_loss: 0.0751 - val_n_outputs0_loss: 0.0553 - val_n_outputs1_loss: 0.0198
Epoch 6/100
27/27 [==============================] - ETA: 0s - loss: 0.0757 - n_outputs0_loss: 0.0629 - n_outputs1_loss: 0.0127
Epoch 00006: val_loss improved from 0.07055 to 0.05840, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 111ms/step - loss: 0.0757 - n_outputs0_loss: 0.0629 - n_outputs1_loss: 0.0127 - val_loss: 0.0584 - val_n_outputs0_loss: 0.0485 - val_n_outputs1_loss: 0.0099
Epoch 7/100
27/27 [==============================] - ETA: 0s - loss: 0.0672 - n_outputs0_loss: 0.0551 - n_outputs1_loss: 0.0120
Epoch 00007: val_loss improved from 0.05840 to 0.05028, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0672 - n_outputs0_loss: 0.0551 - n_outputs1_loss: 0.0120 - val_loss: 0.0503 - val_n_outputs0_loss: 0.0450 - val_n_outputs1_loss: 0.0053
Epoch 8/100
27/27 [==============================] - ETA: 0s - loss: 0.0621 - n_outputs0_loss: 0.0510 - n_outputs1_loss: 0.0111
Epoch 00008: val_loss improved from 0.05028 to 0.04540, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0621 - n_outputs0_loss: 0.0510 - n_outputs1_loss: 0.0111 - val_loss: 0.0454 - val_n_outputs0_loss: 0.0385 - val_n_outputs1_loss: 0.0069
Epoch 9/100
27/27 [==============================] - ETA: 0s - loss: 0.0545 - n_outputs0_loss: 0.0441 - n_outputs1_loss: 0.0104
Epoch 00009: val_loss improved from 0.04540 to 0.04351, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 107ms/step - loss: 0.0545 - n_outputs0_loss: 0.0441 - n_outputs1_loss: 0.0104 - val_loss: 0.0435 - val_n_outputs0_loss: 0.0358 - val_n_outputs1_loss: 0.0077
Epoch 10/100
27/27 [==============================] - ETA: 0s - loss: 0.0558 - n_outputs0_loss: 0.0458 - n_outputs1_loss: 0.0099
Epoch 00010: val_loss improved from 0.04351 to 0.04070, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0558 - n_outputs0_loss: 0.0458 - n_outputs1_loss: 0.0099 - val_loss: 0.0407 - val_n_outputs0_loss: 0.0357 - val_n_outputs1_loss: 0.0050
Epoch 11/100
27/27 [==============================] - ETA: 0s - loss: 0.0505 - n_outputs0_loss: 0.0415 - n_outputs1_loss: 0.0090
Epoch 00011: val_loss improved from 0.04070 to 0.03935, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 109ms/step - loss: 0.0505 - n_outputs0_loss: 0.0415 - n_outputs1_loss: 0.0090 - val_loss: 0.0393 - val_n_outputs0_loss: 0.0340 - val_n_outputs1_loss: 0.0054
Epoch 12/100
27/27 [==============================] - ETA: 0s - loss: 0.0476 - n_outputs0_loss: 0.0388 - n_outputs1_loss: 0.0088
Epoch 00012: val_loss improved from 0.03935 to 0.03624, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0476 - n_outputs0_loss: 0.0388 - n_outputs1_loss: 0.0088 - val_loss: 0.0362 - val_n_outputs0_loss: 0.0298 - val_n_outputs1_loss: 0.0065
Epoch 13/100
27/27 [==============================] - ETA: 0s - loss: 0.0453 - n_outputs0_loss: 0.0373 - n_outputs1_loss: 0.0080
Epoch 00013: val_loss improved from 0.03624 to 0.03507, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 108ms/step - loss: 0.0453 - n_outputs0_loss: 0.0373 - n_outputs1_loss: 0.0080 - val_loss: 0.0351 - val_n_outputs0_loss: 0.0294 - val_n_outputs1_loss: 0.0057
Epoch 14/100
27/27 [==============================] - ETA: 0s - loss: 0.0430 - n_outputs0_loss: 0.0352 - n_outputs1_loss: 0.0079
Epoch 00014: val_loss improved from 0.03507 to 0.03211, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 111ms/step - loss: 0.0430 - n_outputs0_loss: 0.0352 - n_outputs1_loss: 0.0079 - val_loss: 0.0321 - val_n_outputs0_loss: 0.0265 - val_n_outputs1_loss: 0.0056
Epoch 15/100
27/27 [==============================] - ETA: 0s - loss: 0.0397 - n_outputs0_loss: 0.0327 - n_outputs1_loss: 0.0070
Epoch 00015: val_loss improved from 0.03211 to 0.03208, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 110ms/step - loss: 0.0397 - n_outputs0_loss: 0.0327 - n_outputs1_loss: 0.0070 - val_loss: 0.0321 - val_n_outputs0_loss: 0.0279 - val_n_outputs1_loss: 0.0042
Epoch 16/100
27/27 [==============================] - ETA: 0s - loss: 0.0382 - n_outputs0_loss: 0.0316 - n_outputs1_loss: 0.0065
Epoch 00016: val_loss improved from 0.03208 to 0.02880, saving model to ./models/dans-basement.h5
27/27 [==============================] - 3s 108ms/step - loss: 0.0382 - n_outputs0_loss: 0.0316 - n_outputs1_loss: 0.0065 - val_loss: 0.0288 - val_n_outputs0_loss: 0.0243 - val_n_outputs1_loss: 0.0046
Epoch 17/100
27/27 [==============================] - ETA: 0s - loss: 0.0381 - n_outputs0_loss: 0.0313 - n_outputs1_loss: 0.0069
Epoch 00017: val_loss did not improve from 0.02880
27/27 [==============================] - 3s 104ms/step - loss: 0.0381 - n_outputs0_loss: 0.0313 - n_outputs1_loss: 0.0069 - val_loss: 0.0322 - val_n_outputs0_loss: 0.0281 - val_n_outputs1_loss: 0.0041
Epoch 18/100
27/27 [==============================] - ETA: 0s - loss: 0.0375 - n_outputs0_loss: 0.0310 - n_outputs1_loss: 0.0065
Epoch 00018: val_loss did not improve from 0.02880
27/27 [==============================] - 3s 107ms/step - loss: 0.0375 - n_outputs0_loss: 0.0310 - n_outputs1_loss: 0.0065 - val_loss: 0.0293 - val_n_outputs0_loss: 0.0257 - val_n_outputs1_loss: 0.0036
Epoch 19/100
27/27 [==============================] - ETA: 0s - loss: 0.0372 - n_outputs0_loss: 0.0308 - n_outputs1_loss: 0.0064
Epoch 00019: val_loss did not improve from 0.02880
27/27 [==============================] - 3s 108ms/step - loss: 0.0372 - n_outputs0_loss: 0.0308 - n_outputs1_loss: 0.0064 - val_loss: 0.0307 - val_n_outputs0_loss: 0.0275 - val_n_outputs1_loss: 0.0032
Epoch 20/100
27/27 [==============================] - ETA: 0s - loss: 0.0347 - n_outputs0_loss: 0.0285 - n_outputs1_loss: 0.0062
Epoch 00020: val_loss did not improve from 0.02880
27/27 [==============================] - 3s 104ms/step - loss: 0.0347 - n_outputs0_loss: 0.0285 - n_outputs1_loss: 0.0062 - val_loss: 0.0325 - val_n_outputs0_loss: 0.0283 - val_n_outputs1_loss: 0.0042
Epoch 21/100
27/27 [==============================] - ETA: 0s - loss: 0.0349 - n_outputs0_loss: 0.0290 - n_outputs1_loss: 0.0058
Epoch 00021: val_loss did not improve from 0.02880
27/27 [==============================] - 3s 107ms/step - loss: 0.0349 - n_outputs0_loss: 0.0290 - n_outputs1_loss: 0.0058 - val_loss: 0.0293 - val_n_outputs0_loss: 0.0258 - val_n_outputs1_loss: 0.0035
WARNING: CPU random generator seem to be failing, disable hardware random number generation
WARNING: RDRND generated: 0xffffffff 0xffffffff 0xffffffff 0xffffffff

real	1m26.930s
user	1m30.911s
sys	0m42.818s
```