BMI=(float(input("enter your BMI ==>")))

if BMI<18.5:
    print("you are underweight")
elif 18.5<=BMI<24.9:
    print("it's normal")
elif 25< BMI <29.9:
    print("over weight")
elif BMI > 30:
    print("it's obese")
else:
    print("something wrong")

