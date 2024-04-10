import math
radius = (math.pi * (int(input())** 2))*2
point = int(input())

if point > radius :
    print("Safe")
elif point <= radius :
    print("Not Safe")
print(radius)