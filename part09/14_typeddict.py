from typing import TypedDict

class Book(TypedDict):
    title: str
    pages: int

book: Book = {"title": "생각하는 파이썬",
              "pages": "480"}
print(book["page"])
