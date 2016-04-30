# - Python
# Busca endereço do CEP informado.
# busca_endereco.py - by Leonardo Rodrigues Silva - 2016
#
import urllib.request
import json
cep = input("Insira o CEP: ")
url = 'http://correiosapi.apphb.com/cep/' + str(cep)
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
print(str("Rua: "+(data['logradouro'])))
print(str("Bairro: "+(data['bairro'])))
print(str("Cidade: "+(data['cidade'])))
