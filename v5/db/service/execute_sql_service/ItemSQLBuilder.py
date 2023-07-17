import uuid
from db.service.execute_sql_service.execute_sql_service import DML
from db.service.execute_sql_service.SQLBuilder import SQLBuilder

class ItemSQLBuilder(SQLBuilder):
# =========================================================CREATE=========================================================
    def create(self, item) :
        item = item #domain
        id = item.id = str(uuid.uuid4()) # uuid init
        item_tuple = tuple(item.__dict__.values()) # object property -> tuple
        
        sql = "INSERT INTO item(id, name, type, unit_price) VALUES (?, ?, ?, ?)"
        args = item_tuple
        self.execute_sql(DML.INSERT, sql, args) #execute sql

        return id
    
# =========================================================READ=========================================================
