# Phase Three Project: Book Store Management Application
## Overview
This is a comprehensive library management system designed to simplify book and library resource management. Developed as part of the Phase Three curriculum, this project leverages Python and SQLAlchemy to provide a robust web application for organizing and managing books, authors, genres, and publishers. Whether you're a student, librarian, or avid reader, the application offers an intuitive and feature-rich platform for efficient library operations.

## Table of Contents
* Features
* Project Structure
* Project Setup
* Technologies Used 
* Database Migrations
* License

## Features
1. Book Management.
 Add, Edit, and Delete Books: Easily manage books in the library, including details such as title, author, genre, and publisher.
 Comprehensive Book Information: Store additional information about each book, such as publication date, ISBN, and synopsis.

2. Author Information.
 Author Management: Keep track of authors and their works, including biographical information.

3. Genre Categorization.
 Genre Classification: Classify books into different genres for easy navigation and categorization.

4. Publisher Details.
Publisher Information: Manage details about publishers, including contact information and a list of associated books.


## Project Structure
The project follows a well-organized structure to maintain clarity and scalability:

```sh 
   Copy code 
   mylibrary/
  |-- alembic/
  |   |-- versions/
  |-- mylibrary/
  |   |-- cli.py
  |   |-- db.py
  |   |-- models.py
  |   |-- seed.py
  |   
  |-- .env
  |-- .gitignore
  |-- Pipfile
  |-- Pipfile.lock
  |-- README.md
```

alembic/: Database migration scripts to manage changes to the database schema.

mylibrary/: Main application package containing essential modules.

cli.py: Command-line interface commands for common tasks.

db.py: Database configuration and initialization module.

models.py: Defines SQLAlchemy models for database tables.

Pipfile and Pipfile.lock: Dependency management files.

README.md: Documentation file for the project.


## Project Setup
- Clone the repository: `git clone <repository-url>`
- Navigate to cloned repository: `cd Phase-3-CLI-project`
- Create pipenv environment and Install dependencies: `pipenv install && pipenv shell`

## Technologies Used

The following have been used on this project:

- [Python3](https://docs.python.org/3.10/)
- [Pytest](https://docs.pytest.org/en/latest/contents.html)
- [SQLAlchemy==1.4.42](https://docs.sqlalchemy.org/en/20/)
- [Alembic==1.8.1](https://alembic.sqlalchemy.org/en/latest/)
- [Faker==14.2.0](https://faker.readthedocs.io/en/master/)

## Create database migrations

- create db from migrations with alembic: `cd mylibrary && alembic updgrade head`
- populate db with `seed.py`: `python3 seed.py`

## License
Released under the MIT License. See the [LICENSE](https://github.com/Makanda254/Phase-3-CLI-project/blob/main/LICENSE) file.