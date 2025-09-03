''' find simple intrest and total amount in hand'''
p = int(input("enter principle amount"))
t = int(input("enter time in years"))
r = int(input("rate of intrest"))
si = (p * t * r)/100
total_amt = p + r
print("simple intrest",si)
print("total_amt",total_amt)