import sys

from MetaGame import MetaGame

try:
    parametre = sys.argv[1]
except IndexError:
    parametre = input("add a parameter")

#mode arbre
if parametre[1] == 'a':
    pass #TODO

#mode affichage
elif parametre[1] == 'p':
    pass #TODO

#mode par default, l'argument est une configuration et le program joue un coup et retourne le nouveau entier
else:
    initial = MetaGame(parametre)
    print() #le nouveau entier
    pass #TODO