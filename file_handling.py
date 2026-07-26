import os

# import shutil 

# Create/Write a file --> If file exists then it will write only. If not exists then first create then write


# **************** Approach 1 ********************

# file = open("D:/Programs/Python Playwright/direcoty1/my_newfile.txt","w")

# file.write("Welcome to Python \n File handling")
# file.close()


# *************** Approach 2 *******************

# with open("D:/Programs/Python Playwright/direcoty1/my_newfile.txt","w") as file:
#     file.write("Welcome to Python\nFile handling")
#     file.close()


# Appending Data into file
# with open("D:/Programs/Python Playwright/direcoty1/my_newfile.txt","a") as file:
#     file.write("\nI am Ashutosh Rout")
#     file.close()

# Reading Data from text file
# --> read() - reads entire data
# --> readline() - read single line
# --> readlines() - read all lines into list format

# file = open("D:/Programs/Python Playwright/direcoty1/my_newfile.txt","r")

# content = file.read()
# content = file.readline()
# content = file.readlines()
# print(content)
# file.close()

# Rename the file
# import os

# os.rename("D:/Programs/Python Playwright/direcoty1/my_newfile.txt","D:/Programs/Python Playwright/direcoty1/my_file.txt")
# print("file renamed")

# Deleting the file
# import os

# file = "D:/Programs/Python Playwright/direcoty1/my_file.txt"

# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("Does not exists")

# Creating a directory/folder


# os.mkdir("D:\\Programs\\Python Playwright\\mydir")
# print("Directory Created")

# Check Directory Exists or not

# myDir = "D:\\Programs\\Python Playwright\\mydir"

# if os.path.exists(myDir):
#     print("Directory Exists")
#     os.rename(myDir,"D:\\Programs\\Python Playwright\\mydirctory")
#     print("directory renamed")
# else:
#     print("Not Exists")

# Delete Directory 
# myDir = "D:\\Programs\\Python Playwright\\mydirctory"

# if os.path.exists(myDir):
#     print("Directory Exists")
#     os.rmdir(myDir)  # If directory is empty then rmdir works
#     print("directory removed")
# else:
#     print("Not Exists")

# delete directory with wile contains

# shutil.rmtree("D:\\Spring Projects")

# Get the current working directory

print(os.getcwd())  # return current working directory