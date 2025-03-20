#code:1
a=10
b=2
if b>a:
    print('b is greater')
else:
    print('a is greater')
#code:2
marks=int(input("Enter your marks:"))
if marks>=80:
    print("You got A1 Grade")
elif marks>=70:
    print("You got A Grade")
elif marks>=60:
    print("You got B Gradee")
elif marks>=50:
    print("You got C Grade")
else:
    print("You are Fail!")
#code:3
email=input("Enter your email:")
passw=input("Enter your password:")
if email== "abcxyz@gmail.com" and passw=="qwerty":
    print("Login successfully")
else:
    print("Login Failed; Incorrect Email or Password")
#code:4
def name():
    print("Hello my name is Dice\nI am a Data Scientist")
name()
#code:5
import calendar
print(calendar.month(2004,8))
#code:6
def sub(a,b):
     print(a+b)
sub(5,7)
#code:7
def sum(a,b=5,c=10):
    return(a+b+c)
sum(5)
#code:8
def egligible():
    age=int(input('Enter your age:'))
    if age>=18:
        print("You are egligible for liscense.")
    else:
        print("You are not egligible for Liscense!")
egligible()
#code:9
print("Heloo Python", end="\n\n\n\n")
#code:10
city=print('Karachi')
#code:11
num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
print(num1+num2)
#code:12
width=int(input('Enter width of rectangle:'))
height=int(input('Enter height of Rectangle:'))
Area=print(width*height)
#code:13
print("      1\n     1 2\n    1 2 3\n   1 2 3 4\n  1 2 3 4 5\n 1 2 3 4 5 6")