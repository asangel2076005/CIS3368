user_data = input()
user_data = user_data.split(" ")

user_data_int = []
for number in user_data:
    user_data_int.append(int(number))
user_data.clear()

user_data_positive = []
for number in user_data_int:
    if number > -1:
        user_data_positive.append(number)
user_data_int.clear()
user_data_positive.sort()

for i in user_data_positive:
    print(f"{i}", end=" ")
