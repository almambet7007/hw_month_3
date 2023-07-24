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
        self.connection.execute(sql_queries.create_table_for_complain)
        self.connection.commit()


    def sql_insert_complain_users(self, username, telegram_id,
                                  telegram_id_bad_user, reason,count):
        self.cursor.execute(sql_queries.insert_complain_users,(
                                                               username,
                                                               telegram_id,
                                                               telegram_id_bad_user,
                                                               reason,
                                                               count
                                                                  ))
        self.connection.commit()

    def sql_select_complain_users(self, user_id):
        self.cursor.row_factory = lambda cursor, row: {"count": row[0]}
        return self.cursor.execute(sql_queries.select_complain_users_table, (user_id,))

    def sql_select_complain_users_table_check(self, user_id, bad_user_id):
        self.cursor.row_factory = lambda cursor, row: {"count": row[0]}
        return self.cursor.execute(sql_queries.select_complain_users_table_check, (user_id, bad_user_id,))

    def sql_insert_user(self,telegram_id, username, first_name, last_name):
        self.cursor.execute(sql_queries.insert_user_query, (None,
                                                            telegram_id,
                                                            username,
                                                            first_name,
                                                            last_name))
        self.connection.commit()

    def sql_insert_user_form(self,user_id, telegram_id, nickname,
                             age, bio, gender, idea,problems,place,photo):
        self.cursor.execute(sql_queries.insert_user_form_query, (None,
                                                                 user_id,
                                                                 telegram_id,
                                                                 nickname,
                                                                 age,
                                                                 bio,
                                                                 gender,
                                                                 idea,
                                                                 problems,
                                                                 place,
                                                                 photo))
        self.connection.commit()

    def sql_select_user_form(self):
        self.cursor.row_factory = lambda cursor, row: {'id': row[0]}
        self.cursor.row_factory = lambda cursor, row: {'user_id': row[1]}
        self.cursor.row_factory = lambda cursor, row: {'telegram_id': row[2]}
        self.cursor.row_factory = lambda cursor, row: {'nickname': row[3]}
        self.cursor.row_factory = lambda cursor, row: {'age': row[4]}
        self.cursor.row_factory = lambda cursor, row: {'bio': row[5]}
        self.cursor.row_factory = lambda cursor, row: {'gender': row[6]}
        self.cursor.row_factory = lambda cursor, row: {'idea': row[7]}
        self.cursor.row_factory = lambda cursor, row: {'problems': row[8]}
        self.cursor.row_factory = lambda cursor, row: {'place': row[9]}
        self.cursor.row_factory = lambda cursor, row: {'photo': row[10]}
        return self.cursor.execute(sql_queries.select_user_form).fetchall()


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
