# Access List Item
List1 = [10, 20, 30, 40, 50, 60, 70]
print(List1)

# access the list items by index number.
List2 = [10, 20, 30, 40, 50, 60, 70]
print(List2[2])
print(List2[-1])
print(List2[0:3])
print(List2[:4])
print(List2[5:])

# CHANGE index VALUE
List3 = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
List3[4] = 'Item 6'
print(List3)

# FETCH VALUE WITH LOOP
List4 = [10, 20, 30, 40, 50, 60, 70]
for i in List4:
    print(i)

# CHECK VALUES N LIST WITH LOOP
a = ['Item 1', 'Item2' , 'Item 3', 'Item 4', 'Item 5', 'Item 6']
if 'Item2' in a:
    print("value available")
else:
    print("Value is not available")

# GET LENGTH OF LIST
List5 = [10, 20, 30, 40, 50, 60, 70]
print(len(List5))

# APPEND() METHOD
List6 = [10, 20, 30, 40, 50, 60, 70]
List6.append(100)
print(List6)

# Delete list item
list7 = [10, 20, 30, 40, 50, 60, 70, 80]
del list7[5]
print(list7)


# Delete list
list8 = [10, 20, 30, 40, 50, 60, 70, 80]
print(list8)
del list8


# concatinate two list
list9 = [1, 2, 3, 4, 5]
list10 = [6, 7, 8, 9, 10]
print(list9 + list10)

# Print ASCII Value of a character
i = 'A'
print('Tne ASCII value of A is' , ord(i) )


# Write a Python program to get the Python version
# you are using.
import sys
print("Python version")
print(sys.version)
print()

print("Version info.")
print(sys.version_info)

# Display the current date and time
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y %m %d %H : %M : %S"))

# Addition of Element at
# specific Position
# (using Insert Method)
List3 = [1 , 2 , 4 , 5 , 6 , 7 ,8]
List3.insert(3,3 )
List3.insert(0, 0)
print(List3)

# remove specific Position value
List3.remove(3)
print(List3)
List3.remove(0)
print(List3)
List3.pop(1)
print(List3)
