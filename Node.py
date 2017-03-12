#Noeud dans l'arbre de jeu
from MetaGame import MetaGame


class Node:
    #TODO
    def __intit__(self, entier):
        pass
        self.winRate
        self.entier = entier
        self.config = bin(entier)[2:]
        self.children = []
        self.metagame = MetaGame(entier)  #TODO contient le MetaGame


    #TODO
    def sample(self,n):
        """
        à partir de la configuration à ce noeud, effectuer n simulations de coups aléatoires jusqu'à la fin de partie et garder les statistiques du nombre de parties gagnées par x et gagnées par o (les autres étant nulles)
        :param n:
        :return:
        """

    def winCheck(self):
        pass
        #TODO
        #Check sil y a victoire du joueur

    def move(self):
        pass
        #modifie config et entier

    def childrenMaker(self,depth):
        """
        Cree les children du noeud jusqu'a la profondeur voulue
        :param depth: profondeur des children a faire
        :return:
        """
        # if depth == 0:
        #     return
        # else:
        #     for board in self.playableBoard: #passer a chaque board ou il est possible de jouer
        #         moveToDo = board.possibleMoves() #prendre tous les moves possibles pour ce board
        #         for config in configs:
        #             self.children.append(Node(config))