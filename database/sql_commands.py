import sqlite3
from database import sql_queries, sql_ban_queries

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.create_user_table_query)
        self.connection.execute(sql_queries.create_user_form_table_query)
        self.connection.execute(sql_ban_queries.create_ban_table)
        self.connection.execute(sql_queries.create_answer_table)
        self.connection.commit()

    def sql_insert_user(self,telegram_id, username, first_name, last_name):
        self.cursor.execute(sql_queries.insert_user_query, (None,
                                                            telegram_id,
                                                            username,
                                                            first_name,
                                                            last_name))
        self.connection.commit()

    def sql_insert_user_form(self,user_id, telegram_id, nickname,
                             age, bio, gender, photo):
        self.cursor.execute(sql_queries.insert_user_form_query, (None,
                                                                user_id,
                                                                telegram_id,
                                                                nickname,
                                                                age,
                                                                bio,
                                                                gender,
                                                                photo))
        self.connection.commit()

    def sql_select_user_by_id(self,telegram_id):
        self.cursor.row_factory = lambda cursor, row: {'id': row[0]}
        return self.cursor.execute(sql_queries.select_user_by_id,(telegram_id,)).fetchall()


    def sql_answer_query(self,  id_user,username, quiz, quiz_option):
        self.cursor.execute(sql_queries.insert_answer_query, (id_user,
                                                              username,
                                                              quiz,
                                                              quiz_option
                                                            ))
        self.connection.commit()

    def sql_select_user(self):
        self.cursor.row_factory = lambda cursor, row: {'username': row[0]}
        return self.cursor.execute(sql_queries.select_user_query).fetchall()

    def sql_insert_ban_table(self,  username, id_group):
        self.cursor.execute(sql_ban_queries.insert_ban_table,(username,
                                                              id_group))
        self.connection.commit()

    def sql_select_ban_for_users(self, username, id_group):
        self.cursor.execute(sql_ban_queries.select_ban_for_users,(username,id_group)).fetchall()
