name = list(input("Give the name: "))
for i in range(1, len(name)):
    if name[i].isupper():
        name[i] = "_" + name[i].lower()
print("".join(name))
    