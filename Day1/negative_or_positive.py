def check(n):
    if n < 0:
        return "negative"
    else:
        return "positive"





n = int(input("enter a number"))
ans = check(n)
print("the number is",ans)