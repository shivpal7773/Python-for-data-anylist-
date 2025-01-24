# -*- coding: utf-8 -*-
"""Day 6 .py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jPZXbGKfvcxYGFxEPnFhPRzBFA98rOJi

# **BILLING CALCULATER :-**

Write a program to create a billing system at supermarket ?
"""

while True:
    customer = input("Enter customer name: ")
    total = 0
    while True:
        print("**** Enter the amount and quantity ****")
        amount = float(input("Enter item amount: "))
        quantity = float(input("Enter item quantity: "))
        total += amount * quantity

        repeat = input("Do you want to add more items? (yes/no): ").strip().lower()
        if repeat != "yes" and repeat != "y":
            break

    print("*" * 40)
    print("Name:", customer)
    print("Total amount:", total)
    print("*" * 40)
    print("****** HAPPY SHOPPING *****")

    repeat1 = input("Do you want to go to the next customer? (yes/no): ").strip().lower()
    if repeat1 == "no":
        break

"""# PROBLEM SOLVING :-

  " Why Fit in when yoou are born to out !"

  - 1. Write a program to find the length of the following string .
  - 2. Write a program to check how many time alphabat o is occuring .
  - 3. write a program to convert the whole string into lower and upper case .
  - 4. Write a program to convert the followning string into a title .
  - 5. Write a program to find the index number of "Fit in " .
"""

a=" Why Fit in when yoou are born to out !"
print(len(a))

print(a.count("o"))

print(a.upper())

print(a.title())

print(a.find("Fit in"))

"""# PATTERNS PROBLEMS :-

    
"""

for i in range (1,6):
  for j in range (1,6):
    print(j,end=" ")
  print()

for i in range (1,6):
  for j in range (1,i+1):
    print(j,end=" ")
  print()

for i in range (1,6):
  for j in range (1,6):
    print(i,end=" ")
  print()

for i in range (1,6):
  for j in range (1,i+1):
    print(i,end=" ")
  print()

for i in range (1,6):
  for j in range (1,6):
    print("*",end=" ")
  print()

for i in range (1,6):
  for j in range (1,i+1):
    print("*",end=" ")
  print()

for i in range (6,0,-1):
  for j in range (1,i+1):
    print("*",end=" ")
  print()

for i in range (7,0,-1):
  for j in range (1,i+1):
    print(j,end=" ")
  print()

for i in range (6,0,-1):
  for j in range (1,i+1):
    print(i,end=" ")
  print()

for i in range (1,6):
  for j in range (5,i,-1):
    print(" ",end=" ")
  for k in range (i):
    print("*",end=" ")
  print()

for i in range (1,6):
  for j in range (6,i,-1):
    print(j,end=" ")
  print()

for i in range (1,6):
  for j in range (5,i,-1):
    print(" ",end=" ")
  for k in range (i):
    print(i,end=" ")
  print()

for i in range (1,6):
  for j in range (i,0,-1):
    print(j,end=" ")
  print()

for i in range (1,6):
  for j in range (1,i+1):
    print(j,end=" ")
  for k in range (5,i,-1):
    print(" ",end=" ")
  for l in range (1,i+1):
    print(l,end=" ")
  print()

for i in range (1,6):
  for j in range (1,i+1):
    print("*",end=" ")
  print()
for i in range (6,0,-1):
  for j in range (1,i+1):
    print("*",end=" ")
  print()

for i in range (1,11):
  for j in range (1,i+1):
    print(i*j,end=" ")
  print()

