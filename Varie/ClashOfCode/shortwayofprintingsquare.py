# flake8: noqa
# print a square made of # of size given in input

n=int(input())
print('\n'.join(['#'*n if(i==0)or(i==n-1)else'#'+' '*(n-2)+'#'for i in range(n)]))