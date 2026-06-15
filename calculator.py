def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b== 0:
       return "Cannot be divide by zero"
    return a/b
print ("______CALCULATOR______")
print("1. Adition\n2. Subtraction\n3. Multiplication\n4. Division")
a = float(input("Enter the number a: "))
b = float(input("Enter thenumber b: "))
choice = input("Enter your operation from(1-4): ")
if choice == "1":
    result = add(a,b)
    print(f"sum of {a} and {b} is ",result)
elif choice == "2":
    result = subtract(a,b)
    print(f"subtraction of {a} and {b} is ",result)
elif choice == "3":
    result = multiply(a,b)
    print(f"multiplication of {a} and {b} is ",result)
elif choice == "4":
    result = division(a,b)
    print(f"division of {a} and {b} is ",result)   
else:
    print("invalid choice!")