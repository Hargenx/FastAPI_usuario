# FastAPI GitHub API Wrapper

Este projeto utiliza o FastAPI para criar uma API que consome a API pública do GitHub, fornecendo endpoints para obter informações sobre repositórios e usuários do GitHub.

## Requisitos

Certifique-se de ter Python instalado. Você pode instalar as dependências utilizando:

```bash
pip install -r requirements.txt
```

## Funcionalidades
- /repositories/{owner}/{repo}/issues: Retorna as issues de um repositório específico.
- /repositories/{owner}/{repo}/stars: Retorna o número de estrelas de um repositório.
- /users/{username}/repos/count: Retorna a contagem de repositórios públicos de um usuário.
- /users/{username}: Retorna informações de um usuário do GitHub.
- /repositories/{owner}: Retorna os repositórios de um determinado usuário.

## Uso

1- Inicie o servidor com o comando:
```bash
uvicorn main:app --reload
```

2- Acesse a documentação interativa da API em http://127.0.0.1:8000/docs para visualizar os endpoints e testar as requisições.

## Exemplos de Uso
### Obter issues de um repositório
```python
GET /repositories/{owner}/{repo}/issues
```

### Obter número de estrelas de um repositório
```
GET /repositories/{owner}/{repo}/stars
```
### Obter contagem de repositórios de um usuário
```
GET /users/{username}/repos/count
```
### Obter informações de um usuário
```
GET /users/{username}
```
### Obter repositórios de um usuário
```
GET /repositories/{owner}
```
## Contribuição
Sinta-se à vontade para contribuir com novos recursos, melhorias de código ou correções de bugs. Abra um Pull Request ou uma issue para discutir suas ideias.

## Autor
`[Raphael M. S. de Jesus]` - `[@Hargenx]`