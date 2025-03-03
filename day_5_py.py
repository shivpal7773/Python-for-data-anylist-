# -*- coding: utf-8 -*-
"""Day-5 .py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SKs9sLdHMmNIRNSfaHbT-fRbPS1KvLFV

# **Loops and Types :-**

  A loop means to repeat something in the excet some way .

  Types of loops are :-

- 1. For loop
- 2. While loop
- 3. While true loop
- 4. Nested loop

- 1. For loop =>

  For loop is a loop that repeat something in a given range.

  The range has a starting point , ending point and a step/gap in it.

  +1 is added to ending point while defining a range .

       
        for (variable) in range (1,13):
            print(variable)("HELLO")



        for (var)in range (1,12,3[gap])
            print(var)
"""

n=12
for i in range(1,11):
  print(n,"x",i,"=",n*i)

n=int(input("Enter a number :"))
for i in range(1,11):
  print(n,"x",i,"=",n*i)

for i in range (0,11,2):
  print(i)

for i in range(1,11,2):
  print (i)

"""- 2. While loop =>
    
    While loop executes till the given condition is true .

    in while loop the increment is done inside the loop.

        
          while (condition):
                (Body of while)
                (increment)
          
"""

n=0
while n<=10:
  print(n)
  n=n+1

n=1
while n<=10:
  print(n)
  n+=2

n=0
i=7
while n<=10:
  print(n,"x",i,"=",n*i)
  n+=1

a=1
b=int(input("Enter a number :"))
while a<=10:
  print(b,"x",a,"=",b*a)
  a+=1

a=1
b=int(input("Enter a number :"))
while a<=10:
  print(b,"x",a,"=",b*a)
  a+=2

"""- 3. While true loop =>

    it is an infinite loop

    to break a while true loop . break is used .
"""

'''n=1
while True:
  print(n)
  n+=1'''

while True:
  num1=int(input("Enter a number :"))
  num2=int(input("Enter a number :"))

  print(num1+num2)

while True:
  num1=int(input("Enter a number :"))
  num2=int(input("Enter a number :"))

  print(num1+num2)

  user=input("Do you want to stop the program :")
  if user=="yes":
    break
  else:
    continue

"""- 4. Nested Loop =>

  A loop inside a loop is called as nested loop.

  Nested loops are also used to solve pattern problems .
"""

for i in range(1,5):
  for j in range (1,5):
    print(j,end=" ")
  print()

for i in range(1,6):
  for j in range (1,i+1):
    print(j,end=" ")
  print()

"""- 5. For loop with conditional statement =>

  The use o if-else statement increases the ability of for loop to completes the task effectively.

  By using if-else statement we can provide with special condition inside for loop.
"""

for i in range(1,50):
  if i%8==0 and i%12==0:
    print(i)

for i in range(1,11):
  if i==5:
    print("ADD TO FAVOURITE")
  else:
    print(i)

n=1

if n<=10:

  if n==3:

    print("ADD TO FAVOURITE")
  else:
    print(n)
  n+=1

"""- 6. Break and continue statement =>

  - Continue Statement :  it's used when you want to skip a particular condition .

  - Break Statement : It's used when you want to destroy a loop at a certain condition and come out of the loop .
"""

for i in range (1,11):
  if i==5:
    continue
  print(i)

for i in range (1,11):
  if i==5:
    break
  print(i)

"""# PROBLEM SOLVING :-

  - 1. Write a program to find a sum of all the even number up to 50 ?
"""

total=0
for i in range(1,51):
  if i%2==0:
    total=total+i
print("Total is :",total)

"""- 2. Write a program to write first 20 number and their squread number .?"""

for i in range (1,21):
  print(i,"=",i**2)

"""- 3. Write a program to find sum 10 odd number using while loop ?"""

sum = 0
n=0
while n<=20:
  if n%2!=0:
    sum+=n
  n+=1
print("The sum of first 10 odd numbers :",sum)

"""- 4. Write a program to check if a number is divisible by 8 and 10 1 to 100 number .?"""

for i in range(1,101):
  if i%8==0 and i%10==0:
    print(i)

