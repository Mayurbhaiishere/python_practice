import math

Height = float(input("Enter the height of wall:"))
Angle = int(input("Enter the angle between wall and ladder:"))

Radian = math.radians(Angle)
Ladder_length = math.sin(Radian)

print("The length of ladder is",Ladder_length)
