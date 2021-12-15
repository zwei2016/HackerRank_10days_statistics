# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n==0: return 1
    ans = 1
    for i in range(1,n+1):
        ans*=i
    return ans

def nCx(n,x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def binomial(x, n, p):
    return nCx(n,x)*1.0*(p**x)*((1-p)**(n-x))


input_list = list(map(float, input().split()))
a, b = input_list[0], input_list[1]

p = a/(a+b)    

prob = 0
for i in range(3,7):
    prob += binomial(i,6,p)
    
    
print(round(prob,3))