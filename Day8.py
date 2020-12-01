#ex1
print("SyntaxError:")
len("internship")=10
print("NameError:")
pqr
print("IndexError:")
l1=[1,2,3,4]
l1[5]
print("KeyError:")
dic={1:"name",2="class",3="std"}
dic[4]
print("IndentationError:")
if i>40
print(50)
print("TypeError:")
"88"+58
print("ImportError:")
from math import square
print("ValueError:")
int("Hi")
print("ModuleNotFoundError:")
import abcd

#ex2
n=int(input())
while n>0:
    if n==1:
        a=int(input())
        b=int(input())
        print(a+b)
    elif n==2:
        a=int(input())
        b=int(input())
        print(a-b)
    elif n==3:
        a=int(input())
        b=int(input())
        print(a*b)
    elif n==4:
        a=int(input())
        b=int(input())
        try:
            print(a/b)
        except:
            print()
            print(a,"can't be divided by zero")
        else:
            print("Invalid Input")
   
#ex3
try:
    print(a)
except NameError:
    print("x is not defined")
    
#ex4
Try-except is not required when there is no runtime error

#ex5
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisonError:
    print(a,"can't be divided by zero")
  
