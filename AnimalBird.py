# ****** Approach1 : No issue  ******
# import animal as a 
# import bird as b 

# a.fly()

# a.color()

# b.fly()

# b.color()


# *********Approach - 2/3***********
# from animal import *

# from bird import *  # Recent decalred module will be accessed

# fly()

# color()

# ************ Solution of Approach 2/3 *************

# from bird import *
# fly()
# color()

# from animal import *

# fly()

# color ()

# ********** Access Class ************

# ----------- Approach 1 -------------

# import animal as a
# import bird as b 
# objA = a.Animal() # Object is created of class to access class methods

# objA.display()


# -------- Approach 2 --------------

from animal import Animal # from animal import *

from bird import Bird  # from birt import *

obja = Animal()

objb = Bird()

obja.display()

objb.display()