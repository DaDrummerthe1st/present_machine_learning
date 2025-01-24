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

        # at first this did not need to run, it had update the database and made it possible to SELECT and get the information anyway
        db.commit()

        # only one row can be written per run in sqlite
        cursor.execute("""
                        INSERT INTO machines (machinetype) VALUES (
                            ('B52'))""")

        cursor.execute("""
                        INSERT INTO machines (machinetype) VALUES (
                            ('Nissan Micra'))""")

        cursor.execute("""
                        INSERT INTO machines (machinetype) VALUES (
                            ('Volvo Penta'))""")

        db.commit()

        query = """
                SELECT * FROM machines;
                """

        query_delete = """
                DROP TABLE IF EXISTS machines;
            """

        result = cursor.execute(query)
        result = result.fetchall()
        cursor.execute(query_delete)
        db.commit()

        cursor.close()
        db.close()

        return result
