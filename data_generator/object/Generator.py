import uuid
import random

class Generator :
    def __init__(self) :
        self.gu_list = []
        self.city_list = []

    def generate_info(self) :
        pass

    def mk_uuid(self) :
        id = str(uuid.uuid4())
        return id
    
    def mk_address(self) :
        city_name = random.choice(self.city_list)
        gu_name = random.choice(self.gu_list)
        gil_num = str(random.randint(1,50))+'길'
        address_num = random.randint(1,50)
        adresss = city_name+' '+gu_name+' '+gil_num+ ' '+ str(address_num)
        
        return adresss