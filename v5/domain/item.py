class Item() :
    def __init__(self, name, type_, unit_price) :
        self.id = ""
        self.name = name
        self.type_ = type_
        self.unit_price = unit_price

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
    def unit_price(self):
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self.__unit_price = unit_price