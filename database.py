import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path
    def crate_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Food_rating INTEGER,
            Cleanliness_rating INTEGER,
            Extra_comments TEXT
            )
            ''')
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO survey_results(name, food_rating, cleanliness_rating, extra_comments)
                    VALUES (?, ?, ?, ?,)
                """,
                (data["name"], data["rade"], data["rade_clean"], data["extra_comments"])
            )
