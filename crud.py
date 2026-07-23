from sqlalchemy.orm import Session

from models import User, Book
def create_user(db, username, password):
    user = User(
        username=username,
        password=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(db, username):
    return db.query(User).filter(
        User.username == username
    ).first()


def create_book(db, title, author, owner_id):
    book = Book(
        title=title,
        author=author,
        owner_id=owner_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book