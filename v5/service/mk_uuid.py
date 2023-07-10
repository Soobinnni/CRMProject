import uuid


# 고유식별키 - db에 컬럼데이터 생성 시 만드니까 db폴더에 넣는 것이라고 판단.
def mk_uuid() :
    id = str(uuid.uuid4())
    return id