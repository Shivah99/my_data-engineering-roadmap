#Simple Billing System

print("Welcome to value electricity billing system!")
slab1_price = 2.77
slab2_price = 3.56
slab3_price = 5.0
print("Electricity rates per unit:")
print("Up to 100 units:", slab1_price)
print("101 to 250 units:", slab2_price)
print("Above 250 units:", slab3_price)
y=units_used=float(input("Enter the units consumed:"))

if y <= 100:
     print("Your units are under slab-1\n The final bill is:",(units_used * slab1_price))
elif y> 100 and y<=250:
     print("Your units are under slab-2\n The final bill is:",(100 * slab1_price) + ((units_used - 100) * slab2_price))
else:
    print("Your units are under slab-2\n The final bill is:",(100 * slab1_price) + (150 * slab2_price) + ((units_used - 250) * slab3_price))
print("Thanks for being our valued customer!")