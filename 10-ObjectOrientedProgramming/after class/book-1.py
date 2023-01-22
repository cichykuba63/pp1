from book import Book

book = Book("A glass", "Ed Sheeran", 200, 14)
book.open()
print(book)

print()

book.read()
print(book)

book.close()
print()
book.read()