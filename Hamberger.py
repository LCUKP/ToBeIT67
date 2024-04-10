import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

n = 0


d = (d / c) 
if d % 2 == 0 :
    pass
else :
    d = math.ceil(d)
    print(math.ceil(d))

if d >= b :
    d = d * c
    n = d
    x = (n * a) - (c * a)
else :
    n = d
    x = (n * a)

print(n,"ชิ้น")
print(x,"บาท")