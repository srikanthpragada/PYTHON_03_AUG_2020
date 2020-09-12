import requests

id = input("Enter Book id :")
resp = requests.get(f"http://localhost:8000/books/rest/books/{id}")
if resp.status_code == 200:
    book = resp.json()
    print(f"{book['id']} - {book['title']}  - {book['author']} - {book['price']}")
else:  # status 404
    print("Sorry! Book not found!")
