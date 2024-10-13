# Open file in read mode
employee_file = open("13_employees_2.txt", "w")

# print(employee_file.readable())

# print(employee_file.readline())

# print(employee_file.writelines(["Toby - Human Resources"]))

print(employee_file.write("Kelly - Customer Services"))

employee_file.close()
