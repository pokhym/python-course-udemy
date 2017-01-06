# range will return values between range(a,b) from a to b-1
for i in range(1,20):
    print("i is now {}".format(i))

number="9,223,372,036,854,785,807"
num=""
for i in range(0, len(number)): # len returns the length of the string note no need to minus 1 (unlike C)
    if number[i] in '0123456789':
        # print(number[i]) # this will print new line chars by default
        print(number[i], end='') # end will specify the thing that happens after the thing
        num=num+number[i]
print()
print(int(num))
