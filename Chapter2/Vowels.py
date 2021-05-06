vowels = ['a', 'e', 'i', 'o', 'u']

world = input("Podaj słowo, w którym należy wyszukać samogłoski: ")

found = []

for letter in world:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

