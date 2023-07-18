from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class OrderItemSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
# =========================================================READ=========================================================
    def read_all(self, table_name):
        sql = f"""SELECT id, order_id AS "order id", item_id AS "item id" FROM {table_name} """
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_id(self, table_name, id):
        sql = f"""
            SELECT oi.id AS "id", oi.order_id AS "order id", oi.item_id AS "item id", i.name AS "item name"
            FROM {table_name} o
            JOIN "order_item" oi ON o.id = oi.order_id
            JOIN item i ON oi.item_id = i.id
            WHERE o.id = ?
            ORDER BY o.ordered_at DESC
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result