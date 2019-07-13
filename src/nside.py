from src.stock_item import StockItem

class Side(StockItem):
    def __init__(self, name, sItem, serving_size, price=0):
        self._sideItem = sItem
        self._serving_size = serving_size        
        self._name = name
        self._price = price

    @property
    def serving_size(self):
        return self._serving_size

    @property
    def sideItem(self):
        return self._sideItem

    @property
    def name(self):
        return self._sideItem.name + " " + self._name

    @property
    def unit_cost(self):
        if self._price == 0:
            return self._sideItem.unit_cost
        else:
            return self._price
    
    def __str__(self):
        return f"{self._sideItem.name + self._name}"
