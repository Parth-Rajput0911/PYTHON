# Write a program to Find sum of digits of a number.
num=int(input("Enter the number:"))
sum=0
temp=num
if(num>0):
    while(temp!=0):
        sum=sum+temp%10
        temp=temp//10
    print("The Sum of digit of entered number is",sum) 
elif(num<0):
    temp=-num
    while(temp!=0):
        sum=sum+temp%10
        temp=temp//10
    print("The Sum of digit of entered number is",sum) 
else:
    print("The Sum of digit of entered number is 0")


