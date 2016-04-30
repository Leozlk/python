# - Python
# Conecta a um servidor FTP e envia um arquivo gerado pelo próprio Script.
# ftp.py - by Leonardo Rodrigues Silva - 2016
#
import os
import time
import ftplib
print("Teste Python/FTP - Leonardo Rodrigues Silva 2016")
#Cria um arquivo .txt para ser enviado para o servidor
textw = open("resultado.txt", "wb")
textr = open("resultado.txt", "rb")
textw.write("Criado por Leonardo Rodrigues Silva (c) 2016")
textw.write("\nTeste Python/FTP!")
textw.close()
data = textr.read()
#Nome do Arquivo é enviado como o logon_da_máquina.txt -- Efetuado teste em um RedHat
filename = str(os.getlogin())
fileupload = open("resultado.txt", "rb")
ftp = ftplib.FTP("ftp.SEU_FTP")
ftp.login("USUARIO","SENHA")
ftp.storlines("STOR "+filename,fileupload)
ftp.retrlines("LIST")
