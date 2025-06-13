import sqlite3 as sq

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS lek_sr")
    cur.execute("""CREATE TABLE IF NOT EXISTS lek_sr (
    lek_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    to_use TEXT NOT NULL,
    kolvo INTEGER NOT NULL,
    price INTEGER NOT NULL,
    country_p TEXT NOT NULL
    )""")
    info =[
        (1, 'prep1', 'Таблетка', 30, 450, 'Россия'),
        (2, 'prep2', 'Таблетка', 23, 430, 'Таджикистан'),
        (3, 'prep3', 'Таблетка', 30, 210, 'Узбекистан'),
        (4, 'prep4', 'Капсула', 21, 322, 'Польша'),
        (5, 'prep5', 'Укол', 42, 432, 'Франция'),
        (6, 'prep6', 'Ингаляция', 51, 600, 'Болгария'),
        (7, 'prep7', 'Капсула', 32, 3222, 'Еврения'),
        (8, 'prep8', 'Таблетка', 99, 822, 'Румыния'),
        (9, 'prep9', 'Укол', 41, 2111, 'Африка'),
        (10, 'prep10', 'Капсула', 61, 777, 'Колумбия')
    ]

    cur.executemany("INSERT INTO lek_sr VALUES (?, ?, ?, ?, ?, ?)", info)
    #cur.execute("SELECT * FROM lek_sr")
    #print(cur.fetchall())

    cur.execute("SELECT * FROM lek_sr WHERE price < 500")
    print(cur.fetchall())
    cur.execute("SELECT * FROM lek_sr WHERE to_use = 'Таблетка'")
    print(cur.fetchall())
    cur.execute("SELECT * FROM lek_sr WHERE kolvo < 50")
    print(cur.fetchall())

    cur.execute("UPDATE lek_sr SET price = 1000 WHERE country_p = 'Болгария'")
