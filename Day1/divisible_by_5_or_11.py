def check(n):
    if n% 5 == 0 and n%11 ==0:
        return "divisible"
    else:
        return "not divisible"
a = int(input("enter a number"))
print(f"the number is {check(a)} by 5 and 11")