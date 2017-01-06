# get input name
name=input("enter your name") # note the input function returns a string type
age=int(input("age please, {}".format(name)))

# check age
if age>=18:
    print("old enough")
elif age<0:
    print("you cant have negative age")
else:
    print("wrong age")