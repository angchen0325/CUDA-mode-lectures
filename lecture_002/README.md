## Lecture 2 examples

Please make sure PyTorch (2.1.2) and cuda-toolkit (nvcc compiler) are installed.
  - `vector-addition`: Classic CUDA C example, to compile use `make` in the `vector-addition` directory.
  - `rgb2grayscale`: Example uses PyTorch's `torch.utils.cpp_extension.load_inline` feature to compile a custom RGB to grayscale kernel and uses it to convert input image to grayscale and which is saved in as `output.png`. Run in the `rgb2grayscale` folder `python rgb2grayscale.py`.
  - `mean-filter`: This example also uses the PyTorch's `cpp_extension.load_inline` feature to compile a mean filter kernel. The kernel read pixel values in the surrounding (square area) of a pixel and computes the average value for each RGB channel individualy. The result is saved to `output.png`. Run in the `mean-filter` folder `python mean_filter.py`.
 