class Book:
    def __init__(self, title, author, number_of_pages, current_page):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = current_page
        self.is_open = False

    def __str__(self):
        return f"Title: {self.title},\nAuthor: {self.author},\nNumber of pages: {self.number_of_pages},\nCurrent page: {self.current_page}"

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def read(self):
        if self.is_open and self.current_page < self.number_of_pages:
            self.current_page += 1
        elif self.current_page == self.number_of_pages:
            print("You read all the book.")
        else:
            print("The book is closed! Open it first.")
