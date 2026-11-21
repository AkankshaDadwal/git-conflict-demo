def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b

if __name__ == "__main__":
    print(calculate(4, 2, "+"))