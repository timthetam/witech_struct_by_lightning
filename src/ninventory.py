from src.stock_item import StockItem
from src.side import Side
from abc import ABC, abstractmethod
import pickle


class InventoryError(Exception):
        def __init__(self,errors, msg =None):
            if msg is None:
                msg = "Something went wrong"
            super().__init__(msg)
            self.errors = errors
    
        def check_inventory_errors(quantity):
            errors = {}
            if quantity < 0:
                errors['quantity'] = "Please supply a postive value"
            if errors:
                raise InventoryError(errors)
        
        def check_modify(quantity, addition):
            errors = {}
            if quantity + addition < 0:
                errors['modification'] = "Error modifying value in inventory"
            if errors:
                raise InventoryError(errors)


class InvDAO(ABC):

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(cls):
        pass

class Inventory(InvDAO):
    def __init__(self):
        self._stock_list = {}
        self._side_list = []

    def add_side(self, side):
        self._side_list.append(side)

    def add_new_stockItem(self, sItem, quantity):
#        try: 
#            InventoryError.check_inventory_errors(quantity)
#        except InventoryError as ie:
#            return None, ie.errors

        self._stock_list[sItem] = quantity
        return
    
    def modify_stockItem_qty(self, sItem, new_quantity):
        print(sItem.name)
#        try:
#            InventoryError.check_modify(self._stock_list[sItem], new_quantity)
#        except InventoryError as ie:
#            return f"Error cannot reduce by <{new_quantity}> as the there are only <{self._stock_list[sItem]}> of <{sItem.name}>", ie.errors
        if self._stock_list[sItem] >= 0:
            if self._stock_list[sItem] + new_quantity >= 0:
                self._stock_list[sItem] += new_quantity
                return
 
    def get_stockItem_qty(self, sItem):
        if type(sItem) is Side:
            return self.stock_list[sItem.sideItem]
        elif type(sItem) is StockItem:
            return self.stock_list[sItem]
        else:
            return None


    def get_item(self, name):
        items = self._stock_list.keys()
        for item in items:
            if item.name == name:
                print(name)
                return item
        items = self.side_list
        for item in items:
            if item.name == name:
                return item
        return None
    
    def get_all_items(self):
        items = self.stock_list.keys()
        lst = []
        for item in items:
            lst.append([item.name,self.stock_list[item], item.unit_cost])
        return lst

    def get_ingredients_only(self):
        items = self.stock_list.keys()
        lst = []
        for item in items:
            add=1
            for side in self.side_list:
                if side.sideItem == item:
                    add = 0
                    break
            # we only want to include the stock items as they are ingredients that
            # can be added to burgers/wraps
            # so we ignore Sides
            if add:
                lst.append([item.name, self.stock_list[item], item.unit_cost])
        return lst

    def get_Sides_only(self):
        items = self._side_list
        lst = []
        for item in items:
            # we only want to include Sides here
            lst.append([item.name, self.stock_list[item.sideItem], item.unit_cost, item.serving_size])
        return lst
    
    def max_id(self):
        return max([x.item_code for x in self._items])

    def save_data(self):
        with open('inventory.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('inventory.dat', 'rb') as file:
                inventory = pickle.load(file)
        except IOError:
            inventory = Inventory()
            print("New Inventory")
        return inventory
    '''
    Properties
    '''
    
    @property
    def stock_list(self):
        return self._stock_list

    @property
    def side_list(self):
        return self._side_list
    
    
'''Testing'''
'''
InvSys = Inventory()
tomato = StockItem("tomato", 0.2)
bun = StockItem("bun", 0.25)
wrap = StockItem("wrap", 0.25)
lettuce = StockItem("lettuce", 0.3)
#print(InvSys.add_new_stockItem(tomato, 10))

InvSys.add_new_stockItem(tomato, 10)
InvSys.add_new_stockItem(bun,50)
InvSys.add_new_stockItem(wrap,50)
InvSys.add_new_stockItem(lettuce,50)


#print(InvSys.add_new_stockItem(tomato, -10))
#print(InvSys.get_stockItem_qty(tomato))
print(InvSys.modify_stockItem_qty(tomato,-50))
print(InvSys.get_stockItem_qty(tomato))
#assert InvSys.get_stockItem_qty(tomato) == 10
print(InvSys.get_all_items())
'''
