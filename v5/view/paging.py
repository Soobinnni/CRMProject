import math

def get_page_info(page_num, per_page, interval, datas): #현재 페이지 번호, 노출할 게시물 개수, 노출할 페이지 번호 간격, 게시데이터 
    cur_page_list = []
    page_datas = None
   
    total_page = get_total_page(per_page, len(datas)) # 전체 페이지 번호 개수 구하기
    total_page_list = list(range(1, total_page+1)) #  # 전체 페이지 번호를 리스트화 하기(1~전체 int페이지를 담은 리스트)
    
    separated_page_list = get_crop_page(total_page_list, interval) # 페이지에 노출할 페이지 범위만큼 자른 리스트를 요소로 하는 리스트 얻기
   
    cur_page_list = check_current_page_belongs(page_num, separated_page_list) #현재 페이지가 어느 요소에 속하는 지 검사
    page_datas = get_current_page_datas(page_num, per_page, datas)  #현재 페이지의 데이터 get
 
    return (total_page, cur_page_list, page_datas)

def get_total_page(per_page, len_datas):
    total_page = 0
    total_page=math.ceil(len_datas/per_page)
    return total_page

def get_crop_page(page_list, interval) :
    result = [page_list[ i : i + interval ] for i in range( 0, len(page_list), interval )]
    return result

def check_current_page_belongs(cur_page, page_list):
    result = None
    for page in page_list : 
        if cur_page in page : 
            result = page

    return result

def get_current_page_datas(page_num, per_page, datas) :
    start_index=(page_num-1)*per_page
    end_index=page_num * per_page # 슬라이싱은 마지막 범위가 미만이니까 
    return datas[start_index:end_index] 

# def get_page_info(page_num, datas):
#     #log
#     print('----------------------------paging : get_page_info')

#     per_page=10 # 페이지 당 게시할 게시물 수
#     total_page=-1 # 페이지 개수
#     start_index=-1
#     end_index=-1

#     if datas != 0 :
#         # ceil 함수는 실수를 입력하면 올림 하여 정수를 반환하는 함수이다.
#         total_page=math.ceil(len(datas)/per_page)
        
#         # 0~9 / 10~19 / 20~29
#         start_index=(page_num-1)*per_page
#         # 슬라이싱은 마지막 범위가 미만이니까 
#         end_index=page_num*per_page
#         print(f"page_num{page_num} : {start_index},{end_index}")

#         page_datas=datas[start_index:end_index] 

#     return (total_page, page_datas)
