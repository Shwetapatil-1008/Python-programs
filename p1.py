rollNo = int(input("Enter student's roll number:  "))
name = input("Enter students name: ")
marks1 = int(input("Enter the marks in first subject:  "))
marks2 = int(input("Enter the marks in second subject:  "))
marks3 = int(input("Enter the marks in third subject:  "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("Total marks= ",total)
print(f"Percentage= {percentage:.2f} %")
