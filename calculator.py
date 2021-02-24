"""def add(x,y):
    
    return (x+y)
    pass
def sub(x,y):
    
    return (x-y)
    pass
def mul(x,y):
    
    return (x*y)
    pass
def div(x,y):
    div = x + y
    return (x/y)
    pass
def exp(x,y):
    exp = x + y
    return (x**y)
    pass
def sqrt(x,y):
    sqrt = x + y
    return (sqrt)
    pass"""
    
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function expon two numbers
def exponent(x, y):
    return x ** y

# This function squr two numbers
def sqrt(x, y):
    return x ** y/0.5

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Squre root")
while True:
    # Take input from the user
    choice = input("Please choose a number from 1-6: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", exponent(num1, num2))

        elif choice == '6':
            print(num1, "/", num2, "=", sqrt(num1, num2))

        break
    else:
        print("Invalid Input")
        

