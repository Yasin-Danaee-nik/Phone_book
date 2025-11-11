from coon_db import PostgresDB
from tabulate import tabulate

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
                    users.id = numbers.number_id
                """

                cur.execute(query_join)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                print(tabulate(rows, headers=columns, tablefmt="psql"))
                    
            except Exception as error:
                print(f"error! {error}")

    def insert_data_tbale_users(self, F_name, L_name):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()
                
                insert_data = "INSERT INTO users(name, last_name) VALUES(%s, %s)"
                cur.execute(insert_data,(F_name, L_name))
                self.coon.connection.commit()

                print(f"{F_name} {L_name} inserted.")

            except Exception as error:
                print(f"Error! {error}")
        
    def insert_data_table_numbers(self,number_id, number, country_code):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                insert_data = "INSERT INTO numbers(number_id, number, country_code) VALUES(%s, %s, %s)"
                cur.execute(insert_data,(number_id, number, country_code))
                self.coon.connection.commit()

                print(f"{country_code} {number} inserted.")

            except Exception as error:
                print(f"Errro! {error}")
    
    def show_table_users(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_show = "SELECT id ,name, last_name FROM users"
                cur.execute(qurey_show)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                print(tabulate(rows, headers=columns, tablefmt="psql"))

            
            except Exception as error:
                print(f"error!: {error}")

    def show_table_numbers(self):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_show = "SELECT id, country_code, number FROM numbers"
                cur.execute(qurey_show)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                print(tabulate(rows, headers=columns, tablefmt="psql"))
                

            except Exception as error:
                print(f"error!: {error}")
        
    def delete_data_users(self, F_name, L_name):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_delete = "DELETE FROM users WHERE name = %s AND last_name = %s"
                cur.execute(qurey_delete,(F_name, L_name))
                rows = cur.rowcount
                self.coon.connection.commit()

                if rows > 0:
                    print(f"{F_name} {L_name} is deleted")
                
                else:
                    print(f"{F_name}, {L_name} not find!")
            
            except Exception as error:
                self.coon.connection.rollback()
                print(f"Error!: {error}")
        
    def delete_data_numbers(self, number, country_code):
        if self.coon:
            try:
                cur = self.coon.connection.cursor()

                qurey_delete = "DELETE FROM numbers WHERE country_code = %s AND number = %s"
            
                cur.execute(qurey_delete, (country_code, number))
                rows = cur.rowcount
                self.coon.connection.commit()

                if rows > 0:
                    print(f"({country_code}) {number} is deleted")
            
                else:
                    print(f"({country_code}) {number} not find!")
        
            except Exception as error:
                self.coon.connection.rollback()
                print(f"Error!: {error}")


if __name__ == "__main__":
    main = Metods_tables()
    main.show_data_all()