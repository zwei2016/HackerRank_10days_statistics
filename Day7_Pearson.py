# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

def se(x,n):
    tmp = 0
    mean_x = sum(x)*1.0/n
    
    for i in x:
        tmp += (i - mean_x)**2
        
    return sqrt(tmp*1.0/n)
        
def person(x,y,n):
    se_x = se(x,n)
    se_y = se(y,n)
    
    tmp = 0
    mean_x = sum(x)*1.0/n
    mean_y = sum(y)*1.0/n
    
    for i in range(n):
        tmp += (x[i]-mean_x)*(y[i]-mean_y)
        
    return tmp*1.0/(n*se_x*se_y)
    
coef = person(x,y,n)

print(round(coef,3))
    