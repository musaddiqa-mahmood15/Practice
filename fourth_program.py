#code:1 ---while loop
i=1
while i<=100:
    print(i)
    i+=1
#code:2----while loop
k=100
while k>=1:
    print(k)
    k-=1
#code:3----while loop
i=1
n=int(input("Enter value os n:"))
while i<=10:
    print(i*n)
    i+=1
#code:4--- def keyword fuction
def area():
    b=int(input('Enter the radius of circle:'))
    area=3.142*(b**2)
    print(f'The area of number is:{area}')
area()    
#code:5---def keyword function
def info():
    name=input('Enter your name:')
    age=int(input('Enter your age:'))
    print(f"Your name is {name}\nYou're {age} years old. ")
info()
#code:6---Write a Python program that takes two inputs from the user: one integer and one string representing a number. The program should perform the following operations:
# Convert the string input to an integer.
# Add the two integers together.
# Print the result of the addition.
num1=int(input('Enter first number:'))
num2=input("enter second number:")
print(type(num2))
num_int=int(num2)
print(type(num_int))
num_result=num1 + num_int
print(num_result)
#code:7---Format method
a=int(input('First number:'))
b=int(input('second number:'))
add=a+b
sub=a-b
mult=a*b
print("The sum of a and b is {}, difference of a and b is {} and multiplication of a and b is {}.".format(add,sub,mult))
#code:8---Accessing a Specific Digit from a Number
# Ask the user to input a number (first number)
# Ask the user to input another numbger, which will be trated as specific digit from first number
# Print the digit of (first number) at the specified number (second number)
a=input("Enter a number:")
b=int(input('Enter number of position:'))
c=a[b-1]
print(c)