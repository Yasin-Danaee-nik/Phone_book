from metods_tables import Metods_tables
from login_and_sing_up import Login

if __name__ == "__main__":
    main = Metods_tables()
    main2 = Login()
    #main.insert_data_tbale_users("yasin", "danaee")
    main.show_data_all()
    main2.login("yasin", "danaee")