# Write a program to Calculate sum of first N natural numbers.
num=int(input("Enter the number till sum calculated:"))
sum=0
if (num==0):
    print("The sum of number is 0")
elif(num==1):
    print("The sum of number is 1")
else:
    for i in range (num+1):
        sum+=i
    print("The sum of number is",sum)
