from abc import ABC, abstractmethod
from src.stock_item import StockItem
from src.inventory import Inventory


class Main(ABC):


    def __init__(self):
        self._stock_chosen = {}
        self._max_patties = 2 # This can obviously be changed. I don't know what the max patties are off the top of my little head

    def calc_cost(self):
        total = 0.0

        for item in self._stock_chosen:
            total += float(item.unit_cost) * float(self._stock_chosen[item])
            # increments sum by the cost of the stock_item * its quanity

        return total

    def add_stock_item(self, StockItem, quantity):

        # if there are no items then add first
        if len(self._stock_chosen) == 0:
            self._stock_chosen[StockItem] = quantity
        else:
            # increment by the amount of quantity if stock exists in dict
            if StockItem in self._stock_chosen:
                self._stock_chosen[StockItem] += quantity
            # else set the dictionary value by quanity amount if not in dict yet
            else:
                self._stock_chosen[StockItem] = quantity

    def remove_stock_item(self, StockItem, quantity):

        # check our stock dictionary isnt empty
        if len(self._stock_chosen) != 0:
            if StockItem in self._stock_chosen:
                # check if resulted quantity is negative or empty, then remove item
                if (self._stock_chosen[StockItem] - quantity <= 0):
                    del self._stock_chosen[StockItem]
                # else decrement by quantity amount
                else:
                    self._stock_chosen[StockItem] -= quantity

    # abstract methods
    @abstractmethod
    def validate(self):
        pass

    @property
    def stock_chosen(self):
        return self._stock_chosen

    @property
    def max_patties(self):
        return self._max_patties

class TooManyBuns(Exception):
    def __init__(self, msg=None):
        if msg is None:
            self._msg = "Too Many Buns!"

class TooManyWraps(Exception):
    def __init__(self, msg=None):
        if msg is None:
            self._msg = "Too Many Wraps!"

class TooManyPatties(Exception):
    def __init__(self, msg=None):
        if msg is None:
            self._msg = "Too Many Patties!"


class Burger(Main):
    def __init__(self):
        super().__init__()

    def validate(self):
        # Will check the number of buns and patties
        buns = 0
        patties = 0
        for item in self._stock_chosen:
            if 'bun' in str(item.name).lower():
                buns += int(self._stock_chosen[item])
            if 'patty' in str(item.name).lower():
                patties += int(self._stock_chosen[item])
        try:
            if patties > super().max_patties:
                raise TooManyPatties
            elif buns > 4:
                raise TooManyBuns
        except TooManyPatties as error:
            return error._msg
        except TooManyBuns as error:
            return error._msg
          
    def __str__(self):
        ingredients_list = []
        for l in self._stock_chosen:
            ingredients_list.append(f"{self._stock_chosen[l]}x {l}")
        ingredients_list = ', '.join([str(x) for x in ingredients_list])
        return f"Burger with {ingredients_list}"


class Wrap(Main):
    def __init__(self):
        super().__init__()

    def validate(self):
        # Will check the number of Wraps and patties
        wraps = 0
        patties = 0
        for item in self._stock_chosen:
            if 'wrap' in str(item.name).lower():
                wraps += int(self._stock_chosen[item])
            if 'patty' in str(item.name).lower():
                patties += int(self._stock_chosen[item])
        try:
            if patties > super().max_patties:
                raise TooManyPatties
            elif wraps > 1:
                raise TooManyWraps
        except TooManyPatties as error:
            return error._msg
        except TooManyWraps as error:
            return error._msg
            
        return None

    def __str__(self):
        ingredients_list = []
        for l in self._stock_chosen:
            ingredients_list.append(f"{self._stock_chosen[l]}x {l}")
        ingredients_list = ', '.join([str(x) for x in ingredients_list])
        return f"Wrap with {ingredients_list}"


