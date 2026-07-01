# Write a program to Find product of digits
num=int(input("Enter the number:"))
temp=num 
product=1
if(num>0):
    while(temp!=0):
        product=product*(temp%10)
        temp=temp//10
    print("The Product of entered number is",product)
elif(num<0):
    temp=-num
    while(temp!=0):
        product=product*(temp%10)
        temp=temp//10
    print("The Product of entered number is",product)
else:
    print("The Product of entered number is 0")