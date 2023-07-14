from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

import sqlite3

class UserService(ExecuteSQLService) :
# =========================================================CREATE=========================================================
    def create(self, user) :
        #log
        print('----------------------------service-user : create()')

        #domain
        user = user

        # uuid init, object property -> tuple
        id = user.id = mk_uuid()
        user_tuple = self.properties_to_tuple(user)

        #execute sql
        sql = "INSERT INTO user(id, name, gender, birthdate, age, address) VALUES (?, ?, ?, ?, ?, ?)"
        args = user_tuple
        self.execute_sql(DML.INSERT, sql, args)

        #return
        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-user : read_all()')
        
        #execute sql
        sql = "SELECT * FROM user"
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_name_gender(self, name, gender):
        #log
        print('----------------------------service-user : read_name_gender()')
        
        #execute sql
        result = None
        sql = f"SELECT * FROM user WHERE name LIKE '%{name}%' "
        if(gender != 'Both') :
            sql += "AND gender = ?"
            args = (gender,)
            result = self.execute_sql(DML.SELECT, sql, args)
        else :
            result = self.execute_sql(DML.SELECT, sql)    
        
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-user : read_id()')

        #execute sql
        sql = "SELECT * FROM user WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args)
        return result
    
    def read_order(self, id) :
        #log
        print('----------------------------service-user : read_order()')

        #execute sql
        sql = """
            SELECT o.id AS "order id", o.ordered_at AS "purchased date", s.id AS "purchased location"
            FROM "user" u
            JOIN "order" o ON u.id = o.user_id
            JOIN store s ON o.store_id = s.id
            WHERE o.id = ?
            ORDER BY o.ordered_at DESC
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args)
        return result

    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())