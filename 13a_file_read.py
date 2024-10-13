# Open file in read mode
employee_file = open("13_employees.txt", "r")

# print(employee_file.readable())

# print(employee_file.readline())

# print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
