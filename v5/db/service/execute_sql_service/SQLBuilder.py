from db.service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

class SQLBuilder(ExecuteSQLService):
    def read_all(self, table_name, limit_num, offset_num):
        select = "select "
        from_sentence = f" FROM {table_name}"
        lo_sentence = f" LIMIT {limit_num} OFFSET {offset_num}"

        sql = select + "*" + from_sentence + lo_sentence
        count_sql = select + 'count(*) AS "count"' + from_sentence

        result = self.execute_sql(DML.SELECT, sql) # list[dic, ..]
        count_result = int(self.execute_sql(DML.SELECTONE, count_sql)['count']) # integer

        return result, count_result

    def read_kwargs(self, table_name, limit_num, offset_num, **kwargs):
        select = "select "
        from_sentence = f" FROM {table_name}"
        lo_sentence = f" LIMIT {limit_num} OFFSET {offset_num}"
        where_sentence, where_args = self.mk_where_condition(kwargs)

        sql = select + "*" + from_sentence + where_sentence + lo_sentence
        count_sql = select + 'count(*) AS "count"' + from_sentence + where_sentence

        result = self.execute_sql(DML.SELECT, sql, where_args) # list[dic, ..]
        count_result = int(self.execute_sql(DML.SELECTONE, count_sql, where_args)['count']) # integer
        
        return result, count_result

    def read_id(self, table_name, id):
        sql = f"SELECT * FROM {table_name} WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args) #execute sql
        return result
    
    def mk_where_condition(self, condition_dict) :
        where_sentence = " WHERE"
        where_args = ()

        for key, value in condition_dict.items() : 
            if(value) :
                if "like_" in key :
                    where_sentence += " " + key.replace("like_", "") + " LIKE ? AND "
                    where_args += (f"%{value}%",)
                else : 
                    where_sentence += " " + key + ' = ? AND '
                    where_args += (value, )
        where_sentence = where_sentence[0:-5] #TODO: index접근으로 바꿨었으나 인자가 없을 경우 오류..

        return where_sentence, where_args