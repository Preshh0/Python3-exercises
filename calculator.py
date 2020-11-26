num1 = float(input("Enter first number: "))

operator = input("Enter operator: ")

num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator.")

# num1 = input("Enter number: ")
# num2 = input("Enter another number: ")
# result = num1 + num2

# print(int(result))

#Definitely fix this.
#edit:
# The operators only work when you put strings around them