from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import Content, User
from app import db

main = Blueprint('main', __name__)

# -----------------------
# Dashboard (View All)
# -----------------------
@main.route('/dashboard')
@login_required
def dashboard():
    search = request.args.get('search', '')

    if search:
        posts = Content.query.filter(Content.title.contains(search)).all()
    else:
        posts = Content.query.all()

    total_posts = Content.query.count()
    total_users = User.query.count()

    return render_template(
        'dashboard.html',
        posts=posts,
        total_posts=total_posts,
        total_users=total_users
    )

# -----------------------
# Add Content (Admin, Editor)
# -----------------------
@main.route('/content/add', methods=['GET', 'POST'])
@login_required
def add_content():
    if current_user.role not in ['admin', 'editor']:
        flash('You are not allowed to add content')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        post = Content(
            title=request.form['title'],
            body=request.form['body'],
            author=current_user.username,
            status='published'
        )

        db.session.add(post)
        db.session.commit()
        flash('Content added successfully')
        return redirect(url_for('main.dashboard'))

    return render_template('add_content.html')

# -----------------------
# Edit Content (Admin, Editor)
# -----------------------
@main.route('/content/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_content(id):
    if current_user.role not in ['admin', 'editor']:
        flash('You are not allowed to edit content')
        return redirect(url_for('main.dashboard'))

    post = Content.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        db.session.commit()
        flash('Content updated successfully')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_content.html', post=post)

# -----------------------
# Delete Content (Admin ONLY)
# -----------------------
@main.route('/content/delete/<int:id>')
@login_required
def delete_content(id):
    if current_user.role != 'admin':
        flash('You are not allowed to delete content')
        return redirect(url_for('main.dashboard'))

    post = Content.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Content deleted successfully')
    return redirect(url_for('main.dashboard'))
