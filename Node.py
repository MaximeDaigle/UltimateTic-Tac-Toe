#Noeud dans l'arbre de jeu

class Node:

    def __init__(self, entier, parent = None):
        # à faire le winrate
        self.parent = parent
        self.winCount = 0
        self.entier = entier
        self.children = []

    def updateWinCount(self, winner, player):
        """
        Mets a jour le nombre de victoire du joueur
        :param winner: le gagnant de la simulation
        :param player: est '01' si le joueur est 'x', sinon '10' pour un joueur 'o'
        :return:
        """
        if winner == int(player,2):
            self.winCount += 1


    def no_child(self):
        """
        :return: boolean True si pas d'enfant, sinon False
        """
        return len(self.children) == 0

    def addChild(self,entier):
        """
        Ajoute un enfant au noeud self
        :param entier: entier qu'on veut stocker dans un enfant
        """
        self.children.append(Node(entier,self))