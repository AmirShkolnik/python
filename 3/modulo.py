number_to_check = int(input("What is the number you want to check? "))
number = number_to_check % 2

if number == 0:
    print("Even")
else:
    print("Odd")