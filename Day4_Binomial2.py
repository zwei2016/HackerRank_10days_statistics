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

input_list = list(map(int, input().split()))
a, b = input_list[0], input_list[1]

p = a*1.0/100

ans1, ans2 = 0, 0

for i in range(0,3):
    ans1 += binomial(i, b, p)
    
for i in range(2,b+1):
    ans2 += binomial(i, b, p)
    
print(round(ans1,3))
print(round(ans2,3))