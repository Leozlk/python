# - Python
# Gera senha aleatória com quantidade de caracteres definida pelo usuário.
# gerador_senha2.py - by Leonardo Rodrigues Silva - 2016
#
import string
import random
i = 0
size = input("Insira o tamanho da senha: ")
password = ""
for i in range(int(size)):
    chars = random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    password += chars
print(password)
