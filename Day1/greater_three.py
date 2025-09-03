def check(a,b,c):
    if a> b:
        if a>c:
            return a 
        else:
            return c
    else:
        if b >c:
            return b
        else:
            return c
a = int(input("enter a number1"))
b = int(input("enter a number2"))
c = int(input("enter a number3"))
print(f"this value is greatest :  {check(a,b,c)}")