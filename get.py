import requests

base_url = 'http://localhost:5000'

new_product = {
    'name': 'Tomate',
    'price': 08.50
}

response = requests.post(f'{base_url}/products', json=new_product)

if response.status_code == 201:
    new_product_data = response.json()
    print('Novo produto criado:')
    print(new_product_data)
else:
    print('Erro ao criar o novo produto.')
    print(response.json())
