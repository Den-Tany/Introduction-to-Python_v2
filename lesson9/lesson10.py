from sqlalchemy import create_engine, inspect, text

class SQL:
     
     scripts = {
            "add_new" : text(
                """
                INSERT INTO users("user_id", "user_email", "subject_id") 
                values (:user_id, :user_email, :subject_id)
                """
            ),
            "get_on_user_id" : text(
                """
                select *
                from users where user_id = :user_id
                """
            ),
            "delete_on_user_id" : text(
                """
                delete from users where user_id = :user_id
                """
            ),
            "patch_new" : text (
                """
                UPDATE users SET user_email = :user_email WHERE user_id = :user_id
                """
            )
        }

    
     def __init__(self):
        db_connection_string = "postgresql://postgres:4312Nfnz.@localhost:5432/postgres"  # Ввести путь к базе данных из Домашнего Задания - 1. Введение в SQL. Настройка окружения
        self.db = create_engine(db_connection_string)

     def add_user(self, user_id, user_email, subject_id):
        conn = self.db.connect()
        conn.execute(self.scripts["add_new"], {"user_id" : user_id, "user_email" : user_email, "subject_id" : subject_id})
        conn.commit()
        conn.close()
     
     def get_user(self, user_id):
        conn = self.db.connect()
        result = conn.execute(self.scripts["get_on_user_id"], {"user_id" : user_id})
        row = result.mappings().all()
        conn.close()
        return row
    
     def change_user(self, new_user_email, user_id):
        conn = self.db.connect()
        conn.execute(self.scripts["patch_new"], {"user_email" : new_user_email, "user_id" : user_id})
        conn.commit()
        conn.close()

     def delete_user(self, user_id):
        conn = self.db.connect()
        conn.execute(self.scripts["delete_on_user_id"], {"user_id" : user_id})
        conn.commit()
        conn.close()
