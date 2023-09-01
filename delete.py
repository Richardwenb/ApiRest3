import requests

base_url = 'http://localhost:5000'
product_id = 1

response = requests.delete(f'{base_url}/product/{product_id}')

if response.status_code == 204:
    print('Produto excluído com sucesso.')
else:
    print('Erro ao excluir o produto.')
    print(response.json())
