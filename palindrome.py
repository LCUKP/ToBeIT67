n = int(input())
palindrome = []
for i in range(n) :
    word = input()
    ReWord = word[::-1]
    if ReWord == word :
        palindrome.append(word)
print(len(palindrome))
print(palindrome)