import requests

headers = {'Authorization': 'Token 4d25fcb44d7c906cea1f1853aa7d77d00c4f4d52'}

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

novo_curso = {
    "titulo": "Curso de Git e Github",
    "url": "http://www.udemy.com"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201