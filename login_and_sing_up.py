from coon_db import PostgresDB


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
        
            qury_show = "SELECT id FROM users WHERE F_name = %s AND L_name = %s"
            cur.execute(qury_show,(F_name, L_name))
            rows = cur.fetchall()
            
            for row in rows:
                print(f"ID: {row[0]}, FRIST NAME: {row[1]}, LAST NAME: {row[2]}")