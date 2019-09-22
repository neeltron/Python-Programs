# Q1) Find a factorial of given number.
num = int(input("Enter a number: "))
fact = 1
for n in range(1, num+1):
    fact *= n
print(fact)

# Q2) To find whether the given number is Armstrong number.
num1 = int(input("Enter a number: "))
res = 0
temp = num1
while num1 > 0:
    dig = num1 % 10
    num1 = num1 // 10
    res = res + dig*dig*dig
print(res)
if res == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number.")

# Q3) Print Fibonacci series up to given term.
"""
This one's experimental
num = int(input("Enter a number: "))
sk = 0
pr = 0
ne = 1
print(str(ne))
while ne < num:
    print(str(ne))
    pr = ne
    sk = ne - pr
    ne = ne + pr"""

# Q4) Write a program to find prime number.
n = int(input("Enter a number: "))
count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
if count == 0:
    print("Prime")
else:
    print("Not prime")

# Q5) Check whether given number is palindrome or not.
n = int(input("Enter a number: "))
rev = 0
temp = n
while n > 0:
    rev *= 10
    rev = rev + n % 10
    n = n // 10
if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q6) Write a program to print sum of digits.
num = int(input("Enter a number: "))
res = 0
while num > 0:
    dig = num % 10
    num = num // 10
    res += dig
print(res)

# Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100.
for n in range (1, 100):
    if n % 5 == 0 or n % 7 == 0:
        print(n)

# Q8) All lower case to upper in string.
s = input("Enter a string: ")
print(s.upper())

# Q9) Print prime numbers between 1 and 100.

for i in range(2, 100):
    pr = 0
    for j in range(2, i):
        if i % j == 0:
            pr = 1
    if pr < 1:
        print(i)
        
# Q10) Print the table for a given number:
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
