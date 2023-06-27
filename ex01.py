import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
#print(response.text)
palavras = response.text.split('\n')
print(len(palavras))
print(palavras[20000])