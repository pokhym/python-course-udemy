parrot="norwegian blue"
print(parrot)
print(parrot[3]) # n=0, o=1, r=2, w=3
print(parrot[-1]) # counts backwards gives the e in 'blue'a
# slicing get range of values
print(parrot[0:6]) # doesnt print 6 ends at 5
print(parrot[6:]) #from 6 to enda
print(parrot[-4:-2]) #prints bl cant do -4:2 because it cant go backwards
print(parrot[0:6:2]) # start at 0 go up to 5 and with stepsize of 2
print()

print("hi " " bye") # with string literals u dont need the + sign to concactenate
print("hello "*5) # do print 5 timesa
print()

today="today"
print("day" in today) # checks if day is in the variable today and prints true or false
print("friday" in today)