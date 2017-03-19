#Noeud dans l'arbre de jeu

class Node:
    #TODO
    def __init__(self, entier, parent = None):
        # à faire le winrate
        self.parent = parent
        self.winCount = 0
        self.entier = entier
        self.children = []

    #TODO
    def sample(self,n):
        """
        à partir de la configuration à ce noeud, effectuer n simulations de coups aléatoires jusqu'à la fin de partie et garder les statistiques du nombre de parties gagnées par x et gagnées par o (les autres étant nulles)
        :param n:
        :return:
        """

    def updateWinCount(self, winner, player):
        """
        Mets a jour le winrate
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
        self.children.append(Node(entier,self))