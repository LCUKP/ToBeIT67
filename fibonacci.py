def FibonacciRecursion(Num) :
    if Num in d:
        return d[Num]
    else :
        if Num == 1 :
            return 0
        elif Num == 2 :
            return 1
        elif Num == 3 :
            return 1
        else :
            fibo = FibonacciRecursion(Num - 2 ) + FibonacciRecursion(Num - 1)
            d[Num] = fibo
            return fibo
N = int(input())+1
d = []
print(FibonacciRecursion(N))