Basics to read before going into the below:  
1. [Basic intro to GPU arch](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#)  
2. [Programming model and Memory model of GPU](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model)  
  
List of curated blog posts that will give a basic idea of CUDA model.  
  
1. [Intro](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)  
2. [Data transfers between host CPU and GPU device](https://developer.nvidia.com/blog/how-overlap-data-transfers-cuda-cc/)  
3. [Global HBM access](https://developer.nvidia.com/blog/how-access-global-memory-efficiently-cuda-c-kernels/)  
4. [Shared memory usage](https://developer.nvidia.com/blog/using-shared-memory-cuda-cc/)  
  
And finally what lead me to read all these:  
[https://github.com/NVIDIA/cutlass/blob/main/media/docs/efficient_gemm.md#warp-specialization](https://github.com/NVIDIA/cutlass/blob/main/media/docs/efficient_gemm.md#warp-specialization)  
  
which is the instruction set (available only since H100) used in the latest FlashAttention-3 release