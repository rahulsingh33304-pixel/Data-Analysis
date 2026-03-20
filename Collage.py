# Flat case 
myname  = "myname"
# snake case 
my_name_class = "xyx"
# camel case 
myName = "xyz"
# Pascal case 
MyName = "xyz"
x= 12 #interger
print(type(x))


age = int(input("enter your age :"))
if age < 13:
    print("you are a child.")
elif age < 20:
    print("you are a  Teen ager.")
elif age <60:
    print("you are an Adult")
else:
    print("you are a  senior citizen:")

#tuples are not changeable
    #tuples are always start from().
my_tuple = (1,2,3) #simple tuple 
my_typle = (2,"hello",3)
my_tuple = (5,) #single tuple
print(my_tuple)

my_tuple = (2,"hello",3)
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

#tuples Operations 
a = (2,4)
b = (10,30)
#concationation
print(a+b)
#repetation
print(a*4)

a =("It's  a rainy day \n you are a Bad man") #\n new for new line
print(a)

a =  ("it's a rainy day \tyou are a Bad man") #\tfor space 
print(a )

a = ("it's a rainy day  you are  a Bad man")  #for length of neew line
print(a)

a = "1"
b = "3"
print(a+b)
x = "Rahul"
print(x*5)

a = ("it's a rainy day  you are a Bad man") #indexing string
print(a[-11])

a = ("it's a rainy day you are a Bad man")  #slicing string
print(a[6:-11])

a =("it's a rainy day  you are a Bad man")  #member string
print("a"in 'rainy')

a =("it's a rainy day  you are a Bad man")  #lower case string
print(a.lower())

a = ("its a rainy day   you are a Bad man") #upper case string
print(a.upper())

a = ("it's a rainy day  you are a Bad man")  #strip string
print(a.strip())

a=(" 'Hello world' ") 
print(a.strip())


a=("it's a rainy day  you are a Bad man")  #capitalize string
print(a.capitalize())

a=("it's a rainy day  you are a Bad man")  #title string
print(a.title())


text = "   Hello World   "
print(text.strip())

a=("it's a rainy day  you are a Bad man")  #replace string
print(a.replace('Ba','goo'))

a=(" it's a rainy day   you are a Bad man")  # find string
print(a.find('r'))

a=(" it's a rainy day  you ar aa Bad man ")   #if the characcter is not int he sentence it will show  -1
print(a.find('h'))

a=(" it's a rainy day  you are a Bad man")   #count string
print(a.count('a'))

a=("it's a rainy day  yu are  a Bad man ")  #startswith
print(a.startswith("a"))

a=("it's a  rainy day  you are a Bad man")  #lstrip strinng
print(a.lstrip("a").startswith("a"))

a=("its a rainy day  you are a Bad man")
print(a.rstrip().startswith("i"))

a=("its a rainy day you are a Bad man")
print(a.rstrip().startswith(" "))

you= "you are a person of Aura"  #split (seperate words from a sentence)
me = you.split()
print(me)


Flat case 
myname  = "myname"
# snake case 
my_name_class = "xyx"
# camel case 
myName = "xyz"
# Pascal case 
MyName = "xyz"
x= 12 #interger
print(type(x))


age = int(input("enter your age :"))
if age < 13:
    print("you are a child.")
elif age < 20:
    print("you are a  Teen ager.")
elif age <60:
    print("you are an Adult")
else:
    print("you are a  senior citizen:")

# tuples are not changeable
tuples are alwayys start from().
my_tuple = (1,2,3) #simple tuple 
my_typle = (2,"hello",3)
my_tuple = (5,) #single tuple
print(my_tuple)

my_tuple = (2,"hello",3)
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

tuples Operations 
a = (2,4)
b = (10,30)
#concationation
print(a+b)
#repetation
print(a*4)

a =("It's  a rainy day \n you are a Bad man") #\n new for new line
print(a)

a =  ("it's a rainy day \tyou are a Bad man") #\tfor space 
print(a )

a = ("it's a rainy day  you are  a Bad man")  #for length of neew line
print(a)

a = "1"
b = "3"
print(a+b)

print("Hello 😊")
print("I love Python 🐍🔥")
print("\U0001F600")  # 😀
print("\U0001F60D")  # 😍
print("\U0001F680")  # 🚀
import emoji

print(emoji.emojize("Python is fun :smiling_face_with_heart_eyes:"))
print(emoji.emojize("Let's code :rocket:"))
import emoji

print(emoji.emojize("Python is fun :smiling_face_with_heart_eyes:"))
print(emoji.emojize("Let's code :rocket:"))
import emoji

