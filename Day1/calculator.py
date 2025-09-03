def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if(b !=0):
        return a/b
    else:
        return "not divisible"
def remainder(a,b):
    return a%b
a = int(input("enter a:"))
b = int(input("enter b:"))
print("addition value is",add(a,b))
print("subtraction value is ",subtract(a,b))
print("multiplication value is",multiply(a,b))
print("division value is ",division(a,b))
print("remainder is ",remainder(a,b))