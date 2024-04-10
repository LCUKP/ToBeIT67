def bonus(Salary,years,month) :
    while month >= 10 :
        years = years + 1
        month -= 12
    if years >= 20 :
        years = 20

    Salary *= years 
    if Salary < 5000 :
        Salary = 5000
    elif Salary > 1000000 :
        Salary = 1000000
    print(Salary)

bonus(int(input()),int(input()),int(input()))

'''ปกติผมไม่เขียนอย่างงี้เห็นพี่ทำเลยลองบ้าง'''