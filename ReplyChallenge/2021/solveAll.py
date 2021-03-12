import os

# change the python_exec to use different python interpreters
python_exec = "pypy3"
# change the path to the folder containing the input files
path = "input\\"

for name in ["data_scenarios_a_example.txt",
    "data_scenarios_b_mumbai.txt",
    "data_scenarios_c_metropolis.txt",
    "data_scenarios_d_polynesia.txt",
    "data_scenarios_e_sanfrancisco.txt",
    "data_scenarios_f_tokyo.txt"]:
    os.system(f"{python_exec} solve.py {path}{name}")
