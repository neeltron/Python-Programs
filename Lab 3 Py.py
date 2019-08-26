"""Solution to Question 1"""
p = int(input("Enter Principal "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time: "))
si = (p * r * t) / 100
net_amount = p + si
print(net_amount)

"""Solution to Question 2"""
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
vol = 1/3*3.14*radius*radius*height
print(vol)

"""Solution to question 3"""
base = int(input("Enter the base: "))
height = int(input("Enter the Height: "))
area = 1/2 * base * height
print(area)

"""Solution to question 4"""
sec_in = int(input("Enter time in seconds: "))
hours = 0
mint = 0
if sec_in / 3600 >= 0:
    hours += int(sec_in/3600)
    print(hours)
temp = sec_in - hours * 3600
if temp / 60 >= 0:
    mint += int(temp / 60)
    print(mint)
temp2 = temp - mint * 60
if temp2 / 60 >= 0:
    sec = temp2
    print(sec)
print(str(hours)+":"+str(mint)+":"+str(sec))

"""Solution to question 5"""
inch = int(input("Enter the number of inches"))
ft = int(inch/12)
in_out = int(inch - ft*12)
print(str(ft)+"'"+str(in_out)+"inch")

"""Solution to question 6"""
rad = int(input("Enter radius: "))
height = int(input("Enter Height: "))
vol = 3.14 * rad * rad * height
print(vol)

"""Solution to question 7"""
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = a
a = b
b = c
print("A is", a, "B is", b)
