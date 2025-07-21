import psycopg2


class Database:
    def __init__(self):
        self.database = psycopg2.connect(
            dbname = 'films',
            password = 'Xumo0107',
            host = 'localhost',
            user = 'postgres',
            port = '5432'
        )

    def execute(self, sql, *args, commit: bool = False, fetchone: bool = False, fetchall: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                result = None
                if commit:
                    db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return  result

    def get_user(self, categoriy_id):
        sql = '''SELECT title, description FROM films WHERE categoriy_id = %s'''
        return self.execute(sql, categoriy_id, fetchone= True)
