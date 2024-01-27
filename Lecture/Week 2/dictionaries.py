# Dictionaries
my_dict = {
    "first_name": "Jane",
    "last_name": "Doe",
    "birth_year": 2001
}

print(my_dict)
print()

# Ways to get dictionary values
print(my_dict["first_name"])

first_name = my_dict.get("first_name")
print(first_name)
print()

# Reassignment
my_dict = {
    "first_name": "Jane",
    "last_name": "Doe",
    "birth_year": 2001,
    "children": ["Jack", "John", "James"]
}

print(my_dict)
print(my_dict["children"][0])
print()

# Note: the old my_dict object is garbage collected since it is reassigned by a new my_dict object

# Updating dictionaries
my_dict["birth_year"] = 2000
print(my_dict)

my_dict.update({"birth_year": 1900})
print(my_dict)

if "children" in my_dict:
    print("This person has children")
print()

# Update / Add non-existent items in dictionaries
my_dict["father"] = "Jeff"
print(my_dict)
print()
# Note: If it doesn't exist, adds. If it exists, updates it

# Note: Python's dynamic behavior forces it to have a lot of overhead which makes it slower

# Removing dictionary items
my_dict.pop("father")
print(my_dict)

my_dict["father"] = "Jeff"
del my_dict["father"]
print(my_dict)
print()

# Clearing a dictionary
my_dict.clear()
print(my_dict)
print()

# Note: Clearing a dictionary serves a purpose of reusing a dictionary in different instances
# Adds another purpose for reusability
