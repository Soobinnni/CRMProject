from object.User import UserGenerator
from object.Store import StoreGenerator
from object.Item import ItemGenerator
from object.Order import OrderGenerator
from object.OrderItem import OrderItemGenerator

import csv

def get_csv_content(filename) :
    datas =[]    
    with open(filename,'r',encoding='utf-8') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            clean_row = {key.strip() : value.strip() for key, value in row.items()}
            datas.append(clean_row) 
    return datas         

def get_id(filename):
    datas = get_csv_content(filename)
    result = []
    for data in datas : 
        result.append(data['Id'])
    return result

def init_user() :
    user = UserGenerator() 
    user.first_name_list = file_to_list("txt/first_name.txt")
    user.last_name_list = file_to_list("txt/last_name.txt")
    user.gu_list = file_to_list("txt/gu.txt")
    user.city_list = file_to_list("txt/cities.txt")

    return user

def init_store() :
    store = StoreGenerator() 
    store.gu_list = file_to_list("txt/gu.txt")
    store.city_list = file_to_list("txt/cities.txt")
    store.store_place_list = file_to_list("txt/place.txt")
    
    return store

def init_item() :
    item = ItemGenerator() 
    return item

def init_order() :
    order = OrderGenerator()
    order.userid_list = get_id("csv/user.csv")
    order.storeid_list = get_id("csv/store.csv")
    return order

def init_orderitem() :
    orderitem = OrderItemGenerator()
    orderitem.orderid_list = get_id("csv/order.csv")
    orderitem.itemid_list = get_id("csv/item.csv")
    return orderitem

def input_type_num() :
    print('데이터를 생성할 종류를 선택하세요.')
    print('[ user, item, store, order, orderitem ]')
    select_data = input('>>>').strip().lower()
    print(f'\n생성할 {select_data}의 개수를 입력하세요')
    num = int(input('>>>').strip())

    return select_data, num

def get_info_list(select_data, num) :
    obj = None
    info = []
    file_name = "csv/"+select_data+".csv"
    if select_data == 'user' :
        obj = init_user()
    elif select_data == 'store' :
        obj = init_store()
    elif select_data == 'item' :
        obj = init_item()
    elif select_data == 'order' :
        obj = init_order()
    elif select_data == 'orderitem' :
        obj = init_orderitem()
    
    info = gen_info(obj, num)

    return file_name, info

def file_to_list(file_name):
    result = None
    with open(file_name, "r", encoding='utf-8') as file: #mode - r(read), w(write), a(append)
        result =  file.read().split(', ')
    return result

def list_to_csv(file_name, data_list) :
    # csv 출력 함수
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for data in data_list:
                writer.writerow(data)

def gen_info(obj, num) :
    result = obj.generate_info(num)
    return result

def main() :
    select_data, num = input_type_num() #사용자 입력
    file_name, gen_info = get_info_list(select_data, num) #랜덤 데이터 생성
    list_to_csv(file_name, gen_info) # 데이터 쓰기

if __name__ == "__main__" :
    main()