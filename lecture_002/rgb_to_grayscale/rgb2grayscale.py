from pathlib import Path
import torch
from torchvision.io import read_image, write_png
from torch.utils.cpp_extension import load_inline


def compile_extension():
    cuda_source = Path("grayscale_kernel.cu").read_text()
    cpp_source = "torch::Tensor rgb2grayscale(torch::Tensor image);"

    # Load the CUDA kernel as a PyTorch extension
    rgb2grayscale_extension = load_inline(
        name="rgb2grayscale_extension",
        cpp_sources=cpp_source,
        cuda_sources=cuda_source,
        functions=["rgb2grayscale"],
        with_cuda=True,
        extra_cuda_cflags=["-O2"],
        # build_directory='./cuda_build',
    )
    return rgb2grayscale_extension


def main():
    """
    Use torch cpp inline extension function to compile the kernel in grayscale_kernel.cu.
    Read input image, convert it to grayscale via custom cuda kernel and write it out as png.
    """
    ext = compile_extension()

    x = read_image("universe_hubble.jpg").permute(1, 2, 0).cuda()
    print("mean:", x.float().mean())
    print("Input image:", x.shape, x.dtype)

    assert x.dtype == torch.uint8

    y = ext.rgb2grayscale(x)

    print("Output image:", y.shape, y.dtype)
    print("mean", y.float().mean())
    write_png(y.permute(2, 0, 1).cpu(), "universe_hubble_gray.png")


if __name__ == "__main__":
    main()
