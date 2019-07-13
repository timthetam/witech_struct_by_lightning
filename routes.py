
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

        return redirect(url_for('listing'))

    return render_template("review.html", review=review);


@app.route("/listing", methods=["GET"])
def listing():

    return render_template("listing.html", review=review);

@app.route("/newPlace", methods=["GET", "POST"])
def newPlace():

    if request.method == "POST":
        review['location'] = request.form["location"]
        review['locationName'] = request.form["locationName"]
        return redirect(url_for('listing'))

    return render_template("newPlace.html", review=review);


@app.route("/places", methods=["GET"])
def places():

    return render_template("place.html", review=review);

@app.route("/places2", methods=["GET"])
def places2():

    return render_template("place2.html", review=review);

