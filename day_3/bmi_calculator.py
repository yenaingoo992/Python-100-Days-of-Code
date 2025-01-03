print("BMI Calculator")
print("******************\n")

height = float(input("What is your height in feet?\n"))
weight = float(input("What is your weight in pounds?\n"))

# convert feet to inches
feet_to_inches = int(height) * 12

# % 1 is used to get only decimal points in floating numbers
total_inches = feet_to_inches + ((height % 1) * 10)

# calculate bmi
bmi = round((703 * weight) / (total_inches ** 2), 1)

# printing result
result = ""
if bmi < 18.5:
    result = "Underweight"
elif 18.5 <= bmi <= 24.9:
    result = "Normal"
elif 25.0 <= bmi <= 29.9:
    result = "Overweight"
else:
    result = "Obese"

print(f"Your Result: {result}")