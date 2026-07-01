# Write a program to Check whether a number is palindrome.
num=int(input("Enter the number:"))
temp=num
reverse=0
if(num>0):
    while(temp!=0):
        reverse=(reverse*10)+temp%10
        temp=temp//10
    if(num==reverse):
        print("The number is Palindrome.")
    else:
        print("The number is not a Palindrome.")
elif(num<0):
    print("The negative number is not a Palindrome.")
elif(num==0):
    print("The number is Palindrome.")