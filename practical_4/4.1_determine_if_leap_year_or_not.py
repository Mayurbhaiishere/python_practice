year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Year is a leap year.")
elif year % 100 == 0:
    print("Year is not a leap year.")
elif year % 4 == 0:
    print("Year is a leap year.")
else:
    print("Year is not a leap year.")
