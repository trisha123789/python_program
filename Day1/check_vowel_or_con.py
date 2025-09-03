def check(n):
    list =['a','e','i','o','u']
    if n in list:
        return "is a vowel"
    else:
        return "is a consonant"
n = ord(input("enter a character"))
print(f"the given character  {check(n)}")