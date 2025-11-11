from metods_tables import Metods_tables
from login_and_sing_up import Login

if __name__ == "__main__":
    main = Metods_tables()
    main2 = Login()
    main.show_table_users()
    main2.login("ysassin", "danaee")