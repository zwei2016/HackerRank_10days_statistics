# Enter your code here. Read input from STDIN. Print output to STDOUT

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n = len(x)

xy = [i*j for i,j in zip(x,y)]
x_square = [i**2 for i in x]

b = (n*sum(xy) - sum(x)*sum(y))*1.0/(n*sum(x_square)-sum(x)**2)
a = sum(y)*1.0/n - b*sum(x)*1.0/n 

score = a + b*80

print(round(score,3))