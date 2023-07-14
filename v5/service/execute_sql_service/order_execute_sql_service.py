import service.execute_sql_service
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class OrderExecuteSQLService(ExecuteSQLService):
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-order : read_all()')
        
        #execute sql
        sql = """SELECT * FROM "order" """
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_order_date(self, order_date) :
        #log
        print('----------------------------service-order : read_order_date()')
       
        #execute sql
        sql = f"""SELECT * FROM "order" WHERE ordered_at LIKE '{order_date}%'"""
        result = self.execute_sql(DML.SELECT, sql)
        return result

    def read_id(self, id):
        #log
        print('----------------------------service-order : read_id()')
        
        #execute sql
        sql = """
            SELECT oi.id AS "id", oi.order_id AS "order id", oi.item_id AS "item id", i.name AS "item name"
            FROM "order" o
            JOIN "order_item" oi ON o.id = oi.order_id
            JOIN item i ON oi.item_id = i.id
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