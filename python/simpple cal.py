num1 = int(input("Enter a first number "))
num2 = int(input("Enter a second number "))
operator = input("Enter a operator (+,-,*,/ )")
# using comdition check
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("invalid operation")
