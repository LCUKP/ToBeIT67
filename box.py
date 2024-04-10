x = int(input())
y = int(input())
z = int(input())
print("------")
for i in range(y) :
    print("|"+"*"*(y)+"|")
    z -= x
print("------")
print("There are {} stars left.".format(z))