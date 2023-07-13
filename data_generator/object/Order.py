from object.Generator import Generator

from datetime import datetime, timedelta
import csv
import random

class OrderGenerator(Generator) :
    def __init__(self):
        self.userid_list = []
        self.storeid_list = []
        self.id = ""
        self.orderedat = ""
        self.userid = ""
        self.storeid = ""

    def generate_info(self, num) :
        info = []
        for _ in range(0, num) :
            info_list = [self.mk_uuid(), self.mk_orderedat(), self.mk_userid(), self.mk_storeid()]           
            info.append(info_list)
        return info

    def mk_orderedat(self) :    
        start = datetime(2023, 1, 1)  # 범위의 시작 날짜
        end = datetime(2023, 12, 31)  # 범위의 끝 날짜

        # 범위 내에서 랜덤한 날짜 생성
        time_difference = end - start
        random_seconds = random.randint(0, time_difference.total_seconds())
        order_at = start + timedelta(seconds=random_seconds)

        return order_at
    
    def mk_userid(self) :
        id = random.choice(self.userid_list)
        return id

    def mk_storeid(self) :
        id = random.choice(self.storeid_list)
        return id