# Lab 6 Practical no 5
# Q1) Write a program to count and display the number of capital letters in a given string.
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch.isupper():
        count+=1
print(count)

# Q2) Count total number of vowels in a given string.
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
print(count)

# Q3) Input a sentence and print words in separate lines.
string = input("Enter a sentence: ")
for i in string:
    if i == ' ':
        print()
    print(i, end = "")

# Q3.5) Count the frequency of characters in a given string.
str = input("Enter a string: ")
temp = ""
for i in str:
    count = 0
    if i not in temp:
        temp += i
        for j in str:
            if i == j:
                count += 1
        print(i, ":", count)
    

# Q3.6) Check whether the string is palindrome
str = input("Enter a string: ")
rev = str[::-1]
if rev == str:
    print(rev)
    print("Palindrome")
else:
    print("Not palindrome")

# Q3.7) To convert lower case to upper
str = input("Enter a string: ")
print(str.upper())

# Q3.8) Count and display words in a given sentence
str = input("Enter a string: ")
lst = str.split()
count = 0
for i in lst:
    count += 1
print(count)

# Q 3.8) Capitalize first character of each word in a given sentence
str = input("Enter a sentence: ")
print(str.title())

# Q 3.9) Capitalize first character without using title()
str = input("Enter a sentence: ") + " "
lst = []
temp = ""
for i in str:
    if i != " ":
        temp += i
    elif i == " ":
        lst.append(temp)
        temp = ""
for i in lst:
    print(i, end = " ")
