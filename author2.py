#Author class created
class Author:
    #intials function with attributes of authors name
    def __init__(self, name):
        self.name = name
        self.books= []

    #fuction that takes titles and adds it to the book list
    def Publish(self, title):
        #checks if the new title added is in the book list
        if title in self.books:
            print('already in list')
        else:
            self.books.append(title)

     #string function joins the list and displays authors and books
    def __str__(self):
        list_of_books= ' , '.join(self.books)
        return f'|Author name: {self.name}| Books Published: {list_of_books}|'


author1=Author('J. K. Rowling')
author1.Publish('Fantastic Beasts and Where to Find Them')
author1.Publish('Harry Potter')
author1.Publish('Harry Potter')


print(author1)
