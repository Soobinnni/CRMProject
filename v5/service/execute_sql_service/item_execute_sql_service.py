from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class ItemExecuteSQLService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, item) :
        #log
        print('----------------------------service-item : create()')

        #domain
        item = item

        # uuid init, object property -> tuple
        id = item.id = mk_uuid()
        item_tuple = self.properties_to_tuple(item)
        
        #execute sql
        sql = "INSERT INTO item(id, name, type, unit_price) VALUES (?, ?, ?, ?)"
        args = item_tuple
        self.execute_sql(DML.INSERT, sql, args)

        #return
        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-item : read_all()')
        
        #execute sql
        sql = "SELECT * FROM item"
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_name(self, name):
        #log
        print('----------------------------service-item : read_name()')
        
        #execute sql
        sql = f"SELECT * FROM item WHERE name LIKE '%{name}%'"
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_price(self, price):
        #log
        print('----------------------------service-item : read_price()')
        
        #execute sql
        sql = "SELECT * FROM item WHERE unit_price = ?"
        args = (price,)
        result = self.execute_sql(DML.SELECT, sql, args)
        return result
    
    def read_name_price(self, name, price):
        #log
        print('----------------------------service-item : read_name_price()')
        
        #execute sql
        sql = f"SELECT * FROM item WHERE name LIKE '%{name}%' AND unit_price = ?"
        args = (price,)
        result = self.execute_sql(DML.SELECT, sql, args)
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        
        #execute sql
        sql = "SELECT * FROM item WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args)
        return result
    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())