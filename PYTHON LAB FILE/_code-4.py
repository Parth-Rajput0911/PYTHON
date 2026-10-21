# Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\nOdd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")