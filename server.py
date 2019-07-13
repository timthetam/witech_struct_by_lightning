
from flask import Flask
'''
from init import bootstrap_system, bootstrap_inventory
from src.ordering_system import OrderingSystem
from src.inventory import Inventory
from src.customer_order import CustomerOrder
'''
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"

#Loading in Data
'''
print("Loading in data...")
gourmetSystem = OrderingSystem.load_data()
gourmetInventory = Inventory.load_data()

if gourmetSystem == None:
    print("No System")
    gourmetSystem = bootstrap_system.initialise()
else:
    ID = 0
    for order in gourmetSystem.customer_orders:
        print(order)
        if order>ID and gourmetSystem.customer_orders[order].status != "Incomplete Order":
            ID = order + 1
    CustomerOrder.set_id(ID)
if len(gourmetInventory.stock_list) == 0:
    gourmetInventory = bootstrap_inventory.load_data()

print("Loading Complete!")
'''