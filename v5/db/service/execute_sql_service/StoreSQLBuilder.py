import uuid
from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class StoreSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
    def create(self, store) :
        store = store #domain
        
        id = store.id = str(uuid.uuid4()) # uuid init
        store_tuple = tuple(store.__dict__.values()) # object property -> tuple

        sql = "INSERT INTO store(id, name, type, address) VALUES (?, ?, ?, ?)"
        args = store_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================