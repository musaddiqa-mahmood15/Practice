#While Loop--------(use when work in iterator like having variables to update and have stopping condition)
count=1
while count<=5:
    print('Hello World')
    count=count+1 
i=1
while i<=8:
    print(i)
    i+=1
print (count,i)
j=5
while j>=1:
    print(j)
    j-=1
#Print numbers from 1-100
i=1
while i<=100:
    print(i)
    i+=1
#Print numbers from 100-1
j=100
while j>=1:
    print(j)
    j-=1
#Print multiplication table of a number
n=int(input('enter number to multiplication:'))
k=1
while k<=10:
    print(str(n)+'x'+str(k)+'='+str(n*k)) 
    k+=1
#Print the elements of the following list while using loop
lst=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(lst):
    print(lst[idx])
    idx+=1
#Another practice
lst1=['banana','apple','cherry','papaya','pear','guava','pineapple','custurd apple']
indx=0
while indx<len(lst1):
    print(lst1[indx])
    indx+=1
#Print squares of 1-10 from loop
m=1
while m<=10:
    print(m**2)
    m+=1
#search for a number x in the tuple while using loop
nums=(1,4,9,16,25,36,49,64,81,100,36)
x=36
f=0
while f<len(nums):
    if (nums[f]==x):
        print('Found value of x at index:',f)
    f+=1
#Break and Countinue Keyword
u=1
while u<=23:
    print(u)
    if u==13:
        break
    u+=1
print('end of loop')
o=0
while o<=5:
    if(o==3):
        o+=1
        continue
    print(o) 
    o+=1
#print odd number
t=1
while t<=10:
    if(t%2==0):
        t+=1
        continue
    print(t)
    t+=1
#print even number
r=1
while r<=10:
    if(r%2!=0):
        r+=1
        continue
    print(r)
    r+=1
#For Loop--------(use when have to traverse in data-type)
list=[1,2,3,4,5,6,7,8]
for value in list:
    print(value)
vegatables=['potato','brinjal','ladyfinger','tomato','cucembur']
for veglist in vegatables:
    print(veglist)
tup=(1,2,3,4)
for num in tup:
    print(num)
str='musaddiqa'
for char in str:
    if(char=='d'):
        print('d found')
        break
    print(char)
else:
    print('end')
#Practice for loops
topr=[1,4,9,16,25,36,49,64,81,100]
for getting in topr:
    print(getting)
numm=(1,4,9,16,25,36,49,64,81,100,49)
y=49
indexx=0
for valuee in numm:
    if (y==valuee):
        print('Number found at index',indexx)
    indexx+=1
for ell in range(1,101):
    print(ell)
for eell in range(100,0,-1):
    print(eell)
nu=int(input('enter number:'))
for table in range(1,11):
    print(str(nu)+' x '+str(table)+' = '+str(nu*table))
for esd in range(10):
    pass# 
#Calculate sum to n:
n=int(input('enter numers til you want sum:'))
s=0
i=1
while i<=n:
    s+=i
    i+=1
print('Total sum=',s)
nn=int(input('enter numers til you want sum:'))
s=0
for i in range(1,nn+1):
    s+=i
print('The sum is=',s)
#calculate factorial 
n=int(input('enter numers til you want factorial:'))
f=1
j=1
while j<=n:
    f=f*j
    j+=1
print('Factorial=',f)

nn=int(input('enter numers til you want factorial: '))
f=1
for j in range(1,nn+1):
    f=f*j
print('Factorial=',f)
