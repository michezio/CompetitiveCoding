'''
Compute function, takes input_lines and elaborates a solution
producing output_lines to return to the main function which
dumps them in the output file. Here the algorithm takes place.
'''
def compute(input_lines):
    output_lines = input_lines
    return output_lines


##############################################################################


'''
Main function called when launching the script.
It takes the input file path as command line argument,
converts this file into a list of strings (one for each line)
and passes this list to the compute() function, 
which generates another list of strings.
Then it dumps those strings into the output file.
The output file will have '-out' after the name and placed in
the same path as the input file.
'''
def main():
    import os
    import sys
    import time

    assert len(sys.argv) > 1, "Input file path is required"

    input_path = sys.argv[1]
    assert os.path.exists(input_path), "File not found" 

    output_path = input_path[:-4] + "-out.txt"

    print("RUNNING...")
    start_time = time.perf_counter()
    
    with open(input_path, "r") as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]

    output_lines = compute(input_lines)

    with open(output_path, "w") as output_file:
        output_file.write("\n".join(output_lines))

    elapsed_time = time.perf_counter() - start_time
    print(f"COMPLETED IN {elapsed_time:0.4f}s")


if __name__ == "__main__":
    main()