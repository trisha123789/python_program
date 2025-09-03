def check(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
n = int(input("enter a num"))
ans = check(n)
print("the given num is ",ans)