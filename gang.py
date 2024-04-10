import math
gang = ""
sums = 0
while gang != "stop" :
    gang = input()
    if gang == "shrimp sour soup" :
        sums += 80
    elif gang == "mixed vegetables sour soup" :
        sums += 60
    elif gang == "papaya sour soup" :
        sums += 55
    elif gang == "snapper fish sour soup" :
        sums += 100
    elif gang == "cha om shrimp sour soup" :
        sums += 100

if sums > 200 :
    discount = (sums * 15) / 100
else :
    discount = 0
    
total = sums - discount
print("Original Price {} baht\nDiscount {} baht\nTotal {} baht".format(sums,math.floor(discount),math.floor(total)))