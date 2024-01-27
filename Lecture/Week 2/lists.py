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

# Updating List items
my_list[1] = 500
print(my_list)
print()

# Inserting an item to list
my_list.insert(2, "Totally unrelated string")
print(my_list)
print()

# Adding an item to the end of the list
my_list.append("YELLOW")
print(my_list)
print()

# Adding 2 lists. This fuses both lists
more_colors = ["red", "blue", "green"]
my_list.extend(more_colors)
print(my_list)
print()

# Removing List items
my_list.pop(0)  # Remove items at index
print(my_list)
print()

del my_list[-10]  # Delete last item
print(my_list)
print()

# Iterating over a list
for item in my_list:
    print(item)
print()
# Everytime an iteration is rerouted, the previous variable referencing the previous object gets
# into the Garbage collector

# Sorting lists
# my_list.sort()
# Note: Only lists with the one data type can use this method, otherwise a TypeError will show

colors = ["red", "orange", "blue", "green", "black"]
print(my_list)
colors.sort()
print(colors)
print()

# Clearing a list to free up some memory or reuse a list name
my_list.clear()
