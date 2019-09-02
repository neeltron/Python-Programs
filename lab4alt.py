"""This contains all the solutions to lab 4 practicals"""

# Solution to find the area of triangle
a = int(input())
b = int(input())
c = int(input())
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print(area)

# Solution to find the sum on n natural numbers
n = int(input())
sum = 0
for num in range(0,n+1):
    sum += num
print(sum)

# Solutio to find the roots of a quadratic equation
sq = int(input("Enter the coefficient of x^2: "))
sin = int(input("Enter the coefficient of x: "))
cons = int(input("Enter the constant term: "))
r1 = (-sin + (sin**2-4*sq*cons)**(1/2))/2*sq
r2 = (-sin - (sin**2-4*sq*cons)**(1/2))/2*sq
print("Root 1:",r1,"Root 2:",r2)
