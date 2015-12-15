#!/usr/bin/python3

favorite_languages = {
  'jen':'python',
  'sarah':'c',
  'edward':'ruby',
  'phil':'python',
  }

for name, language in sorted(favorite_languages.items()):
    print(name.title() + "'s favorite language is " +
      language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah','erin']

for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + 
          ", I see your favorite language is " +
          favorite_languages[name].title() + "!")

for friend in friends:
    if friend not in favorite_languages.keys():
        print( friend.title() + ", please take our poll!")

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
  'jen': ['python','ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell'],
  }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")

    for language in languages:
        print("\t" + language.title())



