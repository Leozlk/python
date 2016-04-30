# - Python
# Teste simples de placeholder.
# placeholder.py - by Leonardo Rodrigues Silva - 2016
#
paises = ['Brasil', 'Alemanha', 'Rússia', 'Estados Unidos', 'Inglaterra','Canadá']
ingles = [paises[3], paises[4],paises[5]]
count = (str(len(ingles)))
mensagem = 'Os países que falam inglês são %s'
for i in count:
    print(mensagem%(i))
