# Minnesota STEM Partners Car 1 Training Log

```
time donkey train --tub=./data/msp-car-1 --model=./models/msp-car-1.h5
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
2021-07-26 21:18:57.390998: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2021-07-26 21:18:57.409838: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.410285: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 21:18:57.410424: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:18:57.411314: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:18:57.412358: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 21:18:57.412506: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 21:18:57.413323: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 21:18:57.413712: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 21:18:57.415437: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:18:57.415619: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.416133: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.416523: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 21:18:57.416750: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2021-07-26 21:18:57.420820: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3592950000 Hz
2021-07-26 21:18:57.421125: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5629cbee7970 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-07-26 21:18:57.421136: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-07-26 21:18:57.421270: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.421679: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties: 
pciBusID: 0000:09:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.635GHz coreCount: 68 deviceMemorySize: 10.76GiB deviceMemoryBandwidth: 573.69GiB/s
2021-07-26 21:18:57.421712: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:18:57.421724: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:18:57.421735: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2021-07-26 21:18:57.421746: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2021-07-26 21:18:57.421756: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2021-07-26 21:18:57.421766: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2021-07-26 21:18:57.421776: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:18:57.421840: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.422285: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.422675: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-07-26 21:18:57.422700: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2021-07-26 21:18:57.504507: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-07-26 21:18:57.504534: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2021-07-26 21:18:57.504541: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2021-07-26 21:18:57.504754: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.505207: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.505632: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-07-26 21:18:57.506019: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 9892 MB memory) -> physical GPU (device: 0, name: NVIDIA GeForce RTX 2080 Ti, pci bus id: 0000:09:00.0, compute capability: 7.5)
2021-07-26 21:18:57.507379: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5629cdd66f30 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2021-07-26 21:18:57.507389: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): NVIDIA GeForce RTX 2080 Ti, Compute Capability 7.5
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
Using catalog /home/arl/mycar/data/msp-car-1/catalog_17.catalog

Records # Training 1265
Records # Validation 317
Epoch 1/100
2021-07-26 21:18:58.397797: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2021-07-26 21:18:58.705078: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2021-07-26 21:18:59.429125: W tensorflow/stream_executor/gpu/asm_compiler.cc:116] *** WARNING *** You are using ptxas 9.1.108, which is older than 9.2.88. ptxas 9.x before 9.2.88 is known to miscompile XLA code, leading to incorrect results or invalid-address errors.

You do not need to update to CUDA 9.2.88; cherry-picking the ptxas binary is sufficient.
2021-07-26 21:18:59.481809: W tensorflow/stream_executor/gpu/redzone_allocator.cc:314] Internal: ptxas exited with non-zero error code 65280, output: ptxas fatal   : Value 'sm_75' is not defined for option 'gpu-name'

Relying on driver to perform ptx compilation. 
Modify $PATH to customize ptxas location.
This message will be only logged once.
10/10 [==============================] - ETA: 0s - loss: 0.6674 - n_outputs0_loss: 0.5162 - n_outputs1_loss: 0.1512
Epoch 00001: val_loss improved from inf to 0.60297, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 3s 288ms/step - loss: 0.6674 - n_outputs0_loss: 0.5162 - n_outputs1_loss: 0.1512 - val_loss: 0.6030 - val_n_outputs0_loss: 0.4514 - val_n_outputs1_loss: 0.1516
Epoch 2/100
10/10 [==============================] - ETA: 0s - loss: 0.6050 - n_outputs0_loss: 0.5074 - n_outputs1_loss: 0.0976
Epoch 00002: val_loss improved from 0.60297 to 0.51595, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 124ms/step - loss: 0.6050 - n_outputs0_loss: 0.5074 - n_outputs1_loss: 0.0976 - val_loss: 0.5160 - val_n_outputs0_loss: 0.4188 - val_n_outputs1_loss: 0.0972
Epoch 3/100
10/10 [==============================] - ETA: 0s - loss: 0.5707 - n_outputs0_loss: 0.4923 - n_outputs1_loss: 0.0784
Epoch 00003: val_loss improved from 0.51595 to 0.50280, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 110ms/step - loss: 0.5707 - n_outputs0_loss: 0.4923 - n_outputs1_loss: 0.0784 - val_loss: 0.5028 - val_n_outputs0_loss: 0.4224 - val_n_outputs1_loss: 0.0804
Epoch 4/100
10/10 [==============================] - ETA: 0s - loss: 0.5615 - n_outputs0_loss: 0.4917 - n_outputs1_loss: 0.0698
Epoch 00004: val_loss improved from 0.50280 to 0.49159, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 110ms/step - loss: 0.5615 - n_outputs0_loss: 0.4917 - n_outputs1_loss: 0.0698 - val_loss: 0.4916 - val_n_outputs0_loss: 0.4203 - val_n_outputs1_loss: 0.0713
Epoch 5/100
10/10 [==============================] - ETA: 0s - loss: 0.5541 - n_outputs0_loss: 0.4854 - n_outputs1_loss: 0.0687
Epoch 00005: val_loss improved from 0.49159 to 0.48784, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 104ms/step - loss: 0.5541 - n_outputs0_loss: 0.4854 - n_outputs1_loss: 0.0687 - val_loss: 0.4878 - val_n_outputs0_loss: 0.4107 - val_n_outputs1_loss: 0.0772
Epoch 6/100
10/10 [==============================] - ETA: 0s - loss: 0.5527 - n_outputs0_loss: 0.4827 - n_outputs1_loss: 0.0701
Epoch 00006: val_loss improved from 0.48784 to 0.48521, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.5527 - n_outputs0_loss: 0.4827 - n_outputs1_loss: 0.0701 - val_loss: 0.4852 - val_n_outputs0_loss: 0.4127 - val_n_outputs1_loss: 0.0725
Epoch 7/100
10/10 [==============================] - ETA: 0s - loss: 0.5405 - n_outputs0_loss: 0.4764 - n_outputs1_loss: 0.0641
Epoch 00007: val_loss improved from 0.48521 to 0.48270, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 110ms/step - loss: 0.5405 - n_outputs0_loss: 0.4764 - n_outputs1_loss: 0.0641 - val_loss: 0.4827 - val_n_outputs0_loss: 0.4097 - val_n_outputs1_loss: 0.0730
Epoch 8/100
10/10 [==============================] - ETA: 0s - loss: 0.5383 - n_outputs0_loss: 0.4724 - n_outputs1_loss: 0.0659
Epoch 00008: val_loss improved from 0.48270 to 0.47415, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.5383 - n_outputs0_loss: 0.4724 - n_outputs1_loss: 0.0659 - val_loss: 0.4741 - val_n_outputs0_loss: 0.4026 - val_n_outputs1_loss: 0.0715
Epoch 9/100
10/10 [==============================] - ETA: 0s - loss: 0.5288 - n_outputs0_loss: 0.4640 - n_outputs1_loss: 0.0648
Epoch 00009: val_loss did not improve from 0.47415
10/10 [==============================] - 1s 101ms/step - loss: 0.5288 - n_outputs0_loss: 0.4640 - n_outputs1_loss: 0.0648 - val_loss: 0.4780 - val_n_outputs0_loss: 0.4069 - val_n_outputs1_loss: 0.0711
Epoch 10/100
10/10 [==============================] - ETA: 0s - loss: 0.5344 - n_outputs0_loss: 0.4677 - n_outputs1_loss: 0.0667
Epoch 00010: val_loss improved from 0.47415 to 0.45939, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 111ms/step - loss: 0.5344 - n_outputs0_loss: 0.4677 - n_outputs1_loss: 0.0667 - val_loss: 0.4594 - val_n_outputs0_loss: 0.3903 - val_n_outputs1_loss: 0.0691
Epoch 11/100
10/10 [==============================] - ETA: 0s - loss: 0.5014 - n_outputs0_loss: 0.4349 - n_outputs1_loss: 0.0666
Epoch 00011: val_loss improved from 0.45939 to 0.44304, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 112ms/step - loss: 0.5014 - n_outputs0_loss: 0.4349 - n_outputs1_loss: 0.0666 - val_loss: 0.4430 - val_n_outputs0_loss: 0.3672 - val_n_outputs1_loss: 0.0758
Epoch 12/100
10/10 [==============================] - ETA: 0s - loss: 0.4585 - n_outputs0_loss: 0.3847 - n_outputs1_loss: 0.0738
Epoch 00012: val_loss improved from 0.44304 to 0.36563, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.4585 - n_outputs0_loss: 0.3847 - n_outputs1_loss: 0.0738 - val_loss: 0.3656 - val_n_outputs0_loss: 0.2934 - val_n_outputs1_loss: 0.0723
Epoch 13/100
10/10 [==============================] - ETA: 0s - loss: 0.3922 - n_outputs0_loss: 0.3257 - n_outputs1_loss: 0.0664
Epoch 00013: val_loss improved from 0.36563 to 0.30773, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 111ms/step - loss: 0.3922 - n_outputs0_loss: 0.3257 - n_outputs1_loss: 0.0664 - val_loss: 0.3077 - val_n_outputs0_loss: 0.2463 - val_n_outputs1_loss: 0.0614
Epoch 14/100
10/10 [==============================] - ETA: 0s - loss: 0.3662 - n_outputs0_loss: 0.3052 - n_outputs1_loss: 0.0610
Epoch 00014: val_loss improved from 0.30773 to 0.27574, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 107ms/step - loss: 0.3662 - n_outputs0_loss: 0.3052 - n_outputs1_loss: 0.0610 - val_loss: 0.2757 - val_n_outputs0_loss: 0.2294 - val_n_outputs1_loss: 0.0463
Epoch 15/100
10/10 [==============================] - ETA: 0s - loss: 0.3233 - n_outputs0_loss: 0.2626 - n_outputs1_loss: 0.0607
Epoch 00015: val_loss improved from 0.27574 to 0.24205, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 110ms/step - loss: 0.3233 - n_outputs0_loss: 0.2626 - n_outputs1_loss: 0.0607 - val_loss: 0.2421 - val_n_outputs0_loss: 0.1966 - val_n_outputs1_loss: 0.0454
Epoch 16/100
10/10 [==============================] - ETA: 0s - loss: 0.3078 - n_outputs0_loss: 0.2500 - n_outputs1_loss: 0.0577
Epoch 00016: val_loss did not improve from 0.24205
10/10 [==============================] - 1s 100ms/step - loss: 0.3078 - n_outputs0_loss: 0.2500 - n_outputs1_loss: 0.0577 - val_loss: 0.2473 - val_n_outputs0_loss: 0.2023 - val_n_outputs1_loss: 0.0450
Epoch 17/100
10/10 [==============================] - ETA: 0s - loss: 0.2959 - n_outputs0_loss: 0.2404 - n_outputs1_loss: 0.0555
Epoch 00017: val_loss improved from 0.24205 to 0.22809, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 113ms/step - loss: 0.2959 - n_outputs0_loss: 0.2404 - n_outputs1_loss: 0.0555 - val_loss: 0.2281 - val_n_outputs0_loss: 0.1842 - val_n_outputs1_loss: 0.0438
Epoch 18/100
10/10 [==============================] - ETA: 0s - loss: 0.2820 - n_outputs0_loss: 0.2280 - n_outputs1_loss: 0.0540
Epoch 00018: val_loss improved from 0.22809 to 0.21671, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 107ms/step - loss: 0.2820 - n_outputs0_loss: 0.2280 - n_outputs1_loss: 0.0540 - val_loss: 0.2167 - val_n_outputs0_loss: 0.1768 - val_n_outputs1_loss: 0.0400
Epoch 19/100
10/10 [==============================] - ETA: 0s - loss: 0.2568 - n_outputs0_loss: 0.2044 - n_outputs1_loss: 0.0524
Epoch 00019: val_loss did not improve from 0.21671
10/10 [==============================] - 1s 99ms/step - loss: 0.2568 - n_outputs0_loss: 0.2044 - n_outputs1_loss: 0.0524 - val_loss: 0.2190 - val_n_outputs0_loss: 0.1788 - val_n_outputs1_loss: 0.0402
Epoch 20/100
10/10 [==============================] - ETA: 0s - loss: 0.2621 - n_outputs0_loss: 0.2123 - n_outputs1_loss: 0.0499
Epoch 00020: val_loss improved from 0.21671 to 0.21046, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 113ms/step - loss: 0.2621 - n_outputs0_loss: 0.2123 - n_outputs1_loss: 0.0499 - val_loss: 0.2105 - val_n_outputs0_loss: 0.1718 - val_n_outputs1_loss: 0.0386
Epoch 21/100
10/10 [==============================] - ETA: 0s - loss: 0.2521 - n_outputs0_loss: 0.2052 - n_outputs1_loss: 0.0469
Epoch 00021: val_loss improved from 0.21046 to 0.20605, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 111ms/step - loss: 0.2521 - n_outputs0_loss: 0.2052 - n_outputs1_loss: 0.0469 - val_loss: 0.2060 - val_n_outputs0_loss: 0.1675 - val_n_outputs1_loss: 0.0385
Epoch 22/100
10/10 [==============================] - ETA: 0s - loss: 0.2261 - n_outputs0_loss: 0.1781 - n_outputs1_loss: 0.0480
Epoch 00022: val_loss improved from 0.20605 to 0.20553, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 106ms/step - loss: 0.2261 - n_outputs0_loss: 0.1781 - n_outputs1_loss: 0.0480 - val_loss: 0.2055 - val_n_outputs0_loss: 0.1711 - val_n_outputs1_loss: 0.0344
Epoch 23/100
10/10 [==============================] - ETA: 0s - loss: 0.2222 - n_outputs0_loss: 0.1794 - n_outputs1_loss: 0.0429
Epoch 00023: val_loss improved from 0.20553 to 0.20273, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.2222 - n_outputs0_loss: 0.1794 - n_outputs1_loss: 0.0429 - val_loss: 0.2027 - val_n_outputs0_loss: 0.1697 - val_n_outputs1_loss: 0.0331
Epoch 24/100
10/10 [==============================] - ETA: 0s - loss: 0.2126 - n_outputs0_loss: 0.1698 - n_outputs1_loss: 0.0428
Epoch 00024: val_loss improved from 0.20273 to 0.19049, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 105ms/step - loss: 0.2126 - n_outputs0_loss: 0.1698 - n_outputs1_loss: 0.0428 - val_loss: 0.1905 - val_n_outputs0_loss: 0.1562 - val_n_outputs1_loss: 0.0343
Epoch 25/100
10/10 [==============================] - ETA: 0s - loss: 0.2062 - n_outputs0_loss: 0.1658 - n_outputs1_loss: 0.0404
Epoch 00025: val_loss improved from 0.19049 to 0.18404, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.2062 - n_outputs0_loss: 0.1658 - n_outputs1_loss: 0.0404 - val_loss: 0.1840 - val_n_outputs0_loss: 0.1488 - val_n_outputs1_loss: 0.0352
Epoch 26/100
10/10 [==============================] - ETA: 0s - loss: 0.1928 - n_outputs0_loss: 0.1555 - n_outputs1_loss: 0.0372
Epoch 00026: val_loss did not improve from 0.18404
10/10 [==============================] - 1s 102ms/step - loss: 0.1928 - n_outputs0_loss: 0.1555 - n_outputs1_loss: 0.0372 - val_loss: 0.1907 - val_n_outputs0_loss: 0.1563 - val_n_outputs1_loss: 0.0344
Epoch 27/100
10/10 [==============================] - ETA: 0s - loss: 0.1834 - n_outputs0_loss: 0.1428 - n_outputs1_loss: 0.0406
Epoch 00027: val_loss did not improve from 0.18404
10/10 [==============================] - 1s 103ms/step - loss: 0.1834 - n_outputs0_loss: 0.1428 - n_outputs1_loss: 0.0406 - val_loss: 0.1922 - val_n_outputs0_loss: 0.1527 - val_n_outputs1_loss: 0.0396
Epoch 28/100
10/10 [==============================] - ETA: 0s - loss: 0.1668 - n_outputs0_loss: 0.1282 - n_outputs1_loss: 0.0386
Epoch 00028: val_loss improved from 0.18404 to 0.17462, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 113ms/step - loss: 0.1668 - n_outputs0_loss: 0.1282 - n_outputs1_loss: 0.0386 - val_loss: 0.1746 - val_n_outputs0_loss: 0.1436 - val_n_outputs1_loss: 0.0311
Epoch 29/100
10/10 [==============================] - ETA: 0s - loss: 0.1654 - n_outputs0_loss: 0.1282 - n_outputs1_loss: 0.0372
Epoch 00029: val_loss improved from 0.17462 to 0.17365, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 107ms/step - loss: 0.1654 - n_outputs0_loss: 0.1282 - n_outputs1_loss: 0.0372 - val_loss: 0.1736 - val_n_outputs0_loss: 0.1432 - val_n_outputs1_loss: 0.0305
Epoch 30/100
10/10 [==============================] - ETA: 0s - loss: 0.1615 - n_outputs0_loss: 0.1250 - n_outputs1_loss: 0.0364
Epoch 00030: val_loss did not improve from 0.17365
10/10 [==============================] - 1s 96ms/step - loss: 0.1615 - n_outputs0_loss: 0.1250 - n_outputs1_loss: 0.0364 - val_loss: 0.1799 - val_n_outputs0_loss: 0.1493 - val_n_outputs1_loss: 0.0306
Epoch 31/100
10/10 [==============================] - ETA: 0s - loss: 0.1495 - n_outputs0_loss: 0.1162 - n_outputs1_loss: 0.0332
Epoch 00031: val_loss improved from 0.17365 to 0.17255, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 112ms/step - loss: 0.1495 - n_outputs0_loss: 0.1162 - n_outputs1_loss: 0.0332 - val_loss: 0.1726 - val_n_outputs0_loss: 0.1383 - val_n_outputs1_loss: 0.0342
Epoch 32/100
10/10 [==============================] - ETA: 0s - loss: 0.1453 - n_outputs0_loss: 0.1121 - n_outputs1_loss: 0.0333
Epoch 00032: val_loss did not improve from 0.17255
10/10 [==============================] - 1s 104ms/step - loss: 0.1453 - n_outputs0_loss: 0.1121 - n_outputs1_loss: 0.0333 - val_loss: 0.1764 - val_n_outputs0_loss: 0.1456 - val_n_outputs1_loss: 0.0308
Epoch 33/100
10/10 [==============================] - ETA: 0s - loss: 0.1346 - n_outputs0_loss: 0.1043 - n_outputs1_loss: 0.0303
Epoch 00033: val_loss improved from 0.17255 to 0.17092, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 115ms/step - loss: 0.1346 - n_outputs0_loss: 0.1043 - n_outputs1_loss: 0.0303 - val_loss: 0.1709 - val_n_outputs0_loss: 0.1395 - val_n_outputs1_loss: 0.0315
Epoch 34/100
10/10 [==============================] - ETA: 0s - loss: 0.1293 - n_outputs0_loss: 0.0991 - n_outputs1_loss: 0.0302
Epoch 00034: val_loss improved from 0.17092 to 0.16704, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 109ms/step - loss: 0.1293 - n_outputs0_loss: 0.0991 - n_outputs1_loss: 0.0302 - val_loss: 0.1670 - val_n_outputs0_loss: 0.1342 - val_n_outputs1_loss: 0.0329
Epoch 35/100
10/10 [==============================] - ETA: 0s - loss: 0.1196 - n_outputs0_loss: 0.0890 - n_outputs1_loss: 0.0306
Epoch 00035: val_loss improved from 0.16704 to 0.15917, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 110ms/step - loss: 0.1196 - n_outputs0_loss: 0.0890 - n_outputs1_loss: 0.0306 - val_loss: 0.1592 - val_n_outputs0_loss: 0.1280 - val_n_outputs1_loss: 0.0311
Epoch 36/100
10/10 [==============================] - ETA: 0s - loss: 0.1086 - n_outputs0_loss: 0.0805 - n_outputs1_loss: 0.0281
Epoch 00036: val_loss improved from 0.15917 to 0.15774, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 114ms/step - loss: 0.1086 - n_outputs0_loss: 0.0805 - n_outputs1_loss: 0.0281 - val_loss: 0.1577 - val_n_outputs0_loss: 0.1264 - val_n_outputs1_loss: 0.0313
Epoch 37/100
10/10 [==============================] - ETA: 0s - loss: 0.1032 - n_outputs0_loss: 0.0753 - n_outputs1_loss: 0.0279
Epoch 00037: val_loss did not improve from 0.15774
10/10 [==============================] - 1s 99ms/step - loss: 0.1032 - n_outputs0_loss: 0.0753 - n_outputs1_loss: 0.0279 - val_loss: 0.1598 - val_n_outputs0_loss: 0.1281 - val_n_outputs1_loss: 0.0317
Epoch 38/100
10/10 [==============================] - ETA: 0s - loss: 0.1050 - n_outputs0_loss: 0.0783 - n_outputs1_loss: 0.0266
Epoch 00038: val_loss did not improve from 0.15774
10/10 [==============================] - 1s 105ms/step - loss: 0.1050 - n_outputs0_loss: 0.0783 - n_outputs1_loss: 0.0266 - val_loss: 0.1586 - val_n_outputs0_loss: 0.1269 - val_n_outputs1_loss: 0.0317
Epoch 39/100
10/10 [==============================] - ETA: 0s - loss: 0.0983 - n_outputs0_loss: 0.0722 - n_outputs1_loss: 0.0261
Epoch 00039: val_loss improved from 0.15774 to 0.15441, saving model to ./models/msp-car-1.h5
10/10 [==============================] - 1s 111ms/step - loss: 0.0983 - n_outputs0_loss: 0.0722 - n_outputs1_loss: 0.0261 - val_loss: 0.1544 - val_n_outputs0_loss: 0.1243 - val_n_outputs1_loss: 0.0301
Epoch 40/100
10/10 [==============================] - ETA: 0s - loss: 0.0967 - n_outputs0_loss: 0.0703 - n_outputs1_loss: 0.0265
Epoch 00040: val_loss did not improve from 0.15441
10/10 [==============================] - 1s 103ms/step - loss: 0.0967 - n_outputs0_loss: 0.0703 - n_outputs1_loss: 0.0265 - val_loss: 0.1588 - val_n_outputs0_loss: 0.1275 - val_n_outputs1_loss: 0.0313
Epoch 41/100
10/10 [==============================] - ETA: 0s - loss: 0.0989 - n_outputs0_loss: 0.0736 - n_outputs1_loss: 0.0253
Epoch 00041: val_loss did not improve from 0.15441
10/10 [==============================] - 1s 104ms/step - loss: 0.0989 - n_outputs0_loss: 0.0736 - n_outputs1_loss: 0.0253 - val_loss: 0.1580 - val_n_outputs0_loss: 0.1271 - val_n_outputs1_loss: 0.0308
Epoch 42/100
10/10 [==============================] - ETA: 0s - loss: 0.1010 - n_outputs0_loss: 0.0758 - n_outputs1_loss: 0.0253
Epoch 00042: val_loss did not improve from 0.15441
10/10 [==============================] - 1s 107ms/step - loss: 0.1010 - n_outputs0_loss: 0.0758 - n_outputs1_loss: 0.0253 - val_loss: 0.1614 - val_n_outputs0_loss: 0.1315 - val_n_outputs1_loss: 0.0299
Epoch 43/100
10/10 [==============================] - ETA: 0s - loss: 0.0923 - n_outputs0_loss: 0.0680 - n_outputs1_loss: 0.0243
Epoch 00043: val_loss did not improve from 0.15441
10/10 [==============================] - 1s 101ms/step - loss: 0.0923 - n_outputs0_loss: 0.0680 - n_outputs1_loss: 0.0243 - val_loss: 0.1587 - val_n_outputs0_loss: 0.1298 - val_n_outputs1_loss: 0.0288
Epoch 44/100
10/10 [==============================] - ETA: 0s - loss: 0.0870 - n_outputs0_loss: 0.0629 - n_outputs1_loss: 0.0242
Epoch 00044: val_loss did not improve from 0.15441
10/10 [==============================] - 1s 105ms/step - loss: 0.0870 - n_outputs0_loss: 0.0629 - n_outputs1_loss: 0.0242 - val_loss: 0.1601 - val_n_outputs0_loss: 0.1304 - val_n_outputs1_loss: 0.0296
WARNING: CPU random generator seem to be failing, disable hardware random number generation
WARNING: RDRND generated: 0xffffffff 0xffffffff 0xffffffff 0xffffffff

real	1m10.563s
user	1m11.485s
sys	0m39.110s
```