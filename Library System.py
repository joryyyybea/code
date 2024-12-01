# John Henry P. Ortega
# A24-39085


Library = []

def Add_Book(title):
    """
    Add a book in the Library.
    """
    book = {
        "title": title,
        "available": True  
    }
    Library.append(book)
    print(f"Book '{book['title']}' added to the list.\n")

def View_All_Books():
    """
    Display all books in the Library.
    """
    if not Library:
        print("No books in the library.\n")
    else:
        print("\nList of books in the Library:")
        for i in range(len(Library)):
            availability = "Available" if Library[i]['available'] else "Borrowed"
            print(f"{i + 1}. {Library[i]['title']} - {availability}")

def Borrow_a_Book(title):
    """
    Borrow a book from the Library.
    """
    for book in Library:
        if book['title'].lower() == title.lower():
            if book['available']:
                book['available'] = False
                print(f"\nYou have successfully borrowed '{book['title']}'.\n")
                return
            else:
                print(f"\nSorry, '{book['title']}' is currently borrowed.\n")
                return
    print(f"\nBook '{title}' not found in the library.\n")

def Return_Book(title):
    """
    Return borrowed book to the Library.
    """
    for book in Library:
        if book['title'].lower() == title.lower():
            if not book['available']:
                book['available'] = True
                print(f"\nYou have successfully returned '{book['title']}'.\n")
                return
            else:
                print(f"\nBook '{book['title']}' was not borrowed.\n")
                return
    print(f"\nBook '{title}' not found in the library.\n")

def main():
    while True:
        print("Library Menu:")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        
        if choice == '1':
            title = input("Enter the book title: ").strip()
            if title:
                Add_Book(title)
            else:
                print("\nInvalid input. Please enter a valid book title.\n")
        
        elif choice == '2':
            View_All_Books()
        
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ").strip()
            if title:
                Borrow_a_Book(title)
            else:
                print("\nInvalid input. Please enter a valid book title.\n")
        
        elif choice == '4':
            title = input("Enter the title of the book to return: ").strip()
            if title:
                Return_Book(title)
            else:
                print("\nInvalid input. Please enter a valid book title.\n")
        
        elif choice == '5':
            print("\nExiting the program. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice. Please choose a valid option from the menu.\n")

if __name__ == "__main__":
    main()