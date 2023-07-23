create_ban_table = """
         CREATE TABLE IF NOT EXISTS ban_list
         (id INTEGER PRIMARY KEY,
         username CHAR(50),
         id_group INTEGER,
         datetime DATETIME DEFAULT (datetime('now', '+6 hours')) NOT NULL)
         """

insert_ban_table = """INSERT INTO ban_list(username,id_group) VALUES (?,?)"""
select_ban_for_users = """SELECT username FROM ban_list WHERE username = ? AND id_group = ? AND datetime('now', '-18 hours') < datetime('now', '+6 hours')"""
