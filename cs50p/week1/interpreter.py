expression = input("Expression: ")
x, y, z = expression.split()
if y == "/" and z == "0":
    print("You can't divide by 0")
else:
    match y:
        case "+":
            print(f"{float(x) + float(z):.1f}")
        case "-":
            print(f"{float(x) - float(z):.1f}")
        case "*":
            print(f"{float(x) * float(z):.1f}")
        case "/":
            print(f"{float(x) / float(z):.1f}")