x = int(input("enter number1"))
y = int(input("enter number 2"))
x,y = y,x
'''
using temporary variable
temp = x
x = y
y = temp
'''

print("x value",x)
print("y value",y)
