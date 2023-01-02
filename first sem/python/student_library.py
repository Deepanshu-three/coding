class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks
        
    def diaplayavilablebooks(self):
        print("Books in the library are: ")
        for books in self.books:
            print("\t * "+books)
    
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safr and return it on time")
            self.books.remove(bookname)
        
        else:
            print(f"sorry {bookname} has already been borrowed. Please wait for some time")
            
    
    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning the book hope you enjoy reading it")
         
    
class Student:
    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book     
    
    def returntbook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book 



if __name__ == "__main__":
    centrallibrary = Library(["booka","bookb","bookc"])
    student = Student()
    
    while True:
        wel = '''======== Welcome to the library =======
        Please choose an option to continue:
        1 - List all the books
        2 - Request a book
        3 - Return a book
        4 - Exit the library
        '''
        print(wel)
        a = int(input("Enter your choice: "))
        if a == 1:
            centrallibrary.diaplayavilablebooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestbook())
        elif a ==3:
            centrallibrary.returnbook(student.returntbook())
        elif a==4:
            print("Thank you for using your library. Come visit us again!")
            exit()
        else:
            print("Invalid Choice")