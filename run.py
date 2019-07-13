from routes import app
#from server import gourmetSystem, gourmetInventory
import pickle

if __name__ == '__main__':
    app.run(debug=True, port=8085)