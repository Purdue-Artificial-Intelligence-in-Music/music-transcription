import argparse 
import torch

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i', '--input-file', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output-file', type=str, required=True, help='Output file path')
    
    args = parser.parse_args()
    
    print("HELLO WORLD")
    
    input_file_path = args.input_file
    output_file_path = args.output_file
    
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w')
    
    output_file.write(input_file.readline())
    
    output_file.write("Cuda is available: " + str(torch.cuda.is_available()))
    
    
    def batched_dot_mul_sum(a, b):
        return a.mul(b).sum(-1)


    def batched_dot_bmm(a, b):
        a = a.reshape(-1, 1, a.shape[-1])
        b = b.reshape(-1, b.shape[-1], 1)
        return torch.bmm(a, b).flatten(-3)

    x = torch.randn(10000, 64)

    output_file.write(str(batched_dot_mul_sum(x, x)) + str(batched_dot_bmm(x, x)))
    
    output_file.close()
    input_file.close()