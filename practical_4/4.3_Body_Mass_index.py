Mass = float(input("Enter your weight(in kg):"))
Height = float(input("Enter your height(in m):"))

BMI = Mass/(Height**2)

if BMI > 19 and BMI < 25:
    print("bhai tu healthy hai.")

elif BMI < 19 :
    print("kuposhit or underweight.")

else:
    print("abe jadiye or overweight")
