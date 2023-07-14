from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class StoreExecuteSQLService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, store) :
        store = store #domain
        
        id = store.id = mk_uuid() # uuid init
        store_tuple = self.properties_to_tuple(store) # object property -> tuple

        sql = "INSERT INTO store(id, name, type, address) VALUES (?, ?, ?, ?)"
        args = store_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        sql = "SELECT * FROM store"
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result
    
    def read_kwargs(self, **kwargs):
        sql = """SELECT * FROM store WHERE """
        where_sentence, where_args = self.mk_where_condition(kwargs)
        sql += where_sentence
        result = self.execute_sql(DML.SELECT, sql, where_args) #execute sql
        return result
    
    def read_id(self, id):
        sql = "SELECT * FROM store WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql

        return result
    
# =========================================================etc=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())