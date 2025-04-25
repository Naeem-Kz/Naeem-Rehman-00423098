import os
import json

LIBRARY_FILE = "library.txt"

# Load existing library from file (if it exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save current library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("❌ Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added successfully!")

# Remove a book from the library by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for books by title or author
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    query = input("Enter the search term: ").strip().lower()

    results = []
    if choice == "1":
        results = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if query in book["author"].lower()]
    else:
        print("❌ Invalid choice.")
        return

    if results:
        print("\n📚 Matching Books:")
        display_books(results)
    else:
        print("❌ No matching books found.")

# Display all books in the library
def display_books(library):
    if not library:
        print("📂 Your library is empty.")
    else:
        for i, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Show statistics about the library
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("📊 No books in your library.")
        return
    read_count = sum(1 for book in library if book["read"])
    percentage_read = (read_count / total) * 100
    print(f"📘 Total books: {total}")
    print(f"✅ Percentage read: {percentage_read:.1f}%")

# Main program loop
def main():
    library = load_library()

    while True:
        print("\n📚 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
