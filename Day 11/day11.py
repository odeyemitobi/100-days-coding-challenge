h = float(input("Input ur height (in meters e.g: 1.67): "))
w = int(input("Input your weight (In kilograms e.g: 50): "))

bmi = w / h**2

if bmi < 18.3:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi <= 24.0:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi <= 28.5:
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi <= 32.5:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
    print("You are clinically obese")
