# write a small program to ask for a name and an age
# wen both values have been entered, check if the person
# is the right age to go on an 18-30 holidya (they must be over 18 and under 31).
# if they are welcome them to the holidy, otherwise print a polite message refusing them entry


# get input
name=input("Enter your name please: ")
age=int(input("{} please enter your age please: ".format(name)))

# check if valid age
if 18<=age<=30:
    print("{}, you are invited to go on a cruise.".format(name))
else:
    print("{}, you are not elligible for this cruise.".format(name))
