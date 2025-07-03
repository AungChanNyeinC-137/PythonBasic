favorite_languages = {
 'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# for name, language in favorite_languages.items():
#     print(name.title()+"'s favorite language is " + language)

# # for name in favorite_languages.keys():
# #     print(name.title())
friends = ['sarah','phil']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}")
#     if 'erin' not in favorite_languages.keys():
#         print("Hi Erin please take the poll")

#Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}")
if 'erin' not in favorite_languages.keys():
        print("Hi Erin please take the poll")