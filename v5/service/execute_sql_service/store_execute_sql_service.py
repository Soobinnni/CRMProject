from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class StoreExecuteSQLService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, store) :
        #log
        print('----------------------------service-store : create()')

        #domain
        store = store

        #property
        id = store.id = mk_uuid()
        store_tuple = self.properties_to_tuple(store)

        #execute sql
        sql = "INSERT INTO store(id, name, type, address) VALUES (?, ?, ?, ?)"
        args = store_tuple
        self.execute_sql(DML.INSERT, sql, args)

        #return
        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-store : read_all()')

        #execute sql
        sql = "SELECT * FROM store"
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_address(self, address):
        #log
        print('----------------------------service-store : read_address()')
        
        #execute sql
        sql = f"SELECT * FROM store WHERE address LIKE '%{address}%'"
        result = self.execute_sql(DML.SELECT, sql)

        return result
    
    def read_name(self, name):
        #log
        print('----------------------------service-store : read_name()')
        
        #execute sql
        sql = f"SELECT * FROM store WHERE name LIKE '%{name}%'"
        result = self.execute_sql(DML.SELECT, sql)

        return result
    
    def read_name_address(self, name, address):
        #log
        print('----------------------------service-store : read_name_address()')
        
        #execute sql
        sql = f"SELECT * FROM store WHERE name LIKE '%{name}%' AND address LIKE '%{address}%'"
        result = self.execute_sql(DML.SELECT, sql)

        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-store : read_id()')

        #execute sql
        sql = "SELECT * FROM store WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args)

        return result
    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())