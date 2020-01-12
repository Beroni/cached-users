# Cached Users

### Bibliotecas Utilizadas:

1. `time`
2. `os`
3. `sys`
4. `csv`
5. `requests`
6. `json`



## Requisitos

1. Solução deve funcionar com Python 3.6 :heavy_check_mark:
2. Utilização da biblioteca `requests` :heavy_check_mark:
3. Arquivo deverá começar vazio :heavy_check_mark:
4. Ao executar o programa uma vez para um determinado username deve adicionar apenas os dados do username consultado :heavy_check_mark:
5. Em consultas futuras desse username, deve retornar os dados do CSV, sem fazer consulta na API :heavy_check_mark:

## Solução

* Para o cache foi utilizado um dicionário de dicionários para facilitar a busca indexada pelo própio nome do usuário.

Exemplificando a estrutura de dados utilizada: 
```python
cache = {
    Bret : {
        email: Sincere@april.biz,
        website: hildegard.org,
        hemisphere: sul,
        username: Bret 
    },
    Antonette : {
        email: Shanna@melissa.tv,
        website: anastasia.net,
        hemisphere: sul,
        username: Antonette 
    }
}

# Então para buscar o usuário Bret é só utilizar

user = cache['Bret']

```

* O formato de utilização do csv abaixo é para facilitar a exibição de dados na tela.

Formato dos dados no csv:

```csv
username,email,website,hemisphere
Bret,Sincere@april.biz,hildegard.org,sul
Antonette,Shanna@melissa.tv,anastasia.net,sul
```
