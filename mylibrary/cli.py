import click
from faker import Faker
from models import Author,Genre, Publisher, Book
from db import SessionLocal, init_db

fake = Faker()

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.option('--title', prompt='Book Title', help='Title of the book')
@click.option('--author', prompt='Author Name', help='Name of the author')
@click.option('--genre', prompt='Genre Name', help='Genre of the book')
@click.option('--publisher', prompt='Publisher Name', help='Name of the publisher')
def create_book(title, author, genre, publisher):
    """Create a new book with a random author, genre, and publisher."""
    db = SessionLocal()

    try:
        author_obj = Author(name=author)
        db.add(author_obj)
        db.commit()

        genre_obj = Genre(name=genre)
        db.add(genre_obj)
        db.commit()

        publisher_obj = Publisher(name=publisher)
        db.add(publisher_obj)
        db.commit()

        book_obj = Book(title=title, author=author_obj, genre=genre_obj, publisher=publisher_obj)
        db.add(book_obj)
        db.commit()

        db.refresh(book_obj)
        click.echo(f"Book '{title}' by {author_obj.name} in the genre '{genre_obj.name}' published by '{publisher_obj.name}' created with ID: {book_obj.id}")

    except Exception as e:
        db.rollback()
        click.echo(f"Error: {e}")
    finally:
        db.close()
@cli.command()
def read_book():
    """Read all books from the database."""
    db = SessionLocal()

    try:
        books = db.query(Book).all()
        if not books:
            click.echo("No books found.")
        else:
            for book in books:
                click.echo(f"ID: {book.id}, Title: {book.title}, Author: {book.author.name}, Genre: {book.genre.name}, Publisher: {book.publisher.name}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        db.close()
        
@cli.command()
def get_authors():
    """Get names of all authors."""
    db = SessionLocal()

    try:
        authors = db.query(Author).all()
        if not authors:
            click.echo("No authors found.")
        else:
            for author in authors:
                click.echo(f"Author Name: {author.name}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        db.close()

@cli.command()
@click.argument('book_id', type=int)
@click.option('--title', help='New title of the book')
@click.option('--author', help='New author of the book')
@click.option('--genre', help='New genre of the book')
@click.option('--publisher', help='New publisher of the book')
def update_book(book_id, title, author, genre, publisher):
    """Update book information by providing its ID."""
    db = SessionLocal()

    try:
        book = db.query(Book).filter_by(id=book_id).first()
        if book:
            if title:
                book.title = title
            if author:
                author_obj = db.query(Author).filter_by(name=author).first()
                if not author_obj:
                    author_obj = Author(name=author)
                    db.add(author_obj)
                    db.commit()
                book.author = author_obj
            if genre:
                genre_obj = db.query(Genre).filter_by(name=genre).first()
                if not genre_obj:
                    genre_obj = Genre(name=genre)
                    db.add(genre_obj)
                    db.commit()
                book.genre = genre_obj
            if publisher:
                publisher_obj = db.query(Publisher).filter_by(name=publisher).first()
                if not publisher_obj:
                    publisher_obj = Publisher(name=publisher)
                    db.add(publisher_obj)
                    db.commit()
                book.publisher = publisher_obj

            db.commit()
            db.refresh(book)
            click.echo(f"Book information updated successfully.")
        else:
            click.echo('Book not found.')
    except Exception as e:
        db.rollback()
        click.echo(f"Error: {e}")
    finally:
        db.close()

@cli.command()
@click.argument('book_id', type=int)
def retrieve_book_by_id(book_id):
    """Retrieve a book by providing its ID."""
    db = SessionLocal()

    try:
        book = db.query(Book).filter_by(id=book_id).first()
        if book:
            click.echo(f"Book found: ID: {book.id}, Title: {book.title}, Author: {book.author.name}, Genre: {book.genre.name}, Publisher: {book.publisher.name}")
        else:
            click.echo('Book not found.')
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        db.close()
        
@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    """Delete a book from the database using its ID."""
    db = SessionLocal()

    try:
        book = db.query(Book).filter_by(id=book_id).first()
        if book:
            db.delete(book)
            db.commit()
            click.echo(f'Book with ID {book_id} deleted successfully.')
        else:
            click.echo('Book not found.')
    except Exception as e:
        db.rollback()
        click.echo(f"Error: {e}")
    finally:
        db.close()

@cli.command()
def seed():
    """Seed the database with sample data."""
    from seed import seed_data
    seed_data()

if __name__ == "__main__":
    cli()
