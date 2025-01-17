print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill = 15
    print(f"Your pizza cost: ${bill}")
if size == "M":
    bill = 20
    print(f"Your pizza cost: ${bill}")
if size == "L":
    bill = 25
    print(f"Your pizza cost: ${bill}")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
else:
    print(f"Your final bill is: ${bill}")