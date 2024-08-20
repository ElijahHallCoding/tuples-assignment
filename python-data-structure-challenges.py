# Start with an existing list of books in the library
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    # Check if the book is already in the library
    if new_book in library:
        print("The book is already in the library. No duplicates allowed.")
    else:
        # Add the new book to the library if it's not a duplicate
        library.append(new_book)
        print("The book has been added to the library.")

# Example usage:
new_book_1 = ("The Catcher in the Rye", "J.D. Salinger")
new_book_2 = ("1984", "George Orwell")  # This is a duplicate

# Add the first new book
add_book(library, new_book_1)

# Try to add the duplicate book
add_book(library, new_book_2)

# Print the updated library
print("Updated Library:", library)