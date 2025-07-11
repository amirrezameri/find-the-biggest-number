x = int(input("enter your first number"))
y = int(input("enter your second number"))
z = int(input("enter your third number"))

if x>y:
    if x>z:
        print(f"the biggest number is {x}")
if y>x:
    if y>z:
        print(f"the biggest number is {y}")
if z>x:
    if z>y:
        print(f"the biggest number is {z}")                    
