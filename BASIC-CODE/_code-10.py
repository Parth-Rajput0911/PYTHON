# Write a program to Print prime numbers in a range.
num1=int(input("Enter the initial range:"))
num2=int(input("Enter the final range:"))
r=0
count=0

for i in range(num1,num2+1):
    if(i>1):
        for j in range(2,i):
            r=i%j
            if(r==0):
                count=count+1
                break
        if(count==0):
            print("The number",i,"is Prime number.")
        count=0
    elif(i<0):
        print("The negative number are not Prime number.")
    elif(i==0):
        print("The 0 is not a Prime number.")
    elif(i==1):
        print("The 1 is not a Prime number.")