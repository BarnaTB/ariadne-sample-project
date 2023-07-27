from api.models import Book


def get_books_resolver(obj, info):
    """Resolver function to return all books

    Returns:
        dict: return type for all books
    """
    try:
        book_queryset = Book.query.all()
        books = [book.serialize() for book in book_queryset]
        payload = {
            "success": True,
            "books": books
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
