P = int(input("Enter the principal value:"))
R = float(input("Enter the rate(in %) value:"))
T = float(input("Enter the time period:"))
n = int(input("Enter the no of weeks:"))

SimpleInterest= (P*R*T)/100
CompoundInterest= P*(1+(R/(100*n)))**(n*T)

print("Simple interest of given values is:",SimpleInterest)
print("Compound interest of given values is:",CompoundInterest)