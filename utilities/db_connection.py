"""
Sample implementation:
    db_conn = DBConnection()
    result = db_conn.execute_sql("select * from element_set")
    print(result)
"""

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
            conn_string = f"{db_user_name}/{db_user_password}@{db_sid}"

            self.log.info("Attempting database connection")
            self.conn = cx_Oracle.connect(conn_string)
            self.cursor = self.conn.cursor()
            self.log.info("Database connection established.")
        except:
            self.log.exception("**** Database connection failed.")
        return self.cursor

    def execute_sql(self, query):
        try:
            cursor = self.get_db_connection()
            results = cursor.execute(query)
            query_result = [row for row in results]    # Populating every row from query results using List Comprehension method
            self.log.debug("Executed SQL query: " + query)
        except cx_Oracle.DatabaseError:
            self.log.exception("**** The connection to db has issues. Query couldn't be executed.")
        except cx_Oracle.InterfaceError:
            self.log.exception("**** Database connection is not open")
        finally:
            return query_result
            self.cursor.close()
            self.conn.close()
            self.log.debug("Database connection is closed")
