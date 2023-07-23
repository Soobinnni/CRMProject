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
        
        sql = "INSERT INTO user(login_id, login_pwd, id, name, gender, birthdate, age, address, user_auth_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = user_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_user(self, id) :
        sql = """
            SELECT u.id, u.login_id AS "login_id", u.login_pwd AS "login_pwd", u.name AS "name", u.gender AS "gender", u.birthdate AS "birthdate", u.age AS "age", u.address AS "address", ua.name AS "user_auth"
            FROM user u
            JOIN user_auth ua ON u.user_auth_id = ua.id
            WHERE u.login_id = ?;
        """
        args = (id, )
        result = self.execute_sql(DML.SELECTONE, sql, args)

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
    
    def read_visit_store_top_five(self, id) :
        sql = """
            SELECT s.name AS "store name", count(*) AS "visit num"
            FROM user u
            JOIN "order" o ON u.id = o.user_id
            JOIN store s ON o.store_id = s.id
            WHERE u.id = ?
            GROUP BY s.name
            ORDER BY "visit num" DESC
            LIMIT 5
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result
    
    def read_purchase_item_top_five(self, id) :
        sql = """
            SELECT i.name AS "item name", count(*) AS "purchase num"
            FROM user u
            JOIN "order" o ON u.id = o.user_id
            JOIN order_item oi ON o.id = oi.order_id
            JOIN item i ON oi.item_id = i.id
            WHERE u.id = ?
            GROUP BY i.name
            ORDER BY "purchase num" DESC
            LIMIT 5
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result