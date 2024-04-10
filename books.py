num = int(input())
books = []
for i in range(num) :
    book = input()
    if i == 0 :
        books.append(book)
    else :
        for x in range(len(books)) :
            if books.count(book) < 2 :
                if books[x] != book :
                    books.append(book)
                    break
                else :
                    books.insert(x+1,book)
                    break

print("ชั้นวางหนังสือ",books)