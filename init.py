# this file is used to fill the system in with stock items initially
'''from src.stock_item import StockItem
from src.inventory import Inventory
from src.ordering_system import OrderingSystem
from src.side import Side
from src.customer_order import CustomerOrder
'''
class bootstrap_system:
    @classmethod
    def initialise(cls):
        system = OrderingSystem()
        return system


#class bootstrap_inventory:b
    '''
    @classmethod
    def load_data(cls):
        inventory = Inventory()

        WholemealBun = StockItem("Wholemeal Bun", 0.6)
        inventory.add_new_stockItem(WholemealBun, 10)
        WhiteBun = StockItem("White Bun", 0.4)
        inventory.add_new_stockItem(WhiteBun, 10)
        WholemealWrap = StockItem("Wholemeal Wrap", 0.6)
        inventory.add_new_stockItem(WholemealWrap, 10)
        WhiteWrap = StockItem("White Wrap", 0.4)
        inventory.add_new_stockItem(WhiteWrap, 10)

        return inventory
