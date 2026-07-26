# Approach1:  to access methods of other file by importing and using that module object

# import methods_test_files as mtf

# mtf.add(30,40)

# mtf.sub (45,12)

# print(mtf.person["country"])

# Approach 2: from and import

# from methods_test_files import add, person

# add(34,66)

# print(person["name"])

# **** Approach 3: If you don't name module name or attribute name *****

from methods_test_files import *

print(person["age"])