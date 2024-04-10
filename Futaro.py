a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = float(input())
g = int(input())

ps = 0
t = ((f * g) * 60)/100
a = ((g*a)*(f*g))/100
b = ((g*b)*(f*g))/100
c = ((g*c)*(f*g))/100
d = ((g*d)*(f*g))/100
e = ((g*e)*(f*g))/100

if a > t :
    Ichika = "Pass"
    ps += 1
else :
    Ichika = "Fail"

if b > t :
    Nino = "Pass"
    ps += 1
else :
    Nino = "Fail"

if c > t :
    Miku = "Pass"
    ps += 1
else :
    Miku = "Fail"

if d > t :
    Yotsuba = "Pass"
    ps += 1
else :
    Yotsuba = "Fail"

if e > t :
    Itsuki = "Pass"
    ps += 1
else :
    Itsuki = "Fail"

print("Ichika :",Ichika+"\n"+"Nino :",Nino+"\n"+"Miku :",Miku+"\n"+"Yotsuba :",Yotsuba+"\n"+"Itsuki :",Itsuki)

if ps < 3 :
    print("Futaro Outtt!!!")

print(a,b,c,d,e,f,t)