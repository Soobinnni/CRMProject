from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class OrderItemSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
# =========================================================READ=========================================================
    def read_all(self, table_name, limit_num, offset_num):
        select = "select "
        from_sentence = f" FROM {table_name}"
        lo_sentence = f" LIMIT {limit_num} OFFSET {offset_num}"

        sql = select + '''id, order_id AS "order id", item_id AS "item id"''' + from_sentence + lo_sentence
        count_sql = select + 'count(*) AS "count"' + from_sentence

        result = self.execute_sql(DML.SELECT, sql) # list[dic, ..]
        count_result = int(self.execute_sql(DML.SELECTONE, count_sql)['count']) # integer
        
        return result, count_result
    
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