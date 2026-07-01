# Write a program to Find factorial of a number.
num=int(input("Enter the number:"))
fact=1
if (num==0 or num==1):
    print("The Factorial of entered number is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The Factorial of entered number is",fact)