from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Dados simulados - você pode substituir isso por um banco de dados real
products = {}

class ProductResource(Resource):
    def get(self, product_id):
        if product_id in products:
            return products[product_id]
        else:
            return {'message': 'Product not found'}, 404

    def put(self, product_id):
        if product_id in products:
            data = request.get_json()
            products[product_id] = data
            return {'message': 'Product updated', 'product': products[product_id]}
        else:
            return {'message': 'Product not found'}, 404

    def delete(self, product_id):
        if product_id in products:
            del products[product_id]
            return {'message': 'Product deleted'}, 204
        else:
            return {'message': 'Product not found'}, 404

class ProductListResource(Resource):
    def get(self):
        return products

    def post(self):
        data = request.get_json()
        product_id = len(products) + 1  # Simplesmente usando um número sequencial como ID
        products[product_id] = data
        return {'message': 'Product created', 'product': products[product_id]}, 201

api.add_resource(ProductResource, '/product/<int:product_id>')
api.add_resource(ProductListResource, '/products')

if __name__ == '__main__':
    app.run(debug=True)
