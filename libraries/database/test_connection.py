import sqlite3


class TestConnection:
    def __init__(self,
                 path_to_database = "resources/database/present_machine_learning.db"):
        self.path_to_database = path_to_database

    def connect(self):
        db = sqlite3.connect(self.path_to_database)

        cursor = db.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS machines (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        'machinetype');
                        """)

        cursor.execute("""
                INSERT INTO machines VALUES (
                1, 'B52')
                """)

        query = """
                SELECT * FROM machines;
                """

        query_delete = """
                DROP TABLE IF EXISTS machines;
            """

        result = cursor.execute(query)
        result = result.fetchall()
        return result
