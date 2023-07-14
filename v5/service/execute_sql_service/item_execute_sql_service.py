from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class ItemExecuteSQLService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, item) :
        item = item #domain
        id = item.id = mk_uuid() # uuid init
        item_tuple = self.properties_to_tuple(item) # object property -> tuple
        
        sql = "INSERT INTO item(id, name, type, unit_price) VALUES (?, ?, ?, ?)"
        args = item_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        # execute sql
        sql = "SELECT * FROM item"
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result

    def read_kwargs(self, **kwargs):
        where_sentence, where_args = self.mk_where_condition(kwargs)
        sql = f"SELECT * FROM item WHERE {where_sentence}"
        result = self.execute_sql(DML.SELECT, sql, where_args) #execute sql
        return result
    
    def read_id(self, id):
        sql = "SELECT * FROM item WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result
    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())