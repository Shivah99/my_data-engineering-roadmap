
x=int(input("select the shape you wanna measure \n1. rectangle\n2.square\n3. circle:"))
if x==1:
    l=float(input("Recatnagle it is !\nEnter the lenth:"))
    b=float(input("Enter the breadth:"))
    print("area of rectangle:", l*b, "perimeter:",2*(l+b))
elif x==2:
    l=float(input("Square it is!\nEnter the lenth of the side:"))
    print("area of Square:", l*l, "perimeter:", 4*l )
elif x==3:
    l=float(input("Circle it is!\nEnter the radius:"))
    print("area of Circle:", (3.14*l*l), "perimeter:",2*3.14*l )
else:
    print("ERROR! please try again.")
