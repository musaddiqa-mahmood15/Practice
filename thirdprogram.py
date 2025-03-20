#code:1
number=int(input("enter your number:"))
rem=number%2
if rem==0:
    print("Even Number")
else:
    print("Odd Number")
#code:2
num1=int(input('First number:'))
num2=int(input('Second number:'))
num3=int(input('Third number:'))
if num1>num2 and num1>num3:
    print('First number is greatest')
elif num2>num1 and num2>num3:
    print('Second number is greatest')
else:
    print('Third number is greatest')
#code:3
a=int(input('First number:'))
b=int(input('Second number:'))
c=int(input('Third number:'))
d=int(input('fourth number:'))
if a>b and a>c and a>d:
    print('First number is greatest')
elif b>a and b>c and b>d:
    print('Second number is greatest')
elif c>a and c>b and c>d:
    print('Third number is greater')   
else:
    print('Fourth number is greatest')
#code:4
num_check=int(input('Enter number to check:'))
rem=num_check%7
if rem==0:
    print('Number is multiple of 7')
else:
    print('Number is not multiple of seven.')
#code:5
import sys
print(sys.version)
print(sys.version_info)
#code:6
a=5
print(bool(a>0))
#code:7
print('Welcome')
for x in range(5):
    print(x)
    print('Good Morning World!')
#code:8
def greet():
    print('Hello!\nHow are you?')
print('Start of a program')    
greet()
print('End of program')
#code:9
def hello():
    print('Hello\nMy name is Dice.')
print('Hi..\nWhat is your name?')
hello()
print('Great Dice. Nice to meet you!')
#code:10
def sum(a,b):
    print(f'The sum of {a} and {b} is:{a+b}')
sum(4,5)
#code:11
name=input('Enter your name:')
age=input('Enter your age:')
print("Heloo! "+name+". You are "+age+" years old.")

b=id(12)
print(b)