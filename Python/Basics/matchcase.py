a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
op = input("Enter operator ")
match(op):
    case '+':
        print(f"Sum = {a+b}")
    case '-':
        print(f"Difference = {a-b}")
    case _:
        print("No such operator")
