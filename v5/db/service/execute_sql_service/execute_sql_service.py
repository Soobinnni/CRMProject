import sqlite3
from enum import Enum

DATABASE = 'db/crm.db'
class DML(Enum) :
    SELECT = "SELECT"
    SELECTONE = "SELECTONE"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    
class ExecuteSQLService:
    def get_conn_cursor(self) :
        conn = sqlite3.connect("db/crm.db")
        conn.row_factory = sqlite3.Row  
        cursor = conn.cursor()

        return conn, cursor
    
    def execute_sql(self, type_, sql, args = None) :
        conn, cursor = self.get_conn_cursor() # get conn, cursor
        if args != None :
            cursor.execute(sql, args)
        else : 
            cursor.execute(sql)

        result = None
        if type_ == DML.SELECT :
            result = [dict(element) for element in cursor.fetchall()]
        elif type_ == DML.SELECTONE :
            result = dict(cursor.fetchone())
        else : 
            conn.commit()       
        conn.close()

        return result