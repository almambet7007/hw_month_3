import sqlite3
from database import sql_queries

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.create_users_table_query)
        self.connection.commit()

    def sql_insert_users(self, username, first_name, last_name):
        self.cursor.execute(sql_queries.insert_user_query, (None,
                                                            username,
                                                            first_name,
                                                            last_name))
        self.connection.commit()