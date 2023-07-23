import uuid
from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class ItemSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
    def create(self, item) :
        item = item #domain
        id = item.id = str(uuid.uuid4()) # uuid init
        item_tuple = tuple(item.__dict__.values()) # object property -> tuple
        
        sql = "INSERT INTO item(id, name, type, unit_price) VALUES (?, ?, ?, ?)"
        args = item_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_monthly_sales(self, id) :
        sql = """
            SELECT SUBSTR(o.ordered_at, 1, 7) AS "Month", SUM(i.unit_price) AS "Total Revenue", COUNT(*) AS "Item Count"
            FROM item i
            JOIN order_item oi ON i.id = oi.item_id 
            JOIN "order" o ON oi.order_id = o.id
            WHERE i.id = ?
            GROUP BY "Month"
            ORDER BY "Month"
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result
    
    def read_type(self) :
        sql = '''
            SELECT DISTINCT type
            FROM item
            ORDER BY type
        '''
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result