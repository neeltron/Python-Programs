
"""Solution to Questio number 1"""

x = 9
y = 7
z = x + y # For addition
print(z)
z = x - y # For Subtraction
print(z)
z = x * y # For Multiplication
print(z)
z = x / y # For Division
print(z)


"""Solution to Question number 2"""

side = 145
area = side * side
print(area)

"""Solution to Question 3"""

base = 120
height = 33
area = 1/2 * base * height
print(area)

"""Solution to Question 4"""
radius = 12
area = 3.14 * radius * radius

"""Solution to Question 5"""
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = (x * y) * (x * y)
print(z)

"""Solution to Question 6"""
a = 133
b = 72
c = (a^2+b^2)**1/2
print(c)

"""Solution to question 7"""
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = a
a = b
b = c
print("A is", a, "B is", b)

"""Solution to Question 8
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
i = 1
lcm = 1
while i <= num2:
    if num1 % i == 0 or num2 % i == 0:
        lcm = lcm * i
    i += 1
print(lcm)
    """
