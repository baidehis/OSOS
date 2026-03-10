string = input()
characters = sorted(string, key=str.lower)
print("".join(characters))



print(sorted(string, key=str.lower))