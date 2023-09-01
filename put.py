import requests

base_url = 'http://localhost:5000'
product_id = 1

updated_product = {
    'name': 'Tomate',
    'price': 15.50
}

response = requests.put(f'{base_url}/product/{product_id}', json=updated_product)

if response.status_code == 200:
    updated_product_data = response.json()
    print('Produto atualizado:')
    print(updated_product_data)
else:
    print('Erro ao atualizar o produto.')
    print(response.json())
