from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Book


@convert_kwargs_to_snake_case
def create_book_resolver(obj, info, title, author, isbn):
    """Resolver function to create a book

    Returns:
        dict: return type for the newly create product
    """
    try:
        new_book = Book(title=title, author=author, isbn=isbn)
        db.session.add(new_book)
        db.session.commit()
        payload = {
            "success": True,
            "errors": [],
            "book": new_book.serialize()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_book_resolver(obj, info, id):
    """Resolver function to delete a book

    Returns:
        dict: return type for the deleted product
    """
    try:
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        payload = {
            "success": True,
            "errors": [],
            "book": book.serialize()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
