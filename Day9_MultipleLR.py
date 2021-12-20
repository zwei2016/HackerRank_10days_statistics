# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
m, n = map(int, input().split())
X, Y = [], []

for i in range(n):
    x = []
    line = list(map(float, input().split()))
    for j in range(m):
        x.append(line[j])
    X.append(x)
    Y.append(line[m])

#print(Y)

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
#print(a,b)

q = int(input())
new_X = []
for i in range(q):
    x = []
    line = list(map(float, input().split()))
    for j in range(len(line)):
        x.append(line[j])
    
    new_X.append(x)

#print(new_X)

for line in new_X:
    n = len(line)
    ans = a
    for i in range(n):
        ans += line[i]*b[i] 
    print(round(ans,2))