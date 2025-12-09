# BMI CALCULATOR
# BMI = WEIGHT / HEIGHT(SQUARE)

height = float(input("Enter your height"))
weight = int(input("Enter your weight"))

# print(type(height))

bmi = weight / pow(height,2)
print("Your BMI is: ", bmi)