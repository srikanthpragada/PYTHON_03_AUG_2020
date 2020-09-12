import requests

id = input("Enter book id :")
price = input("Enter book price :")
resp = requests.put(f"http://localhost:8000/books/rest/books/{id}",
                    {'price': price})
if resp.status_code == 200:
    print("Book was updated successfully!")
elif resp.status_code == 404:
    print("Sorry! Book not found!")
else:
    print("Sorry! Could not update book due to error!")
