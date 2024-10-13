# Open file in read mode
employee_file = open("13_employees.txt", "a")

# print(employee_file.readable())

# print(employee_file.readline())

# print(employee_file.writelines(["Toby - Human Resources"]))

print(employee_file.write("\nKelly - Customer Services"))

employee_file.close()
