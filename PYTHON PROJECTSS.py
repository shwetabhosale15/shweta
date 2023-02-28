#MINI CALCULATOR :-
num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
print("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
choice=int(input("Enter your choice : "))
if  choice==1 :
    print("addition is : ", num1 + num2)
elif choice==2:
    print("subtraction is :",num1-num2)
elif choice==3:
    print("multipicaation is :",num1*num2)
elif choice==4:
    print("division is :",num1/num2)
else:
    print("Invalid number")


#CALENDAR DISPLAY
import calendar
year=int(input("Enter your year : "))
month=int(input("Enter your month : "))
x=calendar.month(year,month)
print(x)


#DICE -ROLL-SIMULATOR :-
import random
min_value=1
max_value=6
gamestart=input("if gamestart write ok : ")
if gamestart=="ok":
    print("ok.lets start")
    print(random.randint(min_value, max_value))
roll_again=input("roll again dic :")
if roll_again=="ok":
    print(random.randint(min_value, max_value))
    print("one  more last chance")
roll_again=input("roll again dic :")
if roll_again=="ok":
    print(random.randint(min_value, max_value))
    print("game over")


#TRANSOPE ARRAY:-
a=[[2,3,4],
   [4,5,6]]
b=[[0,0],
   [0,0],
   [0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for i in b:
    print(i)


#ADD TWO ARRAY:-
a=[[1,2],
   [2,3]]
b=[[1,2],
   [7,5]]
result=[[0, 0],
  [0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
for i in result:
    print(i)


#CHECK PALINDROME WORD :-
a=input("Enter your word : ")
reverse = a[ : : -1]
if a == reverse:
    print("it is palindrom word")
else:
    print("it is not palindrom word")


#REMOVE PUNCTUATION FROM GIVEN STRING:-
punctuation='''?/.,><'":;@!#$%^&*()_-[]{}|\~`+`='''
empty_string = ""
s=input("Enter anything : ")
for i in s:
    if i not in punctuation:
        empty_string+=i
print(empty_string)


a={1,2,3,5,6,7,9}
b={5,6,8,1}
c=a.union(b)
print("union values are : ", c)
d=a.intersection(b)
print("intersection values are : ", d)
e=a.difference(b)
print("difference values are : ",e)
f=a.symmetric_difference(b)
print("symmetric differnece values are : ",f)
g=set.copy(b)
print("b set copy values are : ",g)
h=a.isdisjoint(b)
print("a is different from b ? : ",h)
i=a.issubset(b)
print("a is subset of b ?  : ",i)
j=a.issuperset(b)
print("a is super set of b ?: ",j)
k=a.clear()
print("a set is clear " ,k)
print(a)


#ADD TWO NUMBERS :
user_input1 = int(input("Enter your first value : "))
user_input2 = int(input("Enter your  second value : "))
sum= (user_input1+user_input2)
print(sum)


#EMAIL VALIDATION USING RegEx :-
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{3,4}$"
user_input =input('Enter your email :')
if re.search(email_condition,user_input):
    print("Right email")
else:
    print("Wrong email")


#FIND SUQREROOT :-
user_input=int(input("Enter your value : "))
sqrt=user_input **(1/2)
print(sqrt)


import math
user_input=int(input("Enter your value : "))
sqrt=math.sqrt(user_input)
print("Your suqre root is here :", sqrt)


#FIND AREA OF TRIANGLE :-
Base=float(input("Enter your value : "))
Height=float(input("Enterr your value : "))
area=1/2 * Base * Height
print("Area of triangle is : " , area)


#SWAP TWO VARIBLES :-
x=50
y=80
temp_varible=x
print("value of temperary_variable is : " , temp_varible)
x=y
print("value of x is :" ,x)
y=temp_varible
print("value of y is : " ,y)


#SWAP TWO VARIBLES WITHOUT USING THIRD VARIBLE: -
x=10
y=50
x,y= y,x
print("value of x is : ", x)
print("value of y is : ",y)


#FIND RANDOM VALUE , CHARACHTER USING RANDOM MODULE
import random
num=random.randint(1,50)
print(num)

import random
mylist=["a","'b","c","d"]
print(random.choice(mylist))

import random
a="Hello world"
print(random.choice(a))


#CONVERT KILOMETER INTO MILES
1 KM = 0.621371 MILES
km=float(input("Enter your  km values : "))
miles = km * (0.621371)
print("Your",km," km convert into miles is here :",miles)


#FIND AREA OF CIRCLE AND CIRCUMFRENCE OF CIRCLE :-
r =float(input("Enter your radius value : "))
a= 3.14 * r * r
print("area of circle is :" ,a)

a=2 * 3.14 * r
print("Circumference of Circle is  :" ,a)


#FIND AREA OF SQUARE
user_input=float(input("Enter your value : "))
a=user_input * user_input
print("Area of squre is : ", a)


#FIND AREA OF RECTANGULRE :-
l=float(input("Enter your lenght value : "))
w=float(input("Enter your width value : "))
a=l*w
print("Area of rectanguler is : ", a)


#CONVERT CELCIUS INTO FERHRENHIT
#0 CELCUIS = 32 FERHRENHIT
#Formula use : (C *1.8) +32 = f
celcius=int(input("Enter your celcius value : "))
f = (celcius *1.8 ) + 32
print("Your Ferhrenhit is here : ", f)


#CHECK POSITIVE OR NEGATIVE NUMBER :-
num=int(input("Enter your value : "))
if num<0 :
    print("Your value is negavite")
elif num==0:
    print("your value is zero")
else:
    print("your value is positive")


#CHECK EVEN OR ODD NUMBER :-
num=int(input("Enter  your number : "))
if num%2==0 :
    print("Your number is even")
else:
    print(" your number is odd")


#CHECK LEAP YEAR
year=int(input("Enter your year : "))
if (year%400==0) and (year%100==0):
    print(" This is leap year")
elif (year%4==0) and (year%100!=0):
    print("This is leap year")
else:
    print("This is not leap year")


#CHECK LARGEST NUMBER:-
num1=20
num2=48
num3=87
if (num1>num2) and (num1>num3):
    print(num1,"num1 is large number")
elif (num2>num1) and (num2>num3):
    print(num2,"num2 is large number")
else:
    print(num3,"num3 is large number")


#FIND FACTORIAL :-
num=int(input("Enter your value : "))
fact=1
if num<0:
    print(" negative factorial does not exit")
if num==0:
    print("factorial of 0 is 1")
if num>0:
    for i in range(1 ,num+1):
        fact=fact * i
        print("Factorial of given number is here : ", fact)


#MULTIPLICATION TABLE:-
num=int(input("Enter your number : "))
for i in range(1,11):
    print(num,"*" ,i, "=", num*i)


#FIND NAUTURAL NUMBER :-
num= int(input("Enter your number : "))
if num<0:
    print("Please enter positive number")
else:
    sum=0
    while num>0:
        sum=num+sum
        num-=1
    print(sum)


#LAMBDA FUNCTION:-
y=lambda num : num ** 2
y(5)


#DECIMAL CONVERT INTO BINARY,OCTAL, HEXADECIMAL :-
decimal=int(input("Enter your decimal value : "))
print(bin(decimal))
print(oct(decimal))
print(hex(decimal))





