#ex1
list=[1,2,3,4,5]
for i in list:
    print(i+2)
    
#ex2
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
    
#ex3    
def rec(n):
    if n<=1:
        return n
    else:
        return(rec(n-1)+rec(n-2))
num=10
if num<=0:
    print("enter a positive number")
else:
    print("Fibonacci sequences")
    for i in range(num):
        print(rec(i))
       
#ex4      
A number is called armstrong number if it equal to sum of the cubes of its own digits
def armstrong(num):
    temp=num
    cube=0
    while(temp!=0):
        cube+=(temp%10)**3
        print("cube=",cube)
        temp//=10
    if cube==num:
        print("armstrong number")
    else:
        print("not an armstrong number")
    print()
armstrong(153)
armstrong(7)

#ex5
num=9
for i in range(1,11):
    print(num,'x',i,'=',num*i)

#ex6
n=int(input("Enter a number:"))
if n>0:
    print("positive")
else:
    print("negative")
    
#ex7
def age(days):
    years=days//365
    days=days%365
    months=days//30
    days=days%30
    print("you are",years,"years",months,"months",days,"days")
age(365*5+30*4+45)

#ex8
import math
print("sin 30+tan 30=",math.sin(math.radians(30))+math.tan(math.radians(30)))

#ex9
choice = int(input("Enter your choice:"))  
if (choice>=1 and choice<=4):
  print("Enter two numbers: ")
  num1 = int(input())
  num2 = int(input())

  if choice == 1:
      res = num1 + num2
      print("Result = ", res)
      
  elif choice == 2: 
      res = num1 - num2
      print("Result = ", res)
  
  elif choice == 3:
       res = num1 * num2
       print("Result = ", res)

  elif choice == 4:
      res = num1 / num2
      print("Result = ", res)

  elif choice == 5:
    exit()
else:
  print("Wrong input..!!")
