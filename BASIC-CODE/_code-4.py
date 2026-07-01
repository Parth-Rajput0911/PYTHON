# Write a program to Count digits in a number.
num=int(input("Enter the number:"))
count=0
temp=num
if(num==0):
    print("The Total digit in entered number is 1")
elif(num<0):
    temp=-num
    while(temp!=0):
        if(temp!=0):
            count=count+1
            temp=temp//10 
    print("The Total digit in entered number is",count)
else:
    while(temp!=0):
        if(temp!=0):
            count=count+1
            temp=temp//10 
    print("The Total digit in entered number is",count)
