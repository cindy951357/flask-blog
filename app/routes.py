# flask-blog/app/routes.py
from flask import Blueprint, Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db

api = Blueprint('api', __name__)

from app.models import Author, Article, ArticleSection, ArticleComment, ArticleLike

# @api.route('/test-db', methods=['GET'])
# def test_db():
#     try:
#         db.session.execute('SELECT 1')
#         return "Database connection successful!", 200
#     except Exception as e:
#         return f"Database connection failed: {str(e)}", 500


@api.route('/test', methods=['GET'])
def test():
    return "Server is running!"

# Route: GET /authors
@api.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

# Route: GET /authors/<id>
@api.route('/authors/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get_or_404(id)
    return jsonify(author.to_dict())

# Route: POST /authors
@api.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    new_author = Author(**data)
    db.session.add(new_author)
    db.session.commit()
    return jsonify(new_author.to_dict()), 201

# Route: PUT /authors/<id>
@api.route('/authors/<int:id>', methods=['PUT'])
def update_author(id):
    author = Author.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(author, key, value)
    db.session.commit()
    return jsonify(author.to_dict())

# Route: DELETE /authors/<id>
@api.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return '', 204

# Repeat similar CRUD patterns for articles, article_sections, article_comments, and article_likes.
