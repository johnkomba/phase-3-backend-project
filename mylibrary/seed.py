from faker import Faker
from models import Author
from models import Genre
from models import Publisher
from models import Book
from db import SessionLocal, init_db

fake = Faker()

def seed_data():
    db = SessionLocal()

    try:
        # Create sample authors
        author_names = [fake.name() for _ in range(50)]
        authors = [Author(name=name) for name in author_names]
        db.add_all(authors)
        db.commit()

        # Create sample genres
        genre_names = [fake.word() for _ in range(50)]
        genres = [Genre(name=name) for name in genre_names]
        db.add_all(genres)
        db.commit()

        # Create sample publishers
        publisher_names = [fake.company() for _ in range(50)]
        publishers = [Publisher(name=name) for name in publisher_names]
        db.add_all(publishers)
        db.commit()

        # Create sample books
        for _ in range(50):
            title = fake.catch_phrase()
            author = fake.random_element(authors)
            genre = fake.random_element(genres)
            publisher = fake.random_element(publishers)

            book = Book(title=title, author=author, genre=genre, publisher=publisher)
            db.add(book)
        db.commit()

        print("Database seeded successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    seed_data()
