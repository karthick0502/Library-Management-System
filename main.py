import sys


# Create Books Library

class BooksLibrary:

    def __init__(self, books):
        self.books_collection = books

    def add_books(self):
        existing_id = list(self.books_collection)[-1]
        new_id = int(input('How many books you want to add: '))
        for book_id in range(existing_id + 1, existing_id + new_id + 1):
            name = input('enter book name: ')
            author = input('enter author name: ')
            new_book_key = book_id
            new_book_value = {'name': name, 'author': author, 'status': 'available'}
            self.books_collection.update({new_book_key: new_book_value})
        print('All Books has been added successfully in the library')

    def update_books(self):
        id = int(input('Enter the book id which you want to update: '))
        if id in list(self.books_collection):
            name = input('enter the new book name: ')
            author = input('enter the author name: ')
            status = input('enter book the new status [available/ unavailable]: ')
            self.books_collection[id] = {'name': name, 'author': author, 'status': status}
            print('Book information was updated successfully in the library')
        elif id not in list(self.books_collection):
            print('book id was incorrect!')
        else:
            print('something wrong!')

    def delete_books(self):
        id = int(input('Enter the book id which you want to delete: '))
        if id in list(self.books_collection):
            del self.books_collection[id]
            print('Book was deleted successfully!')
        elif id not in list(self.books_collection):
            print('book id was incorrect!')
        else:
            print('something wrong!')

    def display_books(self):
        for books_id, books_detail in self.books_collection.items():
            print('************************* \n'
                  'book_id: ', books_id)
            for books_detail_keys, books_detail_values in books_detail.items():
                print(books_detail_keys, ':', books_detail_values)
        return self.books_collection

    # Student Request Book
    def request_books(self, requested):
        if requested in list(self.books_collection):
            for status in self.books_collection[requested].values():
                if status == 'available':
                    self.books_collection[requested]['status'] = 'unavailable'
                    return 'The book which requested is allocated you.'
                elif status == 'unavailable':
                    return f'Sorry! The book which you requested is not available.'
        elif requested not in list(self.books_collection):
            return 'book id was incorrect!'
        else:
            return 'something Wrong!'

    # Student Return Book
    def return_books(self, returned):
        if returned in list(self.books_collection):
            for status in self.books_collection[returned].values():
                if status == 'unavailable':
                    self.books_collection[returned]['status'] = 'available'
                    return 'The book which you returned was successfully updated in library'
                elif status == 'available':
                    return 'Great! The book id which you entered is already available.'
        elif returned not in list(self.books_collection):
            return 'book id was incorrect!'
        else:
            return 'something Wrong!'


# Create class for student

class Student:

    def request_book(self):
        self.requested = int(input('Enter the book id you would like to have: '))
        response = librarian.request_books(self.requested)
        print(response)

    def return_book(self):
        self.returned_to = int(input('Enter the book id you want to return: '))
        response = librarian.return_books(self.returned_to)
        print(response)


books_collection = {1: {'name': 'Apple', 'author': 'Steve jobs', 'status': 'available'},
                    2: {'name': 'TATA', 'author': 'Ratan tata', 'status': 'available'},
                    3: {'name': 'SPACE X', 'author': 'Elon musk', 'status': 'available'},
                    4: {'name': 'Mahabharata', 'author': 'Vyasa', 'status': 'available'},
                    5: {'name': 'stock market', 'author': 'Warren Buffett', 'status': 'available'}}

librarian = BooksLibrary(books_collection)

while True:

    print('*************LIBRARY MANAGEMENT SYSTEM***********\n'
          '1. Display Books\n'
          '2. Add New books\n'
          '3. Update Books\n'
          '4. Delete Books\n'
          '5. Request Books\n'
          '6. Return books\n'
          '7. Exit')
    choice = int(input('please select your option: '))
    if choice == 1:
        librarian.display_books()
    elif choice == 2:
        librarian.add_books()
    elif choice == 3:
        librarian.update_books()
    elif choice == 4:
        librarian.delete_books()
    elif choice == 5:
        Student().request_book()
    elif choice == 6:
        Student().return_book()
    elif choice == 7:
        sys.exit()
    else:
        print('Invalid choice!')
