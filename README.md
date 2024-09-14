# 🎤 Concerts Domain Project 🎶

Welcome to the **Concerts Domain** project! This project simulates the relationships between bands, venues, and concerts using Python and SQLAlchemy.

## 📝 Project Overview

This application models a system where:

- A **Band** performs at multiple **Concerts** 🎸.
- A **Venue** hosts multiple **Concerts** 🎪.
- A **Concert** belongs to one **Band** and one **Venue**, creating a many-to-many relationship between bands and venues 🎶.

## 🛠️ Technologies Used

- **Python** 🐍
- **SQLAlchemy** 🗃️
- **SQLite** (via SQLAlchemy for the database) 🗄️
- **Alembic** for database migrations 📜

## 📂 Project Structure


## 📦 Models

The project includes three models:

- **Band** 🎤: Represents a musical band, with attributes `name` and `hometown`.
- **Venue** 🎪: Represents a venue where concerts are held, with attributes `title` and `city`.
- **Concert** 🎸: Represents a concert, with relationships to both `Band` and `Venue`, and a `date`.

### Band

- `name` (String): The name of the band.
- `hometown` (String): The hometown of the band.
- Relationships: Has many `Concerts`.

### Venue

- `title` (String): The title of the venue.
- `city` (String): The city where the venue is located.
- Relationships: Has many `Concerts`.

### Concert

- `band_id` (ForeignKey): The ID of the band performing.
- `venue_id` (ForeignKey): The ID of the venue hosting the concert.
- `date` (String): The date of the concert.
- Relationships: Belongs to one `Band` and one `Venue`.

## ⚙️ Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/concerts-domain.git
   cd concerts-domain

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install the dependencies:
    pip install -r requirements.txt

3. Apply migrations using Alembic:
    alembic upgrade head

4. Seed the database:
    python seed.py

## 🚀 Running Queries
    Run the test queries:
        python test_query.py

## 🎯 Features
    List all bands and the concerts they've performed 🎸.
    List all venues and the bands that performed there 🎪.
    Check if a concert is a hometown show for a band 🏠.
    Add new concerts and bands dynamically via the Python code 📝.

## 📈 Future Improvements
    Add more methods for complex querying and filtering 🧐.
    Implement a user interface to interact with the database visually 💻.


## 🎉 Conclusion
This project is a great introduction to SQLAlchemy relationships and object-oriented programming with Python. Feel free to build upon it and expand its functionality!

Happy Coding! 😎👨‍💻👩‍💻
