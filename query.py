import requests
import pandas as pd

# Token de autenticação
token = 'eyJhbGciOiJSUzUxMiJ9.eyJhbWJpZW50ZSI6IlBST0RVQ0FPIiwiaWQiOiIxMzk1NjM2NTAwMDEzNiIsInBmbCI6IlBKIiwiY25waiI6IjEzOTU2MzY1MDAwMTM2IiwiY2FydGFvLXBvc3RhZ2VtIjp7Im51bWVybyI6IjAwNzcxMjY1NDgiLCJjb250cmF0byI6Ijk5MTI1NzU5NzEiLCJkciI6MjgsImFwaSI6WzI3LDM0LDM1LDM2LDM3LDQxLDc2LDc4LDgwLDgzLDg3LDkzLDU2Niw1ODddfSwiaXAiOiIyMDAuMTQxLjEwNS4xNDEsMjAwLjE0MS4xMDUuMTQxIiwiaWF0IjoxNjkxMjQ0MDQzLCJpc3MiOiJ0b2tlbi1zZXJ2aWNlIiwiZXhwIjoxNjkxMzMwNDQzLCJqdGkiOiJjMWM3MTEwNy1iMzk0LTRmZGItYmE5YS0yYTRmZmY0NDYzOGIifQ.NJPTX4BzELKJw6jreDw-Am0hn-ko6aPJDCuXuxzwsgDOTGh29vDhKSt8QvJa7at09_J5ZCzPoT6_AKFnCHhavddgpgOxy-01zvAU89Ro_yEqmPPC3ORaOvdKk2-jF-MFHnlj-Yjj4-Cne0kfWCYyjfSu9gLpzsxFJ4NtT0Z_LXB173-nKlYrFHUYOrE6U13X1e0LOnjQlpixbYIdw1r6AA2x5ci7XhsHByVqZ3qsvFco06SQFG-p12x2GINcm8hWTJX35QCXfhqIzYONBbRGWi7qjUPWpdmnaUdzYUzjMm91E6dMcy1lblpG79FiTSCc5bskD4Xk5i5K7eGzxeo_gw'

# URL da API que requer autenticação
api_url = 'https://api.correios.com.br/srorastro/v1/objetos/rastrosdocumento?documento=13956365000136&resultado=T&destinatario-remetente=R'

# Configuração do cabeçalho com a autenticação básica
headers = {
    'Authorization': f'Bearer {token}'
}

# Fazendo a solicitação à API
response = requests.get(api_url, headers=headers)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f'Erro na chamada da API: {response.status_code}')

dadosEstruturados = pd.DataFrame(dados)
print(dadosEstrturados)

