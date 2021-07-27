$ conda install tensorflow-gpu==2.2.0
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/arl/miniconda3/envs/donkey

  added / updated specs:
    - tensorflow-gpu==2.2.0


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cudatoolkit-10.1.243       |       h6bb024c_0       347.4 MB
    cudnn-7.6.5                |       cuda10.1_0       179.9 MB
    cupti-10.1.168             |                0         1.4 MB
    tensorflow-2.2.0           |gpu_py37h1a511ff_0           4 KB
    tensorflow-base-2.2.0      |gpu_py37h8a81be8_0       181.7 MB
    tensorflow-gpu-2.2.0       |       h0d30ee6_0           3 KB
    ------------------------------------------------------------
                                           Total:       710.4 MB

The following NEW packages will be INSTALLED:

  cudatoolkit        pkgs/main/linux-64::cudatoolkit-10.1.243-h6bb024c_0
  cudnn              pkgs/main/linux-64::cudnn-7.6.5-cuda10.1_0
  cupti              pkgs/main/linux-64::cupti-10.1.168-0
  tensorflow-gpu     pkgs/main/linux-64::tensorflow-gpu-2.2.0-h0d30ee6_0

The following packages will be DOWNGRADED:

  _tflow_select                                   2.3.0-mkl --> 2.1.0-gpu
  tensorflow                       2.2.0-mkl_py37h6e9ce2d_0 --> 2.2.0-gpu_py37h1a511ff_0
  tensorflow-base                  2.2.0-mkl_py37hd506778_0 --> 2.2.0-gpu_py37h8a81be8_0


Proceed ([y]/n)? Y


Downloading and Extracting Packages
tensorflow-base-2.2. | 181.7 MB  | ################################################################################################################################################################ | 100% 
cudnn-7.6.5          | 179.9 MB  | ################################################################################################################################################################ | 100% 
cupti-10.1.168       | 1.4 MB    | ################################################################################################################################################################ | 100% 
tensorflow-2.2.0     | 4 KB      | ################################################################################################################################################################ | 100% 
tensorflow-gpu-2.2.0 | 3 KB      | ################################################################################################################################################################ | 100% 
cudatoolkit-10.1.243 | 347.4 MB  | ################################################################################################################################################################ | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done