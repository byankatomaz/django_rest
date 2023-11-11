import requests

headers = {'Authorization': 'Token 4d25fcb44d7c906cea1f1853aa7d77d00c4f4d52'}

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

curso_atualizado = {
    "titulo": "Curso de Scrum",
    "url": "http://www.udemy.com/Scrum"
}

resultado = requests.put(url=f'{url_base_cursos}1/', headers=headers, data=curso_atualizado)

print(resultado.status_code)