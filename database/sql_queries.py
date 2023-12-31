



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

select_user_form = """SELECT * FROM user_form"""

select_user_form_by_id = """SELECT * FROM user_form AS form
    LEFT JOIN telegram_users AS user ON form.user_id = user.id
    WHERE form.id = ?"""

insert_user_query = """INSERT OR IGNORE INTO telegram_users VALUES (?, ?, ?, ?, ?)"""

insert_user_form_query = """INSERT  INTO user_form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

select_user_query = """SELECT username FROM telegram_users"""

select_user_by_id = """SELECT id FROM telegram_users WHERE telegram_id = ?"""

select_user_form_by_telegram_id = """SELECT telegram_id FROM user_form WHERE telegram_id = ?"""

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

create_table_for_complain = """
        CREATE TABLE IF NOT EXISTS complain_users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username CHAR(50),
        telegram_id INTEGER,
        telegram_id_bad_user INTEGER,
        reason TEXT,
        count INTEGER,
        FOREIGN KEY (telegram_id) REFERENCES telegram_users (telegram_id),
        FOREIGN KEY (telegram_id_bad_user) REFERENCES telegram_users (id))
        """

insert_complain_users = """INSERT  INTO complain_users(username, telegram_id, telegram_id_bad_user, reason, count) 
VALUES (?, ?, ?, ?, ?)"""


select_complain_users_table = """ SELECT count FROM complain_users WHERE telegram_id_bad_user = ?"""

select_complain_users_table_check = """
    SELECT telegram_id FROM complain_users WHERE telegram_id = ? AND telegram_id_bad_user = ?
"""

cteate_table_for_scraper_lukizm ="""
       CREATE TABLE IF NOT EXISTS scraper_table_lukizm
       (id INTEGER PTYMARY KEY AUOTOINCREMENT,
       id_user INTEGER,
       one_manga CHAR(50),             
       two_manga CHAR(50),        
       three_manga CHAR(50),         
       four_manga CHAR(50),        
       five_manga CHAR(50) ,      
       FOREIGN KEY (id_user) REFERENCES telegram_users (id),
       UNIQUE(id_user,one_manga,two_manga,three_manga,four_manga, five_manga ))

"""

insert_scraper_lukizm = """
    INSERT OR IGNORE INTO scraper_table_lukizm(id_user,one_manga,two_manga,three_manga,four_manga, five_manga   ) 
    VALUES (?, ?, ?, ?, ?, ?)
"""

select_scraper_lukizm = """
    SELECT id_user,one_manga,two_manga,three_manga,four_manga, five_manga FROM scraper_table_lukizm WHERE id_user = ?
"""