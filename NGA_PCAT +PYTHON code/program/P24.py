#  a program that simulates a simple book management system. Users can add books, remove books, search for books, and display the current list of books in the library:

library = []

# fucntion  to display  the current library
def display_library():
 if not library:
  print("The library is empty.")
 else:
  print("Library Books: ")
  for book in library:
   print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")


# function to add a book  to the libaray
def add_book(title, author, isbn):
 book = {'title':title, 'author': author, 'isbn':isbn}
 library.append(book)
 print(f"Book '{title}' by {author} with  ISBN {isbn} has been  added to the library. ")


# function to remove a book  from  the library
def remove_book(isbn):
 for book in library:
  if book['isbn']  == isbn:
   library.remove(book)
   print(f"Book  with ISBN {isbn} has been  removed from  the libaray.")
   return
 
 print(f"No book found  with ISBN {isbn} in library.")




# Function  to serach  for a  book  by title or author
def search_book(query):
  found_book = []
  for book in library:
    if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
      found_book.append(book)
    
    if found_book:
      print("Found Book: ")
      for book in found_book:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
    else:
      print(f"No books found  matching '{query}'.")


# main Program  loop 
while True:
  print("\n1. Add book  to library")
  print("2. Remove book from library")
  print("3. Search for a book") 
  print("4.Display  libarary books")
  print("5. Exit")


  choice =  input("Enter  Your  Choice (1-5)  ")

  if choice == '1':
    title = input("Enter the title of the book: ")
    author = input("Enter  the Author  of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    add_book(title, author, isbn)
  elif choice == '2':
    isbn = input("Enter the ISBN  of the book to remove: ")
    remove_book(isbn)
  elif choice == '3':
    query = input("Enter the  title or author to search for: ")
    search_book(query)
  elif choice =='4':
    display_library()
  elif choice == '5':
    print("Exiting Program...")
    break
  else:
    print("Invalid  choice . Please enter  a number  from  1 to 5.")


 