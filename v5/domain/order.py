import uuid
from datetime import datetime
class Order() :
    def __init__(self) :
        self.id = ""
        self.store_id = ""
        self.user_id = ""
        self.ordered_at = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def store_id(self):
        return self.__store_id

    @store_id.setter
    def store_id(self, store_id):
        self.__store_id = store_id
        
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    def mk_uuid(self) :
        return str(uuid.uuid4())
    
    def mk_ordered_at(self) :
        now = datetime.now()
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time