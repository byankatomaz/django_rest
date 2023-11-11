import requests

class TestCursos:

    headers = {'Authorization': 'Token 4d25fcb44d7c906cea1f1853aa7d77d00c4f4d52'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
    
    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        
        assert cursos.status_code == 200
    
    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)
        
        assert curso.status_code == 200
    
    
    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso de IOT",
            "url": "http://www.udemy.com/IOT"
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)
 
        assert resultado.status_code == 201
    
    
    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso novo de IA",
            "url": "http://www.udemy.com/NOVOIA"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizado)
 
        assert resposta.status_code == 200
    
    
    def test_del_curso(self):
        
        resultado = requests.delete(url=f'{self.url_base_cursos}5/', headers=self.headers)

        assert resultado.status_code == 204