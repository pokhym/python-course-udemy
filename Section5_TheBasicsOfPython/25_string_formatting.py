age=24
print("my age is " + str(age) + " years") #str function converts to string

# this can be more easily done with replacement fields
print("my age is {0} years".format(age)) # {0} is the replacement field
# this can be extended for multiple variables
print("{0}, {1}, {2}".format(31, "jan", age))
# replacement fields can be used more than once
print("{0}, {1}, {2}, copied {2}, copied again {2}".format(31, "jan", age, age, age))
# note the order of the replacement fields can be infered
print("{}, {}, {}".format(31, "jan", age))

# deprecated string formatting operator (python 2 only)
print("my age is %d years." %age) # like c or c++
print("my age is %d %s %d %s" %(age, "years", 6, "months")) # d=int, s=string

for i in range(1,12):
    print("No. %2d squared is %4d and cubed is %4d" %(i,i**2,i**3))
    # the 2 and 4 represent the number of digits it will take up therefore this causes it to be
    # naturally formatted

# using replacement fields
for i in range(1,12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))
    # note the first digit before the colon represents the index in the format and the
    # digit afte the colon represents the length of the number to be output
    # if using 1:<4 will make everything shift to the left like
    # 1
    # 234
    # 234889

# specify the precision of a number
print("%12.6f"%(22/7)) # 12 digits of 12 precision before decimal 6 digits of precision after decimal

# specify the precision of a number using replacement field
print("{0:12.7}".format(22/7)) # 12 digits of 12 precision before decimal 6 digits of precision after decimal


