weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = float(weight / (height ** 2))
print(type(bmi))
print(f"Your bmi score is: {bmi:.2f}")


if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 25:
        print ("normal weight")
else:
    print("overweight")