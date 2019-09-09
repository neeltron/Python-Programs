# Solution to Question number 1
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by 3 and 5 both.")

# Solution to Question number 2
num = int(input("Enter a number"))
if num % 5 == 0:
    print("It is a multiple of 5.")

# Solution to Question number 3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
if sum > 10 and sum < 20:
    sum = 15
print(sum)

# Solution to Question number 4
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    print("First number is greater than the second one.")
elif num2 > num1:
    print("Second number is greater than the first one.")
else:
    print("Both of them are equal.")

# Solution to Question number 5
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Solution to Question number 6
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))
if num1 > num2 and num1 > num3:
    print("First number is the greatest.")
elif num2 > num1 and num2 > num3:
    print("Second number is the greatest.")
else:
    print("Third number is the greatest.")

# Solution to Question number 7
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))
if b**2 - 4*a*c == 0:
    print("real")
else:
    print("Imaginary")

# Solution to Question number 8
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 400 == 0:
        print("Leap Year.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Not a leap year.")
    if year % 4 == 0 and year % 100 != 0:
        print("Leap Year")
else:
    print("Not a leap Year.")

# Solution to Question number 10
name = input("Enter your name: ")
rno = input("Enter your roll number: ")
sapid = input("Enter your SAP ID: ")
course = input("Enter the course enrolled")
sem = input("Enter your Semester: ")
pds = int(input("Enter your marks in PDS: "))
py = int(input("Enter your marks in Python: "))
chem = int(input("Enter your marks in Chemistry: "))
eng = int(input("Enter your marks in English: "))
phy = int(input("Enter your marks in Physics: "))
total = pds + py + chem + eng + phy
per = total * 100 / 500
cgpa = per / 10
if cgpa < 3.4:
    grade = "F"
elif cgpa <= 5:
    grade = "C+"
elif cgpa <= 6:
    grade = "B"
elif cgpa <= 7:
    grade = "B+"
elif cgpa <= 8:
    grade = "A"
elif cgpa <= 9:
    grade = "A+"
elif cgpa <= 10:
    grade = "O"
print("Name:",name,"\nRoll number:",rno,"\t\tSAP ID:",sapid,"\nSemester:",sem,"\t\tCourse:",course,"\nSubject name\tMarks\nPDS:\t\t",pds,"\nPython:\t\t",py,"\nChemistry:\t",chem,"\nEnglish:\t",eng,"\nPhysics:\t",phy,"\nPercentage:\t",per,"\nCGPA:\t",cgpa,"\nGrade:\t",grade)


# Solution to Question number 9
day = int(input("Day = "))
month = int(input("Month = "))
year = int(input("Year = "))
if month in (1,3,5,7,8,10,12):
    if day == 31:
        if month != 12:
            month += 1
            day = 1
    elif day <= 30:
        day += 1
    else:
        print("Invalid day")
elif month in (4,6,9,11):
    if day == 30:
        month += 1
        day = 1
    elif day <= 29:
        day += 1
    else:
        print("Invalid day")
elif month is 2 and day is 28:
    if year % 4 == 0:
        if year % 400 == 0:
            day = 29
            month = 2
        elif year % 100 == 0 and year % 400 != 0:
            day = 1
            month = 3
    if year % 4 == 0 and year % 100 != 0:
        day = 29
        month = 2
    else:
        day = 1
        month = 3
else:
    print("Invalid month")

if month == 12 and day == 31:
    year += 1
    month = 1
    day = 1
elif day == 30:
    month += 1

print("Day:",day,"\nMonth:",month,"\nYear:",year)
