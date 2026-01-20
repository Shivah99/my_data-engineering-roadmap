x=int(input("Enter integer:x ="))
y=abs(x)
last_digit=y%10
print("last digit:", last_digit)

y=input("\nEnter integer:y =")
z=input("Enter integer:z =")


print("before swap y:", y, "z:", z)
temp = y
y = z
z = temp

print("after swap y:", y, "z:", z)

