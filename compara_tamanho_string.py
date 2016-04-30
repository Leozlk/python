# - Python
# Compara tamanho de duas strings informadas pelo usuário.
# by Leonardo Rodrigues Silva - 2016
#
string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")
print(str('Tamanho de "'+string1+'": '+str(len(string1)))+' caracteres')
print(str('Tamanho de "'+string2+'": '+str(len(string2)))+' caracteres')
if(string1 == string2):
    print("As strings possuem conteudo igual")
else:
    print("As strings possuem conteudo diferente")
if(len(string1) != len(string2)):
    print("Strings de tamanhos diferentes")
else:
    print("Strings de tamanhos diferentes")
