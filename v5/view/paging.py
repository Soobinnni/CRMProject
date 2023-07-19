def get_page_info(page_num, interval, total_page):
    cur_page_list = []
    total_page_list = list(range(1, total_page+1))
    separated_page_list = get_crop_page(total_page_list, interval)
    cur_page_list = check_current_page_belongs(page_num, separated_page_list)

    return cur_page_list

def get_crop_page(page_list, interval) :
    result = [page_list[ i : i + interval ] for i in range( 0, len(page_list), interval )]
    return result

def check_current_page_belongs(cur_page, page_list):
    result = None
    for page in page_list : 
        if cur_page in page : 
            result = page

    return result