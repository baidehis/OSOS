total = 0.0

while True:
    numbers = input()
    
    if numbers == "0":
        break
    
    if numbers.replace(".", "", ).isdigit():
        total += float(numbers)
        print("The total is now", total)
    else:
        print("That was not a number.")

print("The grand total is", total)
