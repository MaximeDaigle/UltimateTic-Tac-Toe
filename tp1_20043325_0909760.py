import sys

from MetaGame import MetaGame

try:
    parametre = sys.argv[1]
except IndexError:
    parametre = input("rentrer un entier")


#mode arbre
if parametre == 'a':
    stateOfGame = MetaGame(int(sys.argv[3]))
    stateOfGame.childrenMaker(int(sys.argv[2]), None, True)

#mode affichage
elif parametre == 'p':
    stateOfGame = MetaGame(int(sys.argv[2]))
    stateOfGame.afficherMeta()

#mode par default, l'argument est une configuration et le program joue un coup et retourne le nouveau entier
else:
    initial = MetaGame(int(parametre))
    print(initial.monteCarloTreeSearch(1000)) #le nouveau entier