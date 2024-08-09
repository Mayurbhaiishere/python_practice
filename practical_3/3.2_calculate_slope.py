line_x1 = int(input("Enter X1:"))
line_x2 = int(input("Enter X2:"))
line_Y1 = int(input("Enter Y1:"))
line_Y2 = int(input("Enter Y2:"))

if line_x1 == line_x2:
    print ("no slope found.")

else:
    slope = (line_Y2-line_Y1)/(line_x2-line_x1)
    print("slope of line is :",slope)

