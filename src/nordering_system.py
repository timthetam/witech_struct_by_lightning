from abc import ABC, abstractmethod
import pickle

from src.customer_order import CustomerOrder
from src.inventory import Inventory
from src.stock_item import StockItem
from src.side import Side
from src.main import Main
 
class OSDAO(ABC):

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(cls):
        pass

class OrderingSystem(OSDAO):
    def __init__(self):
        self._customer_orders = {}
        

    def __str__(self):
        numOrders = len(self._customer_orders)
        msg = f"Currently {numOrders} orders not completed"
        return msg
    
    def create_order(self):
        order = CustomerOrder()
        self._customer_orders[order.id] = order
        return order.id

    def add_order(self, order, InvSys):
        order.update_status("Order Submitted")
        self._customer_orders[order.id] = order
            
        for main in order.main_orders:
            for sItem in main.stock_chosen:
                amount = main.stock_chosen[sItem] * order.main_orders[main]
                amount = int(amount)
                InvSys.modify_stockItem_qty(sItem, -amount)
        for side in order.side_orders:
            amount = order.side_orders[side] * side.serving_size
            int(amount)
            InvSys.modify_stockItem_qty(side.sideItem, -amount)
            
    def remove_order(self, orderNum):
        if order and order in self.customer_orders:
            self._customer_orders.remove(order)
            return True
        elif orderNum:
            for count, order in enumerate(self.customer_orders):
                if order.id == orderNum:
                    del self.customer_orders[count]
                    return True
        return False
    
    def get_order(self, id):
        #print("THE ID COMING IN IS:")
        #print(id)
        return self._customer_orders[id]
    
    def save_data(self):
        #print("Saved Ordering System")
        with open('system.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('system.dat', 'rb') as file:
                system = pickle.load(file)
        except IOError:
            system = OrderingSystem()
            print("New Ordering System")
        return system

    '''
    Properties
    '''
    @property
    def customer_orders(self):
        return self._customer_orders


