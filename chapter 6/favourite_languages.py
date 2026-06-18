# #A DICTIONARY OF SIMILAR OBJECTS
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'rust',
#  'phil': 'python',
#  }

# # language = favorite_languages['sarah'].title()
# # print(f"Sarah's favorite language is {language}.")

# #LOOPING THROUGH ALL KEY VALUE PAIRS

# for name, language in favorite_languages.items():
#     print(f"(name.title())'s favourite language is (language.title()).")

# for name in favorite_languages:
#     print(name.title())

# #LOOPING THROUGH DICTIONARY TO ACCESS VALUES

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         languages = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if "erin" not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# #LOOPING THROUGH KEYS IN PARTICULAR ORDER

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll")

# #LOOPING THROUGH VALUES IN THE DICTIONARY

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#  print

favorite_languages = {
 'jen': ['python', 'rust'],
 'sarah': ['c'],
 'edward': ['rust', 'go'],
 'phil': ['python', 'haskell'],
 }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

