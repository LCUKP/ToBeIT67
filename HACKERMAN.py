key = 0
for i in range(5) :
    char = input()

    if char == "a" or char == "f" or char == "k" or char == "p" or char == "u" or char == "z" :
        key = key + 2
    elif char == "b" or char == "g" or char == "l" or char == "q" or char == "v" :
        key = key + 4
    elif char == "c" or char == "h" or char == "m" or char == "r" or char == "w" :
        key = key + 6
    elif char == "d" or char == "i" or char == "n" or char == "s" or char == "x" :
        key = key + 8
    elif char == "e" or char == "j" or char == "o" or char == "t" or char == "y" :
        key = key + 10

if key >= 25 :
    print("Unlock")
elif key < 25 :
    print(25 - key)