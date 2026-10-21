# String operations
s = "Python Programming"
print(s)
print("String operations")
# 1. Case conversion
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print("hello".casefold())
# 2. Searching and counting
print(s.find("python"))
print(s.rfind("python"))
print(s.index("programming"))
print(s.count("python"))
print(s.startswith("python"))
print(s.endswith("python"))
# 3. Replacing and splitting
print(s.replace("python", "orange"))
print(s.split(","))
print(s.rsplit(",", 1))
# 4. Checking string contents
print("s".isalpha())
print("s".isdigit())
print("s".isalnum())
print("s".islower())
print("s".isupper())
print("s".istitle())
print("s".isspace())
print("s".isdecimal())
print("s".isnumeric())
print("s".isidentifier())
print("s".isascii())
print("s".isprintable())

# List operations

a = [10, 20, 30, 20, 40]
print("Original List:", a)
print("List operations")
# 1. Basic Operations
print("Length:", len(a))
print("First Element:", a[0])
print("Last Element:", a[-1])
print("Slicing:", a[1:4])
print("Reverse Slicing:", a[::-1])
# 2. Append
a.append(50)
print("After Append:", a)
# 3. Extend
a.extend([60, 70])
print("After Extend:", a)
# 4. Insert
a.insert(1, 15)
print("After Insert:", a)
# 5. Remove
a.remove(20)
print("After Remove:", a)
# 6. Pop
x = a.pop()
print("Popped Element:", x)
print("After Pop:", a)
# 7. Index
print("Index of 30:", a.index(30))
# 8. Count
print("Count of 20:", a.count(20))
# 9. Sort
a.sort()
print("Ascending Order:", a)
a.sort(reverse=True)
print("Descending Order:", a)
# 10. Reverse
a.reverse()
print("After Reverse:", a)
# 11. Copy
b = a.copy()
print("Copied List:", b)
# 12. Concatenation
print("Concatenation:", a + [80, 90])
# 13. Repetition
print("Repetition:", [1, 2] * 3)
# 14. Membership
print("30 in List:", 30 in a)
print("100 not in List:", 100 not in a)
# 15. Built-in Functions
print("Minimum:", min(a))
print("Maximum:", max(a))
print("Sum:", sum(a))
print("Length:", len(a))
print("Sorted List:", sorted(a))
# 16. Update Element
a[0] = 100
print("After Updating:", a)
# 17. Delete Element
del a[0]
print("After Deletion:", a)
# 18. Clear List
b.clear()
print("After Clear:", b)
# 19. List Comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)
# 20. Any and All
print("Any:", any(a))
print("All:", all(a))

# Tuple operations

# 1. Creating a Tuple
t = (10, 20, 30, 20, 40)
print("Original Tuple:", t)
print("Tuple operations")
# 2. Length
print("Length:", len(t))
# 3. Indexing
print("First Element:", t[0])
print("Last Element:", t[-1])
# 4. Slicing
print("Slicing:", t[1:4])
print("Reverse Tuple:", t[::-1])
# 5. Concatenation
print("Concatenation:", t + (50, 60))
# 6. Repetition
print("Repetition:", (1, 2) * 3)
# 7. Membership
print("20 in Tuple:", 20 in t)
print("100 not in Tuple:", 100 not in t)
# 8. Count
print("Count of 20:", t.count(20))
# 9. Index
print("Index of 30:", t.index(30))
# 10. Built-in Functions
print("Minimum:", min(t))
print("Maximum:", max(t))
print("Sum:", sum(t))
print("Length:", len(t))
print("Sorted Tuple:", sorted(t))
# 11. Tuple Comparison
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print("Tuples Equal:", t1 == t2)
# 12. Tuple Unpacking
a, b, c = (100, 200, 300)
print("a =", a)
print("b =", b)
print("c =", c)
# 13. Convert List into Tuple
lst = [1, 2, 3, 4]
new_tuple = tuple(lst)
print("List to Tuple:", new_tuple)
# 14. Convert Tuple into List
new_list = list(t)
print("Tuple to List:", new_list)
# 15. Any and All
print("Any:", any(t))
print("All:", all(t))
# 16. Single Element Tuple
single = (10,)
print("Single Element Tuple:", single)
# 17. Empty Tuple
empty = ()
print("Empty Tuple:", empty)
