





# Multiple expection (multiple exception for single try)


# try:
#     print(x)
# except ValueError:
#     print("variable x is not defined.")
# except:
#     print("Unknown Exception")


# Else with try: ---> We can use the else keyword to define a block of code to be executed if no errors were raised.

# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("All are Ok No Exception")

# try, except, else, finally

# try:
#     n = int(input("Enter a value:"))
#     res = 100/n
# except ZeroDivisionError:
#     print("You can't divide by Zero")
# except Exception as e:
#     print(f"{e} occured please enter appropriate numeric value")
# else:
#     print(res)
# finally:
#     print("Process Completed.....")

# Note There can be multiple except block for one try but only one else and finally can be used

# Nested try (Nested Try)

try:
    file = open("D:/Programs/Python Playwright/direcoty1/myfile.txt","w")
    try:
        file.write("Welcomne")
    except:
        print("Something Went Wrong")
    finally:
        file.close()
except:
    print("Something went wrong opening the file")

