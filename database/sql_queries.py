create_users_table_query = """
      CREATE TABLE  IF NOT EXISTS telegram_users
      (id INTEGER PRIMARY KEY ,
      username CHAR(50),
      first_name CHAR(50),
      last_name CHAR(50)
      )                          
"""

insert_user_query = """INSERT INTO telegram_users VALUES (?,?,?,?)"""

select_user_query = """SELECT username FROM telegram_users"""





create_ban_tabl = """
     CREATE TABLE list_of_ban
     (id INTEGER PRIMARY KEY ,
      username CHAR(50),
      first_name CHAR(50),
      last_name CHAR(50)
      )                  

"""

insert_ban = """ INSERT INTI list_of_ban VALUES (?,?,?,?)"""
