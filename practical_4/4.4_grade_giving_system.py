DSA_marks = float(input("Enter the marks in DSA(from 100):"))
RDMS_marks = float(input("Enter the marks in RDMS(from 100):"))
BOOS_marks = float(input("Enter the marks in BOOS(from 100):"))
Python_marks = float(input("Enter the marks in Python(from 100):"))
Grade = None


Total_marks = (DSA_marks+RDMS_marks+BOOS_marks+Python_marks)/4

if Total_marks <= 0 or Total_marks >= 100 :
    print("invalid Grade")
    Grade = -1
else :
    if Total_marks >= 90 and Total_marks  <= 100 :
        Grade = 'A'
    elif Total_marks >= 80 and Total_marks <= 89 :
        Grade = 'B'
    elif Total_marks >= 70 and Total_marks <= 79 :
        Grade = 'C'
    elif Total_marks >= 60 and Total_marks <= 69 :
        Grade = 'D'
    elif Total_marks >= 50 and Total_marks <= 59 :
        Grade = 'E'
    elif Total_marks >= 0 and Total_marks < 50 :
        Grade = 'F'
        


print(Grade)