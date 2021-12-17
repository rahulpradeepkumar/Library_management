from flask_login import UserMixin

from Library_Management_System import db

""" This model is for User - Students as well as Admin- Linked with books as fk """
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    book = db.relationship("Copy", backref="issue", lazy=True)
    admin = db.Column(db.Boolean, default=False)


""" This Model is for Book - Stores the book's details and count of it - linked with copy as fk """
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    author = db.Column(db.String(255))
    description = db.Column(db.Text)
    copy = db.relationship(
        "Copy", backref=db.backref("posts", lazy=True), cascade="all,delete"
    )
    total_copy = db.Column(db.Integer)
    issued_copy = db.Column(db.Integer)
    present_copy = db.Column(db.Integer)


""" This Model is to maintain the return/issue of the book in Book model - linked as book and copy as fk """
class Copy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime())
    issued_by = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=True, default=None
    )
    date_issued = db.Column(db.DateTime(), default=None)
    date_return = db.Column(db.DateTime(), default=None)
    book = db.Column(db.Integer, db.ForeignKey("book.id"))
