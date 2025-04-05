#Lists
marks=[92,99,93.4,67,88,76,97,83,64]
print(marks)
student=['Musaddiqa','20','Karachi']
print(student)
student[1]=21
print(student)
print(marks[0:4])
print(marks[-4:len(marks)])
marks.append(95)
print(marks)
list=[2,3,1,4,3,5,3,5,6,7]
list.remove(3)
print(list)

movie_list=[]
movie_list.append(input('enter first one:'))
movie_list.append(input('enter second one:'))
movie_list.append(input('enter third one:'))
print(movie_list)

list1=[1,2,3,4,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
print(copy_list1)
if list1==copy_list1:
    print('Palindrome')
else:
    print('Not Palindrome')

lst=[1,2,1]
copylist=lst.copy()
print(copylist)
rev=list(reversed(copylist))
print(rev)
if lst==rev:
    print("palindrome")
else:
    print("not Palindrome")

lst = [1,2,3,4,3,2,1] 
copylist=lst.copy() 
rev=[] 
while copylist:
    rev.append(copylist.pop())  

if lst==rev:
    print("palindrome")
else:
    print("not Palindrome")

#Tuples
tup=('C','D','A','A','B','B','A')
print(tup.count('A'))

lst=['C','D','A','A','B','B','A']
lst.sort()
print(lst)

#Sets
set1={1,2,3,4,5,5,5,5,'hello',2.9,(1,'hi')}
print(set1,len(set1),type(set1))  ##set ignores duplicate values
set1.add(78)
set1.remove(1)
print(set1)
set1.clear()  ##do set clear
print(set1)
set2={1,2,3,'hello','hi','you','me','they'}
print(set2.pop())  ##remove random element from set and give
print(set2)  #removed pop element can see here
set3={1,2,3,4,5,6,7}
set4={6,7,8,9,10}
print(set3.union(set4))
print(set3.intersection(set4)) 

#practice more
neww={'table':["a piece of furniture","list of facts and figure"],'cat':'a small animal'}
print(neww)
print(neww.get('table'))
#To count the number of classrooms(each subject requires seperate classroom)
countt={'python','java','c++','python','javascript','java','python','java','c++','c'}
number_of_classrooms=len(countt)
print(number_of_classrooms) 

# marks={}
phy=int(input('enter phy marks:'))
chem=int(input('enter chem marks:'))
maths=int(input('enter maths marks:'))
marks.update({'physics':phy})
marks.update({'chemistry':chem})
marks.update({'maths':maths})
print(marks)

sett={1,3,9,'9.0'}
print(sett)
settt={('int',9),('float',9.0)}
print(settt)
