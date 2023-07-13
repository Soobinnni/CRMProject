import sqlite3
from enum import Enum

class DML(Enum):
    SELECT = "SELECT"
    SELECTONE = "SELECTONE"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
class ExecuteSQLService:
    def get_conn_cursor(self) :
        conn = sqlite3.connect("db/crm.db")
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        return conn, cursor
    
    def execute_sql(self, type_, sql, args = None) :
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        result = None

        # dml분류
        if (type_ == DML.SELECT) or (type_ == DML.SELECTONE) :
            result = None
            if type_ == DML.SELECT :
                result = self.fetchall_as_dict(cursor, sql, args)
            else : 
                result = self.fetchone_as_dict(cursor, sql, args)
            conn.close()
            return result
        else :
            #execute sql
            cursor.execute(sql, args)
            conn.commit()

        #connect close
        conn.close()

    def fetchall_as_dict(self, cursor, sql, args):
        if args != None:
            cursor.execute(sql, args)
        else : 
            cursor.execute(sql)
        columns = [column[0] for column in cursor.description]  #[컬럼명, ...]
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))  # key : value = column : column value
        return result

    def fetchone_as_dict(self, cursor, sql, args):
        cursor.execute(sql, args)

        columns = [column[0] for column in cursor.description]  #[컬럼명, ...]
        row = cursor.fetchone()
        result = {}
        for i, r in enumerate(row):
            result[columns[i]] = r  # key : value = column : column value
        return result