# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

sample_n = float(input())
mean = float(input())
se = float(input())
prob = float(input())
z_value = float(input())

# reverse of CLT
ci_value = z_value*se/sqrt(sample_n) 

L = mean - ci_value
U = mean + ci_value

print(round(L,2))
print(round(U,2))
