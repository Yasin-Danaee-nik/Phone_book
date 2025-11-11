from coon_db import PostgresDB

class Tables:
    def __init__(self):
        self.coon  = PostgresDB(host="localhost", database="phone_book", user="yasin", password="1234")
        self.coon.connect()
    
    def table_users(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                create_table = """CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                F_name VARCHAR(32) NOT NULL,
                L_name VARCHAR(32) NOT NULL
                )"""

                cur.execute(create_table)
                self.coon.connection.commit()

                print("table users = ok")
            
            except Exception as error:
                print(f"error! {error}")
    
    def table_numbers(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                create_table = """CREATE TABLE IF NOT EXISTS numbers(
                id SERIAL PRIMARY KEY,
                number_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
                country_code CHAR(3) NOT NULL,
                number VARCHAR(10) NOT NULL UNIQUE
                )"""

                cur.execute(create_table)
                self.coon.connection.commit()

                print("table numbers = ok")
            
            except Exception as error:
                print(f"error! {error}")
    

if __name__ == "__main__":
    user = Tables()
    user.table_users()
    user.table_numbers()