text = "I love coding :fire:"
print(emoji.emojize(text))

#1. if statement 
x= 1
if x>5:
    print("x is greater than 5")
else:
    print("x is lessthan 5")
#2. if -else statement
    age =16
    if age >=18:
        print("you can vote ")
    else:
        print("You cannot vote")
#3.if elif else  Statement
    marks = int(input("enter your marks : "))
    if marks >= 90:
        print("Grade: A+")
    elif marks >=75:
        print("Grade: A")
    elif marks >=60:
        print("Grade : B")
    
    else :
        print("Grade : c")
#4. Nested if 
num = 19
if num >0:
    if num%2==0:
        print("Positive Even number")
    else:
        print("Positive odd Number")
else:
    
        print("number is Nagative")

#5. short hand if 
x = 10
if x>10:
     print("x is grater than 10")
else:
    print("x is less than 10")
check the number any number in short hand if
x = int(input("enter your number "))
if x>100:
    print("x is greater than 100")
else:
    print("x is lesst than of 100")

6. short hand if else (Tenary Operator)
a,b = 10,20
print("a is grater ")
if a>b:
     
#      print("b is greater")

num1 = float(input("Enter first number; ") )
num2 = float(input("Enter second number: "))
operation= input("chose operation(+,-,*,/):")
if operation =="+":
    print("result:",num1+num2)
elif operation == "-":
    print("result:",num1-num2)
elif operation =="*":
    print("result:",num1*num2)
elif operation == "/":
    if num2 !=0:
          print("result:",num1/num2)
    else:
        print("Invaild Operation")

              
#traffic light
light = input ("Enter traffic light color (red,yellow ,green):")
if light == "red":
    print("stop")
elif light == "yellow":
    print("Get Ready")
elif light == "green":
    print("go")
else:
    print("Invalid light color!")

#1. for loop
for i in range(5):
    print("Hello",i)

#2. while loop
count = 1
while count<= 5:
    print("Hello",count)
    count += 1
    
#3. loop control - break - exixt loop immediately
 #coutinue - skip current itrertion 
 #pass - do nothing (placeholder)
