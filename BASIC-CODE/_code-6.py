# Write a program to Reverse a number.
num=int(input("Enter the number:"))
temp=num
reverse=0
if(num>0):
    while(temp!=0):
        reverse=(reverse*10)+temp%10
        temp=temp//10
    print("The Reverse of entered number is",reverse)
elif(num<0):
    temp=-num
    while(temp!=0):
        reverse=(reverse*10)+temp%10
        temp=temp//10
    print("The Reverse of entered number is-",reverse)
else:
    print("The Reverse of entered number is 0")




