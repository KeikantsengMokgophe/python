# NUMERICAL COMPARISONS
# age = 18
# age == 18




# answer = 17
# if answer != 42:
#     print("That is not the correct answer. please try again!")


# age = 19
# print(age < 21)
# print(age <= 21)
# print(age > 21)
# print(age >= 21)

# USING AND TO CHECK MULTIPLE CONDITIONS

from pickle import LIST


age_0 = 22
# age_1 = 18

# print(age_0 >= 21 and age_1 >= 21)

# AGE_1 = 22
# print(age_0 >= 21 and AGE_1 >= 21)

# USING OR TO CHECK MULTIPLE CONDITIONS
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)

# age_0 = 18
# print(age_0 >= 21 or age_1 >= 21)

# CHECKING WHETHER A VALUE IS IN A LIST

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

# CHECKING WHETHER A VALUE IS NOT IN A LIST
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")