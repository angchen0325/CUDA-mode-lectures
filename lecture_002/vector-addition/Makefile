NVCC        = "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.5/bin/nvcc"
NVCC_FLAGS  = -O3 -I"C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.5/include"
LD_FLAGS    = -lcudart -L"C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.5/lib/x64"
EXE	        = vector_addition
OBJ	        = vector_addition.o

default: $(EXE)

$(EXE).o: $(EXE).cu
	$(NVCC) -c -o $@ $(EXE).cu $(NVCC_FLAGS)

$(EXE): $(OBJ)
	$(NVCC) $(OBJ) -o $(EXE) $(LD_FLAGS)

clean:
	rm -rf *.o $(EXE)