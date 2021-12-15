# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def geometry(n,p):
    return ((1-p)**(n-1))*p

data = list(map(int,input().split()))
a, b =  data[0], data[1]
n = int(input())

p = a*1.0/b

prob = 0
for i in range(1,n+1):
    prob += geometry(i,p) 
    

print(round(prob,3))