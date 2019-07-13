
from server import app#, gourmetSystem, gourmetInventory
from flask import render_template, request, redirect, url_for, session,  jsonify, abort
#from src.customer_order import CustomerOrder
#from src.stock_item import StockItem
#from src.main import Burger, Wrap
#import pickle



review = {"eye": 0, "ear": 0, "physical": 0, "content" : "", "location": "", 'locationName' : ""}


@app.route("/", methods=["GET", "POST"])
def home():
    
    return render_template("home.html")


@app.route("/addReview", methods=["GET", "POST"])
def addReview():

    if request.method == "POST":
        # get form data
        if request.form.get('visualRating'):
            review['eye'] = 1
        if request.form.get("auditoryRating"):
            review['ear'] = 1
        if request.form.get("physicalRating"):
            review['physical'] = 1

        review['content'] = request.form.get("reviewText")

        return redirect(url_for('home'))

    return render_template("review.html");


@app.route("/listing", methods=["GET"])
def listing():

    return render_template("listing.html", review=review);

@app.route("/newPlace", methods=["GET", "POST"])
def newPlace():

    if request.method == "POST":
        review['location'] = request.form["location"]
        review['locationName'] = request.form["locationName"]
        return redirect(url_for('home'))

    return render_template("newPlace.html", review=review);


@app.route("/places", methods=["GET"])
def places():

    return render_template("place.html", review=review);

@app.route("/places2", methods=["GET"])
def places2():

    return render_template("place2.html", review=review);

