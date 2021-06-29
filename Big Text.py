# -*- coding: utf-8 -*-

from colorama import Fore, init
from os import system, name
from art import * 

def clear():
    system("cls") if name == 'nt' else system("clear")


clear()

if name == "nt":
    try:
        system("title Big Text")
        system("mode 160, 40")
    except:
        pass

print(Fore.MAGENTA+"""\n\n
                                                        ____  _         _____         _   
                                                        | __ )(_) __ _  |_   _|____  _| |_ 
                                                        |  _ \| |/ _` |   | |/ _ \ \/ / __|
                                                        | |_) | | (_| |   | |  __/>  <| |_ 
                                                        |____/|_|\__, |   |_|\___/_/\_\\__|
                                                                |___/                     """)
print(Fore.RED+ """
                                                             par simnJS | by simnJS\n\n\n""")

print(Fore.MAGENTA+ "Polices d'écritures disponible : block, random, rnd-small, rnd-medium, italic, ghost, defauld, big.\n\n")
font = input(Fore.GREEN + "Entrez une police d'écriture depuis la liste ce dessus :  > ")
text = input(Fore.GREEN + "Entrez le texte que vous souhaiter :  > ")


big=text2art(text,font=font,chr_ignore=True) # Return ASCII text with block font
input(Fore.RED + big)

txt = input(Fore.BLUE + "\nVoulez vous récupérer le big text dans un .txt ? [y/n] ")
if txt == 'y':
    with open("BigText.txt", 'w') as f:
        f.write(big)
        f.close()