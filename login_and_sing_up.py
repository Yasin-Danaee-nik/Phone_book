from coon_db import PostgresDB
from tabulate import tabulate

class Login:
    def __init__(self):
        self.coon  = PostgresDB(host="localhost", database="phone_book", user="yasin", password="1234")
        self.coon.connect()
    
    def login(self, F_name, L_name):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                self.F_name = str(F_name)
                if self.F_name is None:
                    print("Error! enter your Frist name.")
        
                self.L_name = str(L_name)
                if self.L_name is None:
                    print("error! enter youe last name.")
            except Exception as error:
                print(f"Error! {error}")
        
            qury_show = "SELECT id FROM users WHERE name = %s AND last_name = %s"
            cur.execute(qury_show,(F_name, L_name))
            rows = cur.fetchall()
            if not rows:
                raise ValueError(f"{F_name} {L_name} not found.")
            columns = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=columns, tablefmt="psql"))