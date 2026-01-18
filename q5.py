s = input()
count = 0
for characters in s:
    if characters in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)