'''
@app.route("/<int:orderID>/customiseBurger", methods=["GET", "POST"])
def customise_burger(orderID):
    fieldValues = {}
    errors = {}
    totalCost = 0.0

    all_ingredients = gourmetInventory.get_ingredients_only()
    valid_ingredients = []
    # now remove the wraps from this list
    for i in all_ingredients:
        #print(i[0])
        if i[0] != "White Wrap" and i[0] != "Wholemeal Wrap":
            valid_ingredients.append(i)
            fieldValues[i[0]] = 0

    if request.method == "POST":
        # create a burger object
        temp_burger = Burger()
        
        for x in valid_ingredients:
            # get the user's inputted quantities for each ingredient on the page
            fieldValues[x[0]] = request.form[x[0]]
            #totalCost += float(x[2]) * float(request.form[x[0]])

            # get the actual stockItem object of the item listed
            item = gourmetInventory.get_item(x[0])
            # add this item (and qty) to the burger if qty > 0
            if int(request.form[x[0]]) > 0:
                temp_burger.add_stock_item(item, request.form[x[0]])

            # also check the value with stock on hand
            if int(fieldValues[x[0]]) > int(gourmetInventory.get_stockItem_qty(item)):
                errors[x[0]] = "Please select a smaller quantity"


            # check if the burger is valid
            msg = temp_burger.validate()
            if msg != None:
                errors['err'] = msg
        # get the cost
        totalCost = temp_burger.calc_cost()

        # If the 'Add To Order' button was pressed, and no errors, pass data to the main page
        if 'AddToOrder' in request.form and len(errors) == 0:
            #print("Adding to order pressed")
            
            orderID = fetch_session_order()
            orderID.add_main(temp_burger,1)
            return redirect(url_for('menu'))
        else:
            return render_template("customise_burger.html", ingredients=valid_ingredients, fieldValues=fieldValues, totalCost=totalCost, errors=errors)

    else:
        return render_template("customise_burger.html", ingredients=valid_ingredients, fieldValues=fieldValues,totalCost=totalCost, errors=errors)



@app.route("/<int:orderID>/customiseWrap", methods=["GET", "POST"])
def customise_wrap(orderID):
    fieldValues = {}
    errors = {}
    totalCost = 0.0

    all_ingredients = gourmetInventory.get_ingredients_only()
    valid_ingredients = []
    # now remove the wraps from this list
    for i in all_ingredients:
        #print(i[0])
        if i[0] != "White Bun" and i[0] != "Wholemeal Bun":
            valid_ingredients.append(i)
            fieldValues[i[0]] = 0

    if request.method == "POST":
        # create a burger object
        temp_wrap = Wrap()
        
        for x in valid_ingredients:
            # get the user's inputted quantities for each ingredient on the page
            fieldValues[x[0]] = request.form[x[0]]

            # get the actual stockItem object of the item listed
            item = gourmetInventory.get_item(x[0])
            # add this item (and qty) to the burger if qty > 0
            if int(request.form[x[0]]) > 0:
                temp_wrap.add_stock_item(item, request.form[x[0]])

            # also check the value with stock on hand
            if int(fieldValues[x[0]]) > int(gourmetInventory.get_stockItem_qty(item)):
                errors[x[0]] = "Please select a smaller quantity"


            # check if the burger is valid
            msg = temp_wrap.validate()
            if msg != None:
                errors['err'] = msg
        # get the cost
        totalCost = temp_wrap.calc_cost()

        # If the 'Add To Order' button was pressed, and no errors, pass data to the main page
        if 'AddToOrder' in request.form and len(errors) == 0:
           # print("Adding to order pressed")
            orderID = fetch_session_order()
            orderID.add_main(temp_wrap,1)
            return redirect(url_for('menu', orderID = orderID))
        else:
            return render_template("customise_wrap.html", ingredients=valid_ingredients, fieldValues=fieldValues, totalCost=totalCost, errors=errors)

    else:
        return render_template("customise_wrap.html", ingredients=valid_ingredients, fieldValues=fieldValues,totalCost=totalCost, errors=errors)


@app.route("/staff/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == 'POST':
        if request.form['inv_submit'] == 'add_item':
            name = request.form.get('name')
            quantity = request.form.get('quantity')
            price = request.form.get('price')
            item = StockItem(name, float(price))
            gourmetInventory.add_new_stockItem(item, int(quantity))
        elif request.form['inv_submit'] != None:
            item = gourmetInventory.get_item(request.form['inv_submit'])
            quantity = request.form.get(request.form['inv_submit'])
            gourmetInventory.modify_stockItem_qty(item, int(quantity))
            
    inventory = gourmetInventory.get_all_items()
    return render_template("inventory.html", inventory=inventory)

@app.route("/staff/orders", methods=["GET"])
def view_curr_orders():
	curr_orders = gourmetSystem.customer_orders
	if len(curr_orders) == 0:
		curr_orders = None
    
	return render_template("curr_orders.html", curr_orders=curr_orders)


@app.route("/staff/orders/UpdateOrder<orderID>", methods=["GET", "POST"])
def update_curr_orders(orderID):
	orderID_int = int(orderID)
	curr_order = gourmetSystem.customer_orders[orderID_int]
	return render_template("update_order_status.html", orderID=orderID_int, curr_order=curr_order)


@app.route("/staff/orders/updated<orderID>to<ChosenStatus>", methods=["Get"])
def update_complete(orderID, ChosenStatus):
    orderID_int = int(orderID)
    curr_order = gourmetSystem.customer_orders[orderID_int]
    if len(ChosenStatus) > 0:
        curr_order.update_status(ChosenStatus)
        if ChosenStatus == 'Completed':
            #gourmetSystem.remove_order(orderID_int)
            gourmetSystem.save_data()
            pass

    return render_template("status_update_confirm.html")

@app.route("/order/<int:orderID>", methods=["GET", "POST"])
def my_order_status(orderID):
	#order = 0
    flag = 0
    order = gourmetSystem.get_order(orderID)
    if order.status != 'Completed':
        flag = 1
    print(gourmetSystem.customer_orders)
    print("ORDERID IS:")
    print(order.id)
    #CustomerOrder(order)
	#if order.status == 'Completed':
    #    flag = 1
    #curr_orders = gourmetSystem.customer_orders
	#for order in curr_orders:
	#	if order.id == int(orderID):
	#		flag = 1
	#		break
    
    

    return render_template("view_my_order.html", order=order, flag=flag)		    


'''