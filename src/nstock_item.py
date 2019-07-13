class StockItem():
    __id = -1
    
    def __init__(self, name, unit_cost):
        self._item_code = self.generate_id()
        self._name    = name
        self._unit_cost = unit_cost
    '''
    properties
    '''
    @property
    def name(self):
        return self._name

    @property
    def unit_cost(self):
        return self._unit_cost

    def __str__(self):
        return f"{self._name}"

    def generate_id(self):
        StockItem.__id += 1
        return StockItem.__id

    @classmethod
    def set_id(cls, id):
        cls.__id = id
