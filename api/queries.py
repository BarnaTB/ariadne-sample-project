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


def get_book_by_id_resolver(obj, info, id):
    """Resolver function to return a single book using its id

    Returns:
        dict: dictionary containing the success status, and
        the serialized book object
    """
    try:
        book = Book.query.get_or_404(id)
        payload = {
            "success": True,
            "book": book.serialize(),
        }
    except Exception as err:
        payload = {
            "success": False,
            "errors": [str(err)],
        }
    return payload
