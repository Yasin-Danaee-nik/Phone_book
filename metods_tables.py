from coon_db import PostgresDB
class Metods_tables:
    def __init__(self):
        self.coon  = PostgresDB(host="localhost", database="phone_book", user="yasin", password="1234")
        self.coon.connect()
        
    def show_data_all(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                query_join = """
                SELECT 
                    *
                FROM 
                    users
                JOIN 
                    numbers
                    ON 
                    users.id = numbers.user_id
                """

                cur.execute(query_join)
                rows = cur.fetchall()
                for row in rows:
                    print(f"ID: {row[0]}, FRIST NAME: {row[1]}, LAST NAME: {row[2]}, ID PRSON: {row[3]}, COUNTRY CODE: {row[4]}, NUMBER {row[5]}")

                    
            except Exception as error:
                print(f"error! {error}")

    def insert_data_tbale_users(self, F_name, L_name):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()
                
                insert_data = "INSERT INTO users(F_name, L_name) VALUES(%s, %s)"
                cur.execute(insert_data,(F_name, L_name))
                self.coon.connection.commit()

                print(f"{F_name} {L_name} inserted.")

            except Exception as error:
                print(f"Error! {error}")
        
    def insert_data_table_numbers(self,user_id, number, country_code):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                insert_data = "INSERT INTO numbers(user_id, number, country_code) VALUES(%s, %s, %s)"
                cur.execute(insert_data,(user_id, number, country_code))
                self.coon.connection.commit()

                print(f"{country_code} {number} inserted.")

            except Exception as error:
                print(f"Errro! {error}")
    
    def show_table_users(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_show = "SELECT F_name, L_name FROM users"
                cur.execute(qurey_show)
                rows = cur.fetchall()
                for row in rows:
                    print(f"ID {row[0]} FRIST NAME {row[1]} LAST NAME {row[2]}")
            
            except Exception as error:
                print(f"error!: {error}")

    def show_table_numbers(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_show = "SELECT country_code, number FROM numbers"
                cur.execute(qurey_show)
                rows = cur.fetchall()
                for row in rows:
                    print(f"ID {row[0]} COUNTRY CODE {row[1]} NUMBER {row[2]}")
            
            except Exception as error:
                print(f"error!: {error}")

if __name__ == "__main__":
    main = Metods_tables()
    main.show_table_users()
