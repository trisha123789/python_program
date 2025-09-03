'''write a program to enter student number student name 3 subject marks calculate total average of students details'''
name = input("enter the name")
num = int(input("enter roll no"))
s1 = int(input("enter marks of first subject"))

s2 = int(input("enter marks of second student"))
s3 = int(input("enter the marks of third student"))
total = s1 +s2+s3
avg = total/3
a = round(avg,2)

print("details")
print(f"name is {name} num is {num} ")
print(f"subject1 is {s1} subject2 marks {s2} subject3 {s3}")
print(f" total is {total} avg is {a}")
