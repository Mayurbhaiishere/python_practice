A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))
C = int(input("Enter the value of C:"))


Discriminant = (B**2) - (4*A*C)
Root_1 = (-B+(Discriminant**0.5))/(2*A)
Root_2 = (-B-(Discriminant**0.5))/(2*A)

print("Two roots of given equation are:",Root_1,"and",Root_2)

