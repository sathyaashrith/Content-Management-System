from flask import Blueprint, request, jsonify
from app.models import Content
from app import db

api = Blueprint('api', __name__)

# -----------------------
# GET all posts
# -----------------------
@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Content.query.all()
    data = []

    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': post.author,
            'status': post.status,
            'created_at': post.created_at
        })

    return jsonify(data)

# -----------------------
# GET single post
# -----------------------
@api.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Content.query.get_or_404(id)

    return jsonify({
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author': post.author,
        'status': post.status,
        'created_at': post.created_at
    })

# -----------------------
# CREATE post
# -----------------------
@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    post = Content(
        title=data['title'],
        body=data['body'],
        author='Postman',     # ✅ FIXED
        status='published'
    )

    db.session.add(post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully via Postman'}), 201


# -----------------------
# UPDATE post
# -----------------------
@api.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Content.query.get_or_404(id)
    data = request.get_json()

    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)

    db.session.commit()

    return jsonify({'message': 'Post updated successfully'})

# -----------------------
# DELETE post
# -----------------------
@api.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Content.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return jsonify({'message': 'Post deleted successfully'})