for i in range(1,6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

#loop indide another loop.
for i in range(2):
    for j in range(3):
        print("i=",i,"j=",j)

summery:
for loop - repeat over sequence
while loop - repeat while condition true
break, continye,pass ,control

#loops
 it = iter([1,2,3])
print(next(it))  #1
print(next(2))  # 2
print(next(it)) 

Q.1. print number from 1 to 10 using a for loop.
q2. print number from down fto 1 using a while loop.
Q3. print the multiplication table of 5 using a for loop
Q4. write a program that prints only even numbers between 1 and 20 using a while loop 
Q5. print a pattern using a nessted for loop.

#ans 1.
for i in range(1,10):
    print(i)

    #Ans 2,
num = 10
while num >= 1:
    print(num)
    num -=1

#ans 3. 
for i in range(1,11):
    print(f"5 x {i} = {5*i}")

#Ans 4.
num = 2
while num <=20:
    print(num)
    num +=2

#Ans 5.
rows = 10
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
        print()

#Q 6. print the multiplication table of 6 using for loop.
 #ans 6.
for i in range(1,11):
    print(f"6 x {i} = {6*i}")

#PANDS DATA FRAM : THE STRUCTED DATTA 
#CREATE DATA FRAME
import pandas as  pd 
df = pd.DataFrame([1,2,3],columns = ['column_name'])
print(df)

import pandas as pd

data = {
    "Name": ["Rahul", "Aman"],
    "Age": [20, 22],
    "Section":["A","A",]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd
abc = {
    'name' : ['rahul','aman','preeti','moti','sadhana'],
    'age' : [18,14,19,23,17],
    'salary' : [20000000,344444,555555,56666,77777777],
    'education' : ['btech','bca','ba','bcom','bba']
}
df =pd.DataFrame(abc)
print(df)
#basic DataFrame understsanding 
print(df.head(3)) #top rows by deafault 5 top rows

import pandas as pd
data = {
    'name' : ['abhi','rahul','om','jai','sadhna','moti'],
    'age' : ['14','25','19','20','12','18'],
    'salary' : ['1233333','555555','6000000','666666','55333','335555'],
    'education' : ['ba','bca','btech','bcom','bba','d pharama']
}
df= pd.DataFrame(data)
print(df)
print(df.head(4))   # top rows by deafault 6
print(df.tail(3))  # down rows by deafault 6 down rows

import pandas as pd
data = {
    'name' : ['abhi','rahul','om','jai','sadhna','moti'],
    'age' : ['14','25','19','20','12','18'],
    'salary' : ['1233333','555555','6000000','666666','55333','335555'],
    'education' : ['ba','bca','btech','bcom','bba','d pharama']
}
df= pd.DataFrame(data)
df.shape

import pandas as pd

data = {
    'name': ['abhi','rahul','om','jai','sadhna','moti'],
    'age': ['14','25','19','20','12','18'],
    'salary': ['1233333','555555','6000000','666666','55333','335555'],
    'education': ['ba','bca','btech','bcom','bba','d pharama']
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
df = df.rename(columns={'salary' : 'payment'})
df.rename(columns={'salary','payment'},inplace=True)
# print(df)
df.describe() #for stastical summary
print(df)

Q. create  a com. where you have name,employee id, age,salary,doj, min = 15 rows

import pandas as pd
data = {
    'namr': ['preeti','rah','raj','om','moti','golu','rohit','mohan','ram','sohan','sonu','ronney','sohit','bholu','sita'],
    'employee' : ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
    'age' : ['23','13','34','45','45','23','24','24','25','26','19','20','12','27','29','30'],
    'salary': [25000,30000,28000,27000,35000,22000,40000,38000,42000,26000,
               45000,32000,47000,29000,3600],

    'doj': ['2022-01-10','2021-03-15','2023-06-20','2022-09-05','2020-12-11',
            '2023-02-18','2019-07-25','2021-11-30','2018-05-14','2022-08-19',
            '2017-10-01','2020-04-22','2016-06-17','2021-01-09','2019-03-03']
               

}
df = pd.DataFrame(data)
print(pd)
import pandas as pd

data = {
    'name': ['Rahul','Aman','Neha','Riya','Karan','Pooja','Vikas','Anjali','Rohit','Simran',
             'Arjun','Meena','Suresh','Kavita','Deepak'],
    
    'emp_id': [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    
    'age': [22,25,23,24,26,21,28,27,29,22,30,26,31,24,27],
    
    'salary': [25000,30000,28000,27000,35000,22000,40000,38000,42000,26000,
               45000,32000,47000,29000,36000],
    
    'doj': ['2022-01-10','2021-03-15','2023-06-20','2022-09-05','2020-12-11',
            '2023-02-18','2019-07-25','2021-11-30','2018-05-14','2022-08-19',
            '2017-10-01','2020-04-22','2016-06-17','2021-01-09','2019-03-03']
}

df = pd.DataFrame(data)
df.to_csv('new_data.csv', index=False)
# print(df)
df = pd.read_csv('new_data.csv')
print(df)
# pd.read_csv('new_data.csv',index=False)  #to remove index number

df.loc[(df.name=='abhishek')]

import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Neha', 'Sita'],
    'Age': [20, 21, 19, 22],
    'Salary': [20000, 25000, 18000, 30000]
}

df = pd.DataFrame(data)
print(df)
print(df.iloc[0:3]) #*last value never be include in iloc
print(df.loc[3]) #  this use for the to find the specific point ,value, in the give chart
print(df[df['age'] >=34]) #this use for the to replace the word in the given sentence
print(df['age'] >= 20)
print(df.where(df['age'] >=24))
df.where(df['age'] >= 24)
import pandas as pd

data = {
    'name': ['Rahul','Amit','Neha'],
    'age': [18, 25, 20]
}

df = pd.DataFrame(data)

print(df.where(df['age'] >= 24))
#add ne columns
df['Team'] = ['ceo','cto','accountant']


import pandas as pd

data = {
    'Name': ['Rahul','Amit','Neha','Sita','Ravi',
             'Kiran','Pooja','Arjun','Priya','Vikas',
             'Anjali','Rohit','Sneha','Manoj','Kavita'],
    
    'Age': [20, 21, 19, 22, 23,
            24, 20, 25, 21, 22,
            23, 24, 19, 26, 20],
    
    'Salary': [20000, 25000, 18000, 30000, 27000,
               32000, 21000, 35000, 26000, 28000,
               29000, 31000, 19000, 36000, 22000]
}

df = pd.DataFrame(data)


df['Bonus'] = df['payment']*0.2
print(df)
print(len(df))

print(df.loc[6,'payment'])
df.drop(df[df.name=='xyz'].index)   #drop row axis

df.drop('Bouns',axis=1)

df['Bonus'] = df['Salary'] * 0.10

print("Before Drop:")
print(df)

# Drop Bonus Column
df = df.drop('Bonus', axis=1)

print("\nAfter Drop:")
print(df)

df.drop('Bouns')