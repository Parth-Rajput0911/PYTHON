# Write a program to Check whether a number is prime.
num=int(input("Enter the number:"))
count=0
r=0
if(num>1):
    for i in range(2,num):
        r=num%i
        if(r==0):
            count=count+1
            break
    if(count>0):
        print("The number is not a Prime.")
    else:
        print("The number is a Prime.")
elif(num<0):
    print("The negative number are not Prime number.")
else:
    print("The number is not a Prime.")
