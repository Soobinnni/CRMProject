from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

import sqlite3

class UserService(ExecuteSQLService) :
# =========================================================CREATE=========================================================
    def create(self, user) :
        user = user #domain

        id = user.id = mk_uuid() # uuid init
        user_tuple = self.properties_to_tuple(user) # object property -> tuple
        
        sql = "INSERT INTO user(id, name, gender, birthdate, age, address) VALUES (?, ?, ?, ?, ?, ?)"
        args = user_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        sql = "SELECT * FROM user"
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_kwargs(self, **kwargs):
        where_sentence, where_args = self.mk_where_condition(kwargs)
        sql = f"""SELECT * FROM user WHERE {where_sentence}"""
        result = self.execute_sql(DML.SELECT, sql, where_args) #execute sql

        return result
    
    def read_name_gender(self, name, gender):
        result = None
        sql = "SELECT * FROM user WHERE name LIKE ? "
        if(gender != 'Both') :
            sql += "AND gender = ?"
            args = (f"%{name}%",gender)
            result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        else :
            args = (f"%{name}%",)
            result = self.execute_sql(DML.SELECT, sql, args) #execute sql   
        
        return result
    
    def read_id(self, id):
        #execute sql
        sql = "SELECT * FROM user WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result
    
    def read_order(self, id) :
        sql = """
            SELECT o.id AS "order id", o.ordered_at AS "purchased date", s.id AS "purchased location"
            FROM "user" u
            JOIN "order" o ON u.id = o.user_id
            JOIN store s ON o.store_id = s.id
            WHERE u.id = ?
            ORDER BY o.ordered_at DESC
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result

    
# =========================================================etc=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())