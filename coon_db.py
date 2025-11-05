import psycopg2


class PostgresDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("coon = ok")
        except Exception as e:
            print(e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("coon == off")

if __name__ == "__main__":
    db = PostgresDB(host="localhost", database="tamrin", user="yasin", password="1234")
    db.connect()
    db.close()