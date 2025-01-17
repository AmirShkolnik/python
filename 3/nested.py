print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    print(age)
    if age <= 12:
        print("Your ticket cost $5.")
    elif age <= 18:
        print("Your ticket cost $7.")
    else:
        print("Your ticket cost $12.")
    print(input("Do you want photos? "))
else:
    print("Sorry you have to grow taller before you can ride.")