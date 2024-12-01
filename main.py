# Enhanced Library Program

# Initialize an empty list to store book information
library = []

def add_book(title, author, year):
    """
    Adds a book to the library with the given title, author, and year.
    """
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True  # Indicates if the book is available for borrowing
    }
    library.append(book)
    print(f"\nBook '{title}' by {author} (Year: {year}) added to the library.\n")

def view_all_books():
    """
    Displays all books in the library along with their availability status.
    """
    if not library:
        print("\nNo books in the library.\n")
    else:
        print("\nList of Books in the Library:")
        print("-" * 50)
        for index, book in enumerate(library, start=1):
            status = "Available" if book['available'] else "Borrowed"
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, "
                  f"Year: {book['year']}, Status: {status}")
        print("-" * 50 + "\n")

def borrow_book(title):
    """
    Borrows a book from the library if it's available.
    """
    for book in library:
        if book['title'].lower() == title.lower():
            if book['available']:
                book['available'] = False
                print(f"\nYou have successfully borrowed '{book['title']}'.\n")
                return
            else:
                print(f"\nSorry, '{book['title']}' is currently borrowed.\n")
                return
    print(f"\nBook '{title}' not found in the library.\n")

def return_book(title):
    """
    Returns a borrowed book to the library.
    """
    for book in library:
        if book['title'].lower() == title.lower():
            if not book['available']:
                book['available'] = True
                print(f"\nYou have successfully returned '{book['title']}'.\n")
                return
            else:
                print(f"\nBook '{book['title']}' was not borrowed.\n")
                return
    print(f"\nBook '{title}' not found in the library.\n")

# Main program loop
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
            # Get book details from the user
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            year = input("Enter the publication year: ").strip()
            
            if title and author and year.isdigit():
                add_book(title, author, year)
            else:
                print("\nInvalid input. Please ensure all fields are correctly filled.\n")
        
        elif choice == '2':
            view_all_books()
        
        elif choice == '3':
            # Get the title of the book to borrow
            title = input("Enter the title of the book to borrow: ").strip()
            if title:
                borrow_book(title)
            else:
                print("\nInvalid input. Please enter a valid book title.\n")
        
        elif choice == '4':
            # Get the title of the book to return
            title = input("Enter the title of the book to return: ").strip()
            if title:
                return_book(title)
            else:
                print("\nInvalid input. Please enter a valid book title.\n")
        
        elif choice == '5':
            print("\nExiting the program. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
