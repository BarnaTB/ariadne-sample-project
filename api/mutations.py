from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Book


@convert_kwargs_to_snake_case
def create_book_resolver(obj, info, title, author, isbn):
    try:
        new_book = Book(title=title, author=author, isbn=isbn)
        db.session.add(new_book)
        db.session.commit()
        payload = {
            "success": True,
            "book": new_book.serialize()
		}
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
