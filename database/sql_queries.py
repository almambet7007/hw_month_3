create_user_table_query = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (id INTEGER PRIMARY KEY,
        telegram_id INTEGER,
        username CHAR(50),
        first_name CHAR(50), 
        last_name CHAR(50),
        UNIQUE(telegram_id))

"""

create_user_form_table_query = """
        CREATE TABLE IF NOT EXISTS user_form
        (id INTEGER PRIMARY KEY,
        user_id INTRGER NOT NULL,
        telegram_id INTEGER,
        nickname CHAR(50), 
        age INTEGER,
        bio TEXT,
        gender TEXT,
        idea CHAR(50),
        problems Char(50),
        place CHAR(50),
        photo TEXT,
        FOREIGN KEY (telegram_id) REFERENCES telegram_users (telegram_id),
        FOREIGN KEY (user_id) REFERENCES telegram_users (id) )

"""


insert_user_query = """INSERT OR IGNORE INTO telegram_users VALUES (?, ?, ?, ?, ?)"""

insert_user_form_query = """INSERT  INTO user_form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

select_user_query = """SELECT username FROM telegram_users"""

select_user_by_id = """SELECT id FROM telegram_users WHERE telegram_id = ?"""

create_answer_table = """
        CREATE TABLE IF NOT EXISTS user_answers_in_victory
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_user CHAR(50),
        username CHAR(50),
        quiz CHAR(50), 
        quiz_option INTEGER,
        FOREIGN KEY (id_user) REFERENCES telegram_users (id))

"""

insert_answer_query = """INSERT INTO user_answers_in_victory(id_user, username, quiz, quiz_option) VALUES (?,?,?,?)"""
