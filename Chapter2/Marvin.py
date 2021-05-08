paranoid_android = "Marvin, paranoid android"

letters = list(paranoid_android)

for char in letters[:6]:
    print("\t", char)
print("")
for char in letters[-7:]:
    print("\t"*2, char)
print("")
for char in letters[7:-8]:
    print("\t"*3, char)