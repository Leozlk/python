"""
Created by Leonardo Rodrigues Silva
Python 3.5.1 - 2016

Gera um arquivo .txt em / com os dados fornecidos pulando linha.
"""
import os
from datetime import datetime
print("- Created by Leonardo Rodrigues Silva (c) 2016 -")
def main():
    filename = input("Filename: ") + ".txt"
    def checkFor_txt():
        if os.path.isfile(filename):
            print("The file already exists! Calling insert function.")
            insert_entry()
        else:
            print("The file doesn\'t exists. Creating new...")
            generate_txt()
    def generate_txt():
            choice = input("Do you really want to create the '"+filename+"' file \nin the actual folder? (y)es or (n)o: ")
            if(choice == "y" or choice == "Y"):
                file = open(filename,"w")
                file.write("- Generated at "+str(datetime.now())+" -")
                file.close()
                insert_entry()
            else:
                print("Returning to the main function.")
                main()
    def insert_entry():
        entry = input("Insert the link to append: ")
        if entry != "":
            file = open(filename,"a")
            file.write("\n"+entry)
            file.close()
            insert_entry()
        else:
            print("Please insert a valid link!")
            insert_entry()
    checkFor_txt()
main()
