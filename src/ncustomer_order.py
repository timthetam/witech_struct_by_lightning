from src.side import Side
from src.main import Main

class CustomerOrderException(Exception):
    def __init__(self, order, errors, msg =None):
        if msg is None:
            msg = "Something went wrong"
        super().__init__(msg)
        self.errors = errors
        self._order = order


class CustomerOrder(): 
    #        assert(str(type(burger2)) == "<class 'main.Burger'>")
    # stores the class-wide variable for gernating unique order IDs
    __order_ID = -1

    # generates the next available order ID
    
    def generate_order_id(self):
        CustomerOrder.__order_ID += 1
        return CustomerOrder.__order_ID

    @classmethod
    def set_id(cls, id):
        cls.__order_ID = id
    
    def __init__(self):
        self._main_orders = {}
        #self._main_orders_qty = []

        self._side_orders = {}
        #self._side_orders_qty = []

        # set a unique id for this customer_order object
        self._id = self.generate_order_id()
        print("Generating New ID")
        print(self._id)
        self._status = "Incomplete Order"


    def calc_total_cost(self):
        #please return a floatie
        # iterate through the list of main_orders and side_orders and calculate the total cost
        total = 0.0

        
        for m in self._main_orders:
            # increment total by the cost of the main we are looking at,
            # multiplied by the quantity of that main (stored in dictionary)
            total += (m.calc_cost() * self._main_orders[m])
        
        for s in self._side_orders:
            #print(f"unit_cost:{s.unit_cost}, serving_size: {s.serving_size}")
            # increment total by the cost of the main we are looking at,
            # multiplied by the quantity of that main (stored in dictionary) 
                #print(s.unit_cost)
                #print(self._side_orders[s])
                #print(2.00 * self._side_orders[s])
                total += (s.unit_cost * self._side_orders[s])

        return total
    
    def update_status(self, status):
        self._status = status

    def add_main(self, main, quantity):
        # if there are no items in the dict yet, add them straight away
        if len(self._main_orders) == 0:
            self._main_orders[main] = quantity

        else:
            if main in self._main_orders:
                # increment the dictionary value by quanity amount if already in dict
                self._main_orders[main] += quantity
            else:
                # set the dictionary value by quanity amount if not in dict yet
                self._main_orders[main] = quantity

    def remove_main(self, main, quantity):
        # check the mains dict is not already empty!
        if len(self._main_orders) != 0:
            if main in self._main_orders:
                if (self._main_orders[main] - quantity <= 0):
                    # if the new quantity is 0 or less, delete the entry
                    del self._main_orders[main]
                else:
                    # if the new quantity is more than 0, adjust it accordingly
                    self._main_orders[main] -= quantity

    def add_side(self, side, quantity):
        if len(self._side_orders) == 0:
            self._side_orders[side] = quantity
        else:
            if side in self._side_orders:
                self._side_orders[side] += quantity
            else:
                self._side_orders[side] = quantity
    
    def remove_side(self, side, quantity):
        if len(self._side_orders) != 0:
            if side in self._side_orders:
                if (self._side_orders[side] - quantity <= 0):
                    del self._side_orders[side]
                else:
                    self._side_orders[side] -= quantity


    def validate_order(self):
        errors = {}
        try: 
            if (len(self._main_orders) == 0):
                raise CustomerOrderException(self, errors)
        except CustomerOrderException as ie:
                raise CustomerOrderException(self, errors)

    def __str__(self):
        mains_list = []
        for l in self._main_orders:
            mains_list.append(f"{self._main_orders[l]}x {l} ")
        mains_list = ', '.join([str(x) for x in mains_list])
        
        sides_list = []
        for l in self._side_orders:
            sides_list.append(f"{self._side_orders[l]}x {l}")
        sides_list = ', '.join([str(x) for x in sides_list])
        return f"OrderID: {self._id} - MAINS: {mains_list}, SIDES: {sides_list}, STATUS: {self._status}."


    # helper 'getter' functions
    @property
    def main_orders(self):
        return self._main_orders

    @property
    def side_orders(self):
        return self._side_orders

    @property
    def id(self):
        return self._id
    
    @property
    def status(self):
        return self._status