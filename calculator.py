# Calculator
print("¿What operation do you want?")
print()
op = input("Enter either +, -, *, / or **: ")
print()

n1 = float(input("Enter first number: "))
print()
n2 = float(input("Enter second number: "))

if op == "+":
    print(n1, op, n2, "=", n1+n2)
elif op == "-":
    print(n1, op, n2, "=", n1-n2)
elif op == "*":
    print(n1, n2, op, "=", n1*n2)
elif op == "/":
    print(n1, n2, op, "=", n1/n2)
elif op == "**":
    print(n1, n2, op, "=", n1**n2)    
else:
    print()
    print("invalid input")
    
    




    

