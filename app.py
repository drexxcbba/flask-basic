from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({ "message": "Yes!!!" })

@app.route('/products')
def getall():
    return jsonify({
        "count": len(products),
        "products": products
    })

@app.route('/products/<string:name>')
def getbyname(name):
    result = [it for it in products if it['name'] == name]
    if len(result) > 0:
        return jsonify({
            "message": "success",
            "product": result
        })
    else:
        return jsonify({
            "message": "product not found"
        })

@app.route('/products', methods=['POST'])
def createproduct():
    newproduct = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(newproduct)
    return jsonify({
        "message": "successfully created",
        "product": newproduct
    })

@app.route('/products/<string:name>', methods=['PUT'])
def updateproduct(name):
    result = [it for it in products if it['name'] == name]
    if len(result) > 0:
        result[0]["price"] = request.json['price']
        result[0]["quantity"] = request.json['quantity']
        return jsonify({
            "message": "successfully updated",
            "product": result
        })
    else:
        return jsonify({
            "message": "product not found"
        })

@app.route('/products/<string:name>', methods=['DELETE'])
def deleteproduct(name):
    result = [it for it in products if it['name'] == name]
    if len(result) > 0:
        products.remove(result[0])
        return jsonify({
            "message": "successfully deleted",
            "products": products
        })
    else:
        return jsonify({
            "message": "product not found"
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)