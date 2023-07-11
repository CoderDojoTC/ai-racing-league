# Training Log for MSP Car #1

After cleanup we only got about 1,500 records.  But here is a log of the training.  It took about 1.5 minutes.

```sh
$ donkey train --tub=./data/msp-car-1 --model=./models/msp-car-1.f5

```
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
2021-07-26 19:50:45.562205: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2021-07-26 19:50:45.565106: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3592950000 Hz
2021-07-26 19:50:45.565470: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55d85e9d19f0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-07-26 19:50:45.565492: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-07-26 19:50:45.565578: I tensorflow/core/common_runtime/process_util.cc:147] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.
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
10/10 [==============================] - ETA: 0s - loss: 1.0885 - n_outputs0_loss: 0.5975 - n_outputs1_loss: 0.4909
Epoch 00001: val_loss improved from inf to 0.54341, saving model to ./models/msp-car-1.f5
2021-07-26 19:50:57.881390: W tensorflow/python/util/util.cc:329] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.
WARNING:tensorflow:From /home/arl/miniconda3/envs/donkey/lib/python3.7/site-packages/tensorflow/python/ops/resource_variable_ops.py:1817: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
10/10 [==============================] - 11s 1s/step - loss: 1.0885 - n_outputs0_loss: 0.5975 - n_outputs1_loss: 0.4909 - val_loss: 0.5434 - val_n_outputs0_loss: 0.4668 - val_n_outputs1_loss: 0.0767
Epoch 2/100
10/10 [==============================] - ETA: 0s - loss: 0.5522 - n_outputs0_loss: 0.4640 - n_outputs1_loss: 0.0882
Epoch 00002: val_loss improved from 0.54341 to 0.53272, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 999ms/step - loss: 0.5522 - n_outputs0_loss: 0.4640 - n_outputs1_loss: 0.0882 - val_loss: 0.5327 - val_n_outputs0_loss: 0.4605 - val_n_outputs1_loss: 0.0722
Epoch 3/100
10/10 [==============================] - ETA: 0s - loss: 0.5392 - n_outputs0_loss: 0.4638 - n_outputs1_loss: 0.0754
Epoch 00003: val_loss improved from 0.53272 to 0.50775, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.5392 - n_outputs0_loss: 0.4638 - n_outputs1_loss: 0.0754 - val_loss: 0.5077 - val_n_outputs0_loss: 0.4551 - val_n_outputs1_loss: 0.0527
Epoch 4/100
10/10 [==============================] - ETA: 0s - loss: 0.5318 - n_outputs0_loss: 0.4605 - n_outputs1_loss: 0.0713
Epoch 00004: val_loss improved from 0.50775 to 0.49783, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 999ms/step - loss: 0.5318 - n_outputs0_loss: 0.4605 - n_outputs1_loss: 0.0713 - val_loss: 0.4978 - val_n_outputs0_loss: 0.4455 - val_n_outputs1_loss: 0.0523
Epoch 5/100
10/10 [==============================] - ETA: 0s - loss: 0.5333 - n_outputs0_loss: 0.4608 - n_outputs1_loss: 0.0725
Epoch 00005: val_loss improved from 0.49783 to 0.49721, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.5333 - n_outputs0_loss: 0.4608 - n_outputs1_loss: 0.0725 - val_loss: 0.4972 - val_n_outputs0_loss: 0.4451 - val_n_outputs1_loss: 0.0521
Epoch 6/100
10/10 [==============================] - ETA: 0s - loss: 0.5277 - n_outputs0_loss: 0.4619 - n_outputs1_loss: 0.0658
Epoch 00006: val_loss did not improve from 0.49721
10/10 [==============================] - 9s 934ms/step - loss: 0.5277 - n_outputs0_loss: 0.4619 - n_outputs1_loss: 0.0658 - val_loss: 0.4981 - val_n_outputs0_loss: 0.4461 - val_n_outputs1_loss: 0.0520
Epoch 7/100
10/10 [==============================] - ETA: 0s - loss: 0.5265 - n_outputs0_loss: 0.4577 - n_outputs1_loss: 0.0688
Epoch 00007: val_loss improved from 0.49721 to 0.49668, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.5265 - n_outputs0_loss: 0.4577 - n_outputs1_loss: 0.0688 - val_loss: 0.4967 - val_n_outputs0_loss: 0.4442 - val_n_outputs1_loss: 0.0525
Epoch 8/100
10/10 [==============================] - ETA: 0s - loss: 0.5138 - n_outputs0_loss: 0.4467 - n_outputs1_loss: 0.0671
Epoch 00008: val_loss improved from 0.49668 to 0.49536, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.5138 - n_outputs0_loss: 0.4467 - n_outputs1_loss: 0.0671 - val_loss: 0.4954 - val_n_outputs0_loss: 0.4408 - val_n_outputs1_loss: 0.0546
Epoch 9/100
10/10 [==============================] - ETA: 0s - loss: 0.5109 - n_outputs0_loss: 0.4468 - n_outputs1_loss: 0.0642
Epoch 00009: val_loss improved from 0.49536 to 0.48741, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.5109 - n_outputs0_loss: 0.4468 - n_outputs1_loss: 0.0642 - val_loss: 0.4874 - val_n_outputs0_loss: 0.4353 - val_n_outputs1_loss: 0.0521
Epoch 10/100
10/10 [==============================] - ETA: 0s - loss: 0.5030 - n_outputs0_loss: 0.4405 - n_outputs1_loss: 0.0625
Epoch 00010: val_loss did not improve from 0.48741
10/10 [==============================] - 9s 930ms/step - loss: 0.5030 - n_outputs0_loss: 0.4405 - n_outputs1_loss: 0.0625 - val_loss: 0.4936 - val_n_outputs0_loss: 0.4351 - val_n_outputs1_loss: 0.0585
Epoch 11/100
10/10 [==============================] - ETA: 0s - loss: 0.4974 - n_outputs0_loss: 0.4310 - n_outputs1_loss: 0.0664
Epoch 00011: val_loss improved from 0.48741 to 0.47748, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 11s 1s/step - loss: 0.4974 - n_outputs0_loss: 0.4310 - n_outputs1_loss: 0.0664 - val_loss: 0.4775 - val_n_outputs0_loss: 0.4238 - val_n_outputs1_loss: 0.0536
Epoch 12/100
10/10 [==============================] - ETA: 0s - loss: 0.4887 - n_outputs0_loss: 0.4208 - n_outputs1_loss: 0.0679
Epoch 00012: val_loss did not improve from 0.47748
10/10 [==============================] - 9s 925ms/step - loss: 0.4887 - n_outputs0_loss: 0.4208 - n_outputs1_loss: 0.0679 - val_loss: 0.4836 - val_n_outputs0_loss: 0.4148 - val_n_outputs1_loss: 0.0687
Epoch 13/100
10/10 [==============================] - ETA: 0s - loss: 0.4591 - n_outputs0_loss: 0.3927 - n_outputs1_loss: 0.0664
Epoch 00013: val_loss improved from 0.47748 to 0.40567, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.4591 - n_outputs0_loss: 0.3927 - n_outputs1_loss: 0.0664 - val_loss: 0.4057 - val_n_outputs0_loss: 0.3540 - val_n_outputs1_loss: 0.0516
Epoch 14/100
10/10 [==============================] - ETA: 0s - loss: 0.4323 - n_outputs0_loss: 0.3665 - n_outputs1_loss: 0.0658
Epoch 00014: val_loss improved from 0.40567 to 0.37099, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.4323 - n_outputs0_loss: 0.3665 - n_outputs1_loss: 0.0658 - val_loss: 0.3710 - val_n_outputs0_loss: 0.3153 - val_n_outputs1_loss: 0.0556
Epoch 15/100
10/10 [==============================] - ETA: 0s - loss: 0.3754 - n_outputs0_loss: 0.3063 - n_outputs1_loss: 0.0691
Epoch 00015: val_loss improved from 0.37099 to 0.33956, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.3754 - n_outputs0_loss: 0.3063 - n_outputs1_loss: 0.0691 - val_loss: 0.3396 - val_n_outputs0_loss: 0.2853 - val_n_outputs1_loss: 0.0542
Epoch 16/100
10/10 [==============================] - ETA: 0s - loss: 0.3314 - n_outputs0_loss: 0.2723 - n_outputs1_loss: 0.0591
Epoch 00016: val_loss improved from 0.33956 to 0.30289, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.3314 - n_outputs0_loss: 0.2723 - n_outputs1_loss: 0.0591 - val_loss: 0.3029 - val_n_outputs0_loss: 0.2524 - val_n_outputs1_loss: 0.0505
Epoch 17/100
10/10 [==============================] - ETA: 0s - loss: 0.3168 - n_outputs0_loss: 0.2591 - n_outputs1_loss: 0.0576
Epoch 00017: val_loss improved from 0.30289 to 0.28694, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.3168 - n_outputs0_loss: 0.2591 - n_outputs1_loss: 0.0576 - val_loss: 0.2869 - val_n_outputs0_loss: 0.2390 - val_n_outputs1_loss: 0.0479
Epoch 18/100
10/10 [==============================] - ETA: 0s - loss: 0.2990 - n_outputs0_loss: 0.2446 - n_outputs1_loss: 0.0544
Epoch 00018: val_loss improved from 0.28694 to 0.27270, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2990 - n_outputs0_loss: 0.2446 - n_outputs1_loss: 0.0544 - val_loss: 0.2727 - val_n_outputs0_loss: 0.2257 - val_n_outputs1_loss: 0.0470
Epoch 19/100
10/10 [==============================] - ETA: 0s - loss: 0.2706 - n_outputs0_loss: 0.2185 - n_outputs1_loss: 0.0521
Epoch 00019: val_loss improved from 0.27270 to 0.25193, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2706 - n_outputs0_loss: 0.2185 - n_outputs1_loss: 0.0521 - val_loss: 0.2519 - val_n_outputs0_loss: 0.2099 - val_n_outputs1_loss: 0.0421
Epoch 20/100
10/10 [==============================] - ETA: 0s - loss: 0.2602 - n_outputs0_loss: 0.2112 - n_outputs1_loss: 0.0490
Epoch 00020: val_loss improved from 0.25193 to 0.23899, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2602 - n_outputs0_loss: 0.2112 - n_outputs1_loss: 0.0490 - val_loss: 0.2390 - val_n_outputs0_loss: 0.1974 - val_n_outputs1_loss: 0.0416
Epoch 21/100
10/10 [==============================] - ETA: 0s - loss: 0.2345 - n_outputs0_loss: 0.1866 - n_outputs1_loss: 0.0479
Epoch 00021: val_loss improved from 0.23899 to 0.23396, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2345 - n_outputs0_loss: 0.1866 - n_outputs1_loss: 0.0479 - val_loss: 0.2340 - val_n_outputs0_loss: 0.1911 - val_n_outputs1_loss: 0.0428
Epoch 22/100
10/10 [==============================] - ETA: 0s - loss: 0.2229 - n_outputs0_loss: 0.1758 - n_outputs1_loss: 0.0471
Epoch 00022: val_loss improved from 0.23396 to 0.22651, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2229 - n_outputs0_loss: 0.1758 - n_outputs1_loss: 0.0471 - val_loss: 0.2265 - val_n_outputs0_loss: 0.1858 - val_n_outputs1_loss: 0.0407
Epoch 23/100
10/10 [==============================] - ETA: 0s - loss: 0.2175 - n_outputs0_loss: 0.1730 - n_outputs1_loss: 0.0445
Epoch 00023: val_loss improved from 0.22651 to 0.22245, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2175 - n_outputs0_loss: 0.1730 - n_outputs1_loss: 0.0445 - val_loss: 0.2225 - val_n_outputs0_loss: 0.1806 - val_n_outputs1_loss: 0.0419
Epoch 24/100
10/10 [==============================] - ETA: 0s - loss: 0.2084 - n_outputs0_loss: 0.1624 - n_outputs1_loss: 0.0460
Epoch 00024: val_loss improved from 0.22245 to 0.20674, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.2084 - n_outputs0_loss: 0.1624 - n_outputs1_loss: 0.0460 - val_loss: 0.2067 - val_n_outputs0_loss: 0.1694 - val_n_outputs1_loss: 0.0374
Epoch 25/100
10/10 [==============================] - ETA: 0s - loss: 0.1889 - n_outputs0_loss: 0.1457 - n_outputs1_loss: 0.0432
Epoch 00025: val_loss improved from 0.20674 to 0.20416, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1889 - n_outputs0_loss: 0.1457 - n_outputs1_loss: 0.0432 - val_loss: 0.2042 - val_n_outputs0_loss: 0.1638 - val_n_outputs1_loss: 0.0403
Epoch 26/100
10/10 [==============================] - ETA: 0s - loss: 0.1882 - n_outputs0_loss: 0.1467 - n_outputs1_loss: 0.0414
Epoch 00026: val_loss improved from 0.20416 to 0.19422, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1882 - n_outputs0_loss: 0.1467 - n_outputs1_loss: 0.0414 - val_loss: 0.1942 - val_n_outputs0_loss: 0.1557 - val_n_outputs1_loss: 0.0385
Epoch 27/100
10/10 [==============================] - ETA: 0s - loss: 0.1706 - n_outputs0_loss: 0.1328 - n_outputs1_loss: 0.0378
Epoch 00027: val_loss did not improve from 0.19422
10/10 [==============================] - 9s 930ms/step - loss: 0.1706 - n_outputs0_loss: 0.1328 - n_outputs1_loss: 0.0378 - val_loss: 0.2016 - val_n_outputs0_loss: 0.1615 - val_n_outputs1_loss: 0.0401
Epoch 28/100
10/10 [==============================] - ETA: 0s - loss: 0.1630 - n_outputs0_loss: 0.1248 - n_outputs1_loss: 0.0382
Epoch 00028: val_loss improved from 0.19422 to 0.18035, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1630 - n_outputs0_loss: 0.1248 - n_outputs1_loss: 0.0382 - val_loss: 0.1803 - val_n_outputs0_loss: 0.1445 - val_n_outputs1_loss: 0.0358
Epoch 29/100
10/10 [==============================] - ETA: 0s - loss: 0.1601 - n_outputs0_loss: 0.1219 - n_outputs1_loss: 0.0382
Epoch 00029: val_loss improved from 0.18035 to 0.17528, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1601 - n_outputs0_loss: 0.1219 - n_outputs1_loss: 0.0382 - val_loss: 0.1753 - val_n_outputs0_loss: 0.1410 - val_n_outputs1_loss: 0.0343
Epoch 30/100
10/10 [==============================] - ETA: 0s - loss: 0.1483 - n_outputs0_loss: 0.1117 - n_outputs1_loss: 0.0366
Epoch 00030: val_loss improved from 0.17528 to 0.17039, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1483 - n_outputs0_loss: 0.1117 - n_outputs1_loss: 0.0366 - val_loss: 0.1704 - val_n_outputs0_loss: 0.1372 - val_n_outputs1_loss: 0.0332
Epoch 31/100
10/10 [==============================] - ETA: 0s - loss: 0.1481 - n_outputs0_loss: 0.1114 - n_outputs1_loss: 0.0368
Epoch 00031: val_loss did not improve from 0.17039
10/10 [==============================] - 9s 915ms/step - loss: 0.1481 - n_outputs0_loss: 0.1114 - n_outputs1_loss: 0.0368 - val_loss: 0.1783 - val_n_outputs0_loss: 0.1436 - val_n_outputs1_loss: 0.0347
Epoch 32/100
10/10 [==============================] - ETA: 0s - loss: 0.1470 - n_outputs0_loss: 0.1111 - n_outputs1_loss: 0.0358
Epoch 00032: val_loss improved from 0.17039 to 0.16278, saving model to ./models/msp-car-1.f5
10/10 [==============================] - 10s 1s/step - loss: 0.1470 - n_outputs0_loss: 0.1111 - n_outputs1_loss: 0.0358 - val_loss: 0.1628 - val_n_outputs0_loss: 0.1301 - val_n_outputs1_loss: 0.0327
Epoch 33/100
10/10 [==============================] - ETA: 0s - loss: 0.1368 - n_outputs0_loss: 0.1027 - n_outputs1_loss: 0.0341
Epoch 00033: val_loss did not improve from 0.16278
10/10 [==============================] - 9s 928ms/step - loss: 0.1368 - n_outputs0_loss: 0.1027 - n_outputs1_loss: 0.0341 - val_loss: 0.1666 - val_n_outputs0_loss: 0.1345 - val_n_outputs1_loss: 0.0320
Epoch 34/100
10/10 [==============================] - ETA: 0s - loss: 0.1305 - n_outputs0_loss: 0.0971 - n_outputs1_loss: 0.0334
Epoch 00034: val_loss did not improve from 0.16278
10/10 [==============================] - 9s 929ms/step - loss: 0.1305 - n_outputs0_loss: 0.0971 - n_outputs1_loss: 0.0334 - val_loss: 0.1728 - val_n_outputs0_loss: 0.1413 - val_n_outputs1_loss: 0.0315
Epoch 35/100
10/10 [==============================] - ETA: 0s - loss: 0.1353 - n_outputs0_loss: 0.1027 - n_outputs1_loss: 0.0326
Epoch 00035: val_loss did not improve from 0.16278
10/10 [==============================] - 9s 933ms/step - loss: 0.1353 - n_outputs0_loss: 0.1027 - n_outputs1_loss: 0.0326 - val_loss: 0.1706 - val_n_outputs0_loss: 0.1391 - val_n_outputs1_loss: 0.0315
Epoch 36/100
10/10 [==============================] - ETA: 0s - loss: 0.1319 - n_outputs0_loss: 0.0989 - n_outputs1_loss: 0.0331
Epoch 00036: val_loss did not improve from 0.16278
10/10 [==============================] - 9s 936ms/step - loss: 0.1319 - n_outputs0_loss: 0.0989 - n_outputs1_loss: 0.0331 - val_loss: 0.1729 - val_n_outputs0_loss: 0.1401 - val_n_outputs1_loss: 0.0328
Epoch 37/100
10/10 [==============================] - ETA: 0s - loss: 0.1290 - n_outputs0_loss: 0.0952 - n_outputs1_loss: 0.0338
Epoch 00037: val_loss did not improve from 0.16278
10/10 [==============================] - 9s 929ms/step - loss: 0.1290 - n_outputs0_loss: 0.0952 - n_outputs1_loss: 0.0338 - val_loss: 0.1709 - val_n_outputs0_loss: 0.1381 - val_n_outputs1_loss: 0.0327
WARNING: CPU random generator seem to be failing, disable hardware random number generation
WARNING: RDRND generated: 0xffffffff 0xffffffff 0xffffffff 0xffffffff
(donkey) arl@arl1:
```