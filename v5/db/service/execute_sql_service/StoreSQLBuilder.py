import uuid
from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class StoreSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
    def create(self, store) :
        store = store #domain
        
        id = store.id = str(uuid.uuid4()) # uuid init
        store_tuple = tuple(store.__dict__.values()) # object property -> tuple

        sql = "INSERT INTO store(id, name, type, address) VALUES (?, ?, ?, ?)"
        args = store_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_sales(self, id, type_) :
        substr_num = None
        date_column_name  = None
        order_by = None

        if (type_ == "monthly") :
            substr_num = 7
            date_column_name  = "month"
            order_by = "count(*)"
        else :
            substr_num = 10
            date_column_name  = "date"
            order_by = '''"month"'''
        
        sql = f"""
            SELECT SUBSTR(o.ordered_at, 1, {substr_num}) AS "{date_column_name}", SUM(i.unit_price) AS "revenue", COUNT(*) AS "count"
            FROM store s
            JOIN "order" o ON s.id = o.store_id
            JOIN order_item oi ON o.id = oi.order_id
            JOIN item i ON oi.item_id = i.id
            WHERE s.id = ?
            GROUP BY "{date_column_name}"
            ORDER BY {order_by} DESC
        """
        args = (id,)
        print(sql)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql

        return result
    
    def read_regular_customer(self, id) : 
        sql = """
            SELECT u.id AS "user id", u.name AS "name", COUNT(*) AS "frequency"
            FROM store s
            JOIN "order" o ON s.id = o.store_id
            JOIN user u ON o.user_id = u.id
            WHERE s.id = ?
            GROUP BY u.name
            ORDER BY COUNT(*) DESC
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql

        return result
    
    def read_type(self) :
        sql = """
            SELECT DISTINCT type
            FROM store
            ORDER BY type
        """
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result