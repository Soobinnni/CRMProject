from object.Generator import Generator

import random
import csv

class OrderItemGenerator(Generator) :
    def __init__(self) :
        self.orderid_list = []
        self.itemid_list = []
        self.id = ""
        self.orderid = ""
        self.itemid = ""
        
    def generate_info(self, num) :
        info = []
        for _ in range(0, num) :
            info_list = [self.mk_uuid(), self.mk_orderid(), self.mk_itemid()]           
            info.append(info_list)
        return info
    
    def mk_orderid(self) :
        id = random.choice(self.orderid_list)
        return id
    
    def mk_itemid(self) :
        id = random.choice(self.itemid_list)
        return id
      