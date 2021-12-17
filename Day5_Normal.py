# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt, erf

mean, se = 20, 2
t1 = 19.5
t2, t3 = 20, 22

def cdf(x):
    tmp = (x - mean)*1.0/(se*sqrt(2))
    return 0.5*(1+erf(tmp))

print(round(cdf(19.5),3))
print(round(cdf(22)-cdf(20),3))