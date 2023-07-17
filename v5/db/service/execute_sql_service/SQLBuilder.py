from db.service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class SQLBuilder(ExecuteSQLService):
    def read_all(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        result = self.execute_sql(DML.SELECT, sql) #execute sql
        return result

    def read_kwargs(self, table_name, **kwargs):
        where_sentence, where_args = self.mk_where_condition(kwargs)
        sql = f"SELECT * FROM {table_name} WHERE {where_sentence}"
        result = self.execute_sql(DML.SELECT, sql, where_args) #execute sql
        return result
    
    def read_id(self, table_name, id):
        sql = f"SELECT * FROM {table_name} WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result
    
    def mk_where_condition(self, condition_dict) :
        where_sentence = ""
        where_args = ()
        for key, value in condition_dict.items() : 
            if(value) :
                if "like_" in key :
                    where_sentence += key.replace("like_", "") + " LIKE ? AND "
                    where_args += (f"%{value}%",)
                else :
                    where_sentence += key + ' = ? AND '
                    where_args += (value, )
        where_sentence = where_sentence[0:-5] #TODO: 좋은 방법 같지 않음.. AND를 자르기 위함

        return where_sentence, where_args