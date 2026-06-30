from fastapi import FastAPI
app = FastAPI()
books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]
@app.get("/books/statistics")
def get_book_static():
    total_book = len(books)
    available_book = len([book for book in books if book['is_available'] == True])
    book_borrow = len([book for book in books if book['is_available'] == False])
    return {
        "total_books":total_book,
        "available_book":available_book,
        "book_borrow":book_borrow
    }
@app.get("/books/categories")
def get_category_book():
    unique_category = list(set(book['category'] for book in books))
    return {"category":unique_category}
@app.get("/books/latest")
def get_late_book():
    if not books:
        return {"message":"No books available"}
    late_book = max(books,key=lambda book:book['year'])
    return late_book