import service.execute_sql_service
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class OrderExecuteSQLService(ExecuteSQLService):
# =========================================================READ=========================================================
    def read_all(self):
        sql = """SELECT * FROM "order" """
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_kwargs(self, **kwargs):
        sql = """SELECT * FROM "order" WHERE """
        where_sentence, where_args = self.mk_where_condition(kwargs)
        sql += where_sentence
        result = self.execute_sql(DML.SELECT, sql, where_args) #execute sql
        return result

    def read_id(self, id):
        sql = """
            SELECT oi.id AS "id", oi.order_id AS "order id", oi.item_id AS "item id", i.name AS "item name"
            FROM "order" o
            JOIN "order_item" oi ON o.id = oi.order_id
            JOIN item i ON oi.item_id = i.id
            WHERE o.id = ?
            ORDER BY o.ordered_at DESC
        """
        args = (id,)
        result = self.execute_sql(DML.SELECT, sql, args) #execute sql
        return result
# =========================================================etc=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())