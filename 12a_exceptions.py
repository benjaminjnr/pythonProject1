
# # this input is unprotected and can break
# number = int(input("Enter a number: "))
# print(number)

# let's now account for possible exceptions
try:
    number = int(input("Enter a number: "))
    answer = 10 / number
    print(number)
except ZeroDivisionError as err:
    # print("Divided by zero")
    print(err)
except ValueError as err:
    print("Invalid input!")



