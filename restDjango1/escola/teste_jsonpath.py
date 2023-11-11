import requests
import jsonpath

headers = {'Authorization': 'Token 4d25fcb44d7c906cea1f1853aa7d77d00c4f4d52'}

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers)

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultados)