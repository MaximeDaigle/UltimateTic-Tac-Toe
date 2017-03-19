#l'arbre de jeu
from Node import Node

class GameTree:

    def __init__(self,entier,depth = 0):
        self.depth = depth
        self.root = Node(entier)

    def getDepth(self):
        return self.depth