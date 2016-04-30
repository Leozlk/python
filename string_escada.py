# - Python
# Efetua print da palavra informada em forma de escada
# string_escada.py - by Leonardo Rodrigues Silva - 2016
#
string = input("Insira a string: ")
cpl = ""
i = 0
for i in range(len(string)):
    cpl += string[i]
    print(cpl)
