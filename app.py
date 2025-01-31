from flask import Flask, request
app =Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/data', methods=['GET'])
def get_data():
    data = request.json
    return {"data":data, "message": "Send a POST request with JSON dat" }

@app.route('/data', methods=['POST'])
def handle_data():

    data = request.json
    return {"message": "Data received", "data": data}

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return {"message": f"Item {item_id} updated"}

@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return {"message": f"Item {item_id} deleted"}

if __name__ == '__main__':
    app.run(debug=True)