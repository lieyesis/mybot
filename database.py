import sqlite3




class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                instagram_username TEXT,
                food_rating INTEGER,
                cleanliness_rating INTEGER,
                visit_date DATE
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS meals(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price FLOAT,
                photo TEXT,
                receipt TEXT,
                category TEXT
                )
            """)
            conn.commit()

    def save_survey(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO reviews(name, instagram_username,food_rating, cleanliness_rating, visit_date )
                VALUES (?,?,?,?,?)
                """,
                (data['name'], data['instagram_username'],data['food_rating'], data['cleanliness_rating'],data['visit_date'])
            )
            conn.commit()

    def save_meal(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO meals(name, price, photo, receipt, category)
                VALUES (?,?,?,?,?)
                """,
                (data['name'], data['price'],data['photo'],data['reciept'], data['category'])
            )
            conn.commit()

    def get_all_meals(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * FROM meals")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]

    def get_meals_by_price(self):
        with sqlite3.connect(self.path) as conn:
            conn.row_factory = sqlite3.Row 
            result = conn.execute("""
            SELECT * FROM meals
            ORDER BY price ASC;
            """)
            data = result.fetchall()
            return [dict(row) for row in data]

