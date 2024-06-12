import sqlite3


class Database:
    def __init__(self):
        self.db_name = "app/eshopDatabase.db"
        self.conn = None
        self.cursor = None
        self.connect()
        #self.cursor.execute("DROP TABLE products")

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            #print(f"Connected to database: {self.db_name}")
            return self.conn
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def commit(self):
        if self.conn:
            self.conn.commit()
            print("Database connection commited.")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def insert(self, query, params):
        if self.conn and self.cursor:
            self.cursor.execute(query, params)
            self.conn.commit()
            #self.conn.close()
            return self.cursor.lastrowid

    def select(self, query):
        if self.conn and self.cursor:
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def onselect(self, query, params):
        if self.conn and self.cursor:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

    def update(self, query):
        if self.conn and self.cursor:
            self.cursor.execute(query)
            return True

    def delete(self, query):
        if self.conn and self.cursor:
            self.cursor.execute(query)
            return True

    def crate_table(self, query):
        if self.conn and self.cursor:
            self.cursor.execute(query)
            return True

    def drop_table(self, query):
        if self.conn and self.cursor:
            self.cursor.execute(query)
            return True
