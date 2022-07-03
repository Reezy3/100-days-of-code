# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Modulo
def modulo(n1, n2):
    return n1 % n2

# exponential
def exponential(n1, n2):
    return n1 ** n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": modulo,
  "**": exponential,
}

num1 = int(input("What is your first number? "))

for x in operations:
    print(x)
    
end_program = False
while not end_program:

    operation_symbol = input("Pick an operation symbol: ")
    num2 = int(input("What is the next number? "))

    calculation_function = operations[operation_symbol]

    answer = calculation_function(n1=num1, n2=num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    test_to_end = input("Do you want to calculate another number 'yes' or 'no': ").lower()
    if test_to_end == "no":
        end_program = True
        
    elif test_to_end == "yes":
        num1 = answer