age=23#int(input("how old are you"))

if age>=16 and age<=65:
    print("you are between the ages of 16 and 65")

# the below also works which is awesome and doens twork in c++
if 16<=age<=65:
    print("you are between the ages of 16 and 65")

if age<16 or age>65:
    print("checks if either youre <16 or >65")

x="false"
if x: # in a condition any non 0 is considered as true
    print("x is true")

x=0 # this will print false
if not x:
    print("x is false")

# bool function can be used to check true or false
print(bool(1))
print(bool(0))
print(bool("test"))

# letter presence checker
parrot="norwegian Blue"
letter=input("enter a char: ")

if letter in parrot:
    print("{} is present".format(letter))
else:
    print("letter not present")