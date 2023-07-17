from service.execute_sql_service.execute_sql_service import DML
from service.execute_sql_service.SQLBuilder import SQLBuilder

class OrderItemSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
# =========================================================READ=========================================================
    def read_all(self, table_name):
        sql = f"""SELECT id, order_id AS "order id", item_id AS "item id" FROM {table_name} """
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_id(self, table_name, id):
        sql = f"""SELECT id, order_id AS "order id", item_id AS "item id" FROM {table_name} WHERE id = ?"""
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result