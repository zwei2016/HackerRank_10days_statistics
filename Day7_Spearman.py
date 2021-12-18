# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

# X, Y contain unique values
rank_x = [sorted(x).index(i) for i in x]
rank_y = [sorted(y).index(i) for i in y]

d = [xr - yr for xr, yr in zip(rank_x, rank_y)]

spearman = 1 - 6*sum([i**2 for i in d])*1.0/(n*(n**2-1))

print(round(spearman,3))