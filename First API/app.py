from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import abort


app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'hello world'

@app.route('/')
def home():
    return render_template('index.html')

stores = [
    {
        'name': 'Walmart',
        'items': [
            {
                'name': 'shampoo',
                'price': 15.99,
            }
        ],
    }

]

# POST - used to receive data from user
# GET - used to send data back to user

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        # 'items': request_data['items']
        'items': []
    }
    stores.append(new_store)
    return jsonify({"stores":stores})

# GET /store/<string:name>
@app.route('/store/<string:name>')  # http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"store": store})
    
    return abort(404)

#GET /store
@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/items', methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({"stores": stores})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/items')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return abort(404)

app.run(port=5000)
