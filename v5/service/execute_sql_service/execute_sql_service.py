import sqlite3
from enum import Enum

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
    
    def mk_where_condition(self, condition_dict) :
        where_sentence = " "
        where_args = ()
        for key, value in condition_dict.items() : 
            if(value) :
                if "like_" in key :
                    where_sentence += key.replace("like_", "") + " LIKE ? AND "
                    where_args += (f"%{value}%",)
                else :
                    where_sentence += key + ' = ? AND '
                    where_args += (value, )
        where_sentence = where_sentence[0:-5] #TODO: 좋은 방법 같지 않음.. AND를 자르기 위함

        return where_sentence, where_args
