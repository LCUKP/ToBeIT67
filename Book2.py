code = input()
books = []
while code != "END" :
    code = input()
    books.append(code)

booksr = list(books)
booksr.sort()

for x in books :
    print(x,booksr.index(books[books.index(x)]),books.count(x))