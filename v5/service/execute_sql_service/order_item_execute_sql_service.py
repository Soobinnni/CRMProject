from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class OrderItemExecuteSQLService(ExecuteSQLService):
    def read_all(self):
        #log
        print('----------------------------service-order_item : read_all()')
        
        #execute sql
        sql = """SELECT * FROM order_item """
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-order_item : read_id()')
        
        #execute sql
        sql = """SELECT * FROM order_item WHERE id = ?"""
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args)
        return result
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())