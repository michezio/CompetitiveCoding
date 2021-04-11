# flake8: noqa
# print 1 if the number of ones in the binary form of the 32 bit hex number given is prime else 0

print(int(bin(int(input(),16)).count('1')in[2,3,5,7,11,13,17,19,23,29,31]))