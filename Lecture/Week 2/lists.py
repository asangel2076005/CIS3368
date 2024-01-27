# Lists
# they are ordered, changeable, allow duplications and multiple data types

my_list = ["apple", "kiwi", "pear"]
print(my_list)
print()

# Reassigning
my_list = ["apple", "kiwi", "pear", "apple", "apple"]
print(my_list)
print()
# In this case, the old my_list is garbage collected and replaced by the new my_list

# count the list item amount
list_length = len(my_list)
print(list_length)
print()

# Data types in lists
my_list = [100, 15, 77, 99, 300]
print(my_list)

my_list = [True, False, True]
print(my_list)

my_list = ["Apple", 300, True, 400, "Alex", [1, 3, 5, 7, 9]]
print(my_list)
print()
# In conclusion, lists can contain many data types but has overhead

# Accessing List items
print(my_list[1])
print(my_list[-1])
print()
# Negative index references item starting from the end of the list
# Do not use this if using Python with other languages

# List Slice Notation
print(my_list[2:5])
print()
# The second number in the slice notation is exclusive (not part of the executed code)

print(my_list[:5])
print()
# In this case, slice notation begins from the start to the end (exclusive)

# Checking if items exists in a list
if "Alex" in my_list:
    print("Alex is part of the list")
else:
    print("Alex isn't here somewhere")
print()

if "Monica" in my_list:
    print("Monica is here")
else:
    print("Monica is nowhere to be seen in this list")
print()
