from api import app, db

from flask import jsonify, request
from flask.cli import FlaskGroup

from ariadne import (load_schema_from_path,
                     make_executable_schema,
                     graphql_sync,
                     snake_case_fallback_resolvers,
                     ObjectType)
from ariadne.constants import CONTENT_TYPE_TEXT_HTML
from api.queries import get_books_resolver
from api.mutations import create_book_resolver


cli = FlaskGroup(app)


query = ObjectType("Query")

mutation = ObjectType("Mutation")

query.set_field("getBooks", get_books_resolver)

mutation.set_field("createBook", create_book_resolver)

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
    )


@app.route("/graphql")
def graphql_playground():
    return CONTENT_TYPE_TEXT_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    if success:
        status_code = 200
    else:
        status_code = 400

    return jsonify(result), status_code


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
