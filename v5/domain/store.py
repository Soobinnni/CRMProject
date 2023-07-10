class Store() :
    def __init__(self, name, type_, address) :
        self.id = ""
        self.name = name
        self.type_ = type_
        self.address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        self.__type_ = type_
        
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address