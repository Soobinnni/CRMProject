import uuid
from db.service.execute_sql_service.SQLBuilder import SQLBuilder
from db.service.execute_sql_service.execute_sql_service import DML

import sqlite3

class UserSQLBuilder(SQLBuilder) :
# =========================================================CREATE=========================================================
    def create(self, user) :
        user = user #domain

        id = user.id = str(uuid.uuid4()) # uuid init
        user_tuple = tuple(user.__dict__.values()) # object property -> tuple
        
        sql = "INSERT INTO user(id, name, gender, birthdate, age, address) VALUES (?, ?, ?, ?, ?, ?)"
        args = user_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
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