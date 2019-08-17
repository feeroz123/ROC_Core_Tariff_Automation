import logging
import cx_Oracle
from utilities import custom_logger as cl


class DBConnection:
    log = cl.custom_logging(logLevel=logging.DEBUG)

    def __init__(self):
        self.conn = None
        self.cursor = None

    def get_db_connection(self):
        try:
            db_user_name = 'rocref'  # Reference DB Username
            db_user_password = 'rocref'  # Reference DB Password
            db_sid = 'orcl'  # Reference DB Oracle SID
            db_host = 'localhost'  # Reference DB Host Machine
            db_port = '1521'  # Reference DB Oracle Port

            self.log.debug("Attempting database connection")
            conn_string = f"{db_user_name}/{db_user_password}@{db_sid}"
            self.conn = cx_Oracle.connect(conn_string)
            self.cursor = self.conn.cursor()
            self.log.info("Database connection established.")
        except:
            self.log.error("**** Database connection failed.")
        return self.cursor

    def execute_sql(self, query):
        try:
            cursor = self.get_db_connection()
            print(cursor)
            cursor.execute(query)
            for row in cursor:
                print(row)
        except:
            print("The connection to db has issues. Query couldn't be executed.")
        finally:
            self.cursor.close()
            self.conn.close()


db_conn = DBConnection()
db_conn.execute_sql("select * from element;")
