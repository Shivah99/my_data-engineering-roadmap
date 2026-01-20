P = float(input("Enter principal amount:"))
T = float(input("Enter time in year/s:"))
R = float(input("Enter Rate of Interest:"))

SI= (P*T*R)/100

print("simple interest:", SI)

MSI= SI/(T*12)

print("Average monthly interest:", MSI)