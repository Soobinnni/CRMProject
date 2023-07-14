from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class OrderItemExecuteSQLService(ExecuteSQLService):
    def read_all(self):
        sql = """SELECT id, order_id AS "order id", item_id AS "item id" FROM order_item """
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_id(self, id):
        sql = """SELECT id, order_id AS "order id", item_id AS "item id" FROM order_item WHERE id = ?"""
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())