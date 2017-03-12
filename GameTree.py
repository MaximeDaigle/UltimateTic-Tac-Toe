#l'arbre de jeu
from Node import Node

class GameTree:

    def __init__(self,entier,depth = 0):
        pass
        #TODO
        self.depth = depth
        self.root = Node(entier)
        self.root.childrenMaker(depth)