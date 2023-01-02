a = int(input("Enter first numbre "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))

if a>b and a>c:
    print(f"{a} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")