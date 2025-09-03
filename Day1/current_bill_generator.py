'''write a program to enter consumer number,consumer name, persent month reading and last month reading ,calculate total units and current bill 
note: cost per unit is 3.80,finally print all consumer details with bill'''



consumer_num = int(input("enter consumer number"))
conumer_name = input("enter consumer name :")
present_month_reading = int(input("present month reading"))
last_month_reading = int(input("last month reading"))
total_units = present_month_reading - last_month_reading
cost_per_unit = 3.80
current_bill = total_units * cost_per_unit
print(total_units)
print(current_bill)

print("consumer number",consumer_num)
print("consumer_name",conumer_name)
print("total units",total_units)
print("current_bill",current_bill)