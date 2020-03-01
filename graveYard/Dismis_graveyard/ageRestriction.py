# read in age
age = int(input("What's your age?"))

if age >= 18:
    print("Access allowed")
elif age < 18 and age > 0:
    print("Access not allowed")
else:
    print("Invalid age")