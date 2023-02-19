height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Write your code below this line
bmI = weight / (height ** 2)
bmiStr = str(bmI)

if bmI < 18:
    print("Your BMI is " + bmiStr + " and you are underweight")
elif 18.5 > bmI < 25:
    print("Your BMI is " + bmiStr + " and you have a normal weight")
elif 25 > bmI < 30:
    print("Your BMI is " + bmiStr + " and you are overweight")
elif 30 > bmI < 35:
    print("Your BMI is " + bmiStr + " and you are obese")
else:
    print("Your BMI is " + bmiStr + " and you are clinically obese")
