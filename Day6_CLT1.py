# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt, erf

def clt_cdf(x, mean, se, n):
    mean1 = n*mean
    se1 = sqrt(n)*se
    tmp = (x - mean1)*1.0/(se1*sqrt(2))
    return 0.5*(1+erf(tmp))

max_weight = 9800
num_box = 49
mean = 205
se = 15

prob = clt_cdf(max_weight, mean, se, num_box)

print(round(prob,4))