import math
import numpy as np

'''
MLE for test set 3, too big numbers, needs more advanced
prime finding techniques, actually, given N as input
i need just the next prime after sqrt(N) and the previous
2 below sqrt(N) so just 3 primes in total but finding
them for N up to 10e18 is not trivial.
'''

def largest_primes_under(number, cap):
    n = cap - 1
    while number and n >= 2:
        if all(n % d for d in range(2, int(n ** 0.5 + 1))):
            yield n
            number -= 1
        n -= 1

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def solve(num):
	#print(primes(int(math.sqrt(num))))
	top = int(math.sqrt(num*2))
	prms = primes(max(8, top))[::-1]
	for p1, p2 in zip(prms, prms[1:]):
		if p1*p2 <= num:
			return p1*p2

TEST = int(input())

for i in range(TEST):
	num = int(input())
	res = solve(num)
	print(f"Case #{i+1}: {res}")