def check(n):
    if n >=65 and n <=90 or n >=97 and n <=125:
        return "character"
    else:
        return "not a character"
n = ord(input("enter a character"))
 
print(f"the entered value is {check(n)}")
