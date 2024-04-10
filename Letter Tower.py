word = input()
print("_"*9)
for i in word :
    print("|{} <-> {}|".format(i,i))
    word.pop()
print("*"*9)