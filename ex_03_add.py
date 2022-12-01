import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_project(conn, projekt):
   """
   Create a new project into the projects table
   :param conn:
   :param projekt:
   :return: project id
   """
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projekt)
   conn.commit()
   return cur.lastrowid

def add_task(conn, task):
   """
   Create a new task into the tasks table
   :param conn:
   :param task:
   :return: task id
   """
   sql = '''INSERT INTO tasks(projekt_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   projekt = ("Porządki domowe", "2022-11-12 00:00:00", "2022-11-12 00:00:00")

   conn = create_connection("baza_danych.db")
   pr_id = add_project(conn, projekt)

   task = (
       pr_id,
       "Ogarnięcie domu przed przyjadem rodziny",
       "Zrobienie zakupów, posprzatanie łazienki, wyniesienie śmieci",
       "started",
       "2022-11-12 12:00:00",
       "2022-11-12 15:00:00"
   )

   task_id = add_task(conn, task)

   print(pr_id, task_id)
   conn.commit()