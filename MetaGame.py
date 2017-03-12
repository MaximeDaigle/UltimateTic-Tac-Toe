# Gère l'entier représentant le jeu
from Game import Game
from GameTree import GameTree


class MetaGame:

    def __intit__(self, entier):
        """
        :param entier: entier representant l'etat du jeu
        :return:
        """
        self.entier = entier #configuration en entier
        self.configBin = bin(entier)[9:] #configuration en binaire sans les 7 bits de last
        self.last = entier >> 162 & 127  #case ou le dernier mouvement a ete fait

        self.ultimateBoard = []  # Contient les 9 sous-parties de tic-tac-toe

        for i in range(9):
            self.ultimateBoard.append(Game(entier, i))

        if entier >> ((80- self.last)<<1) & 3 == 1: #si dernier mouvement fait par 'x'
            self.player = '10'                  #le joueur est maintenant 'o'
        else:
            self.player = '01'     #sinon mainteant joueur est 'x'

        self.tree = GameTree(entier)
        self.playableBoard = self.getPlayableBoard()

    #TODO TESTER
    def getPlayableBoard(self):
        """
        Selectionne les boards ou on peut jouer
        :return: liste de int (allant de 0 a 8)
        """
        board2Check = self.last % 9 #le board ou le dernier move envoie le joueur

        # si ce board est jouable, renvoyer le board
        if self.ultimateBoard[board2Check].winner == 'enCours':
            return [board2Check]

        # sinon, trouver tous les autre boards non completer
        else:
            result = []
            for i in range(9):
                if i == board2Check:
                    continue
                if self.ultimateBoard[i].winner == 'enCours':
                    result.append(i)
            return result

    # TODO TESTER
    def winner(self):
        """
        Donne gagnant s'il y en a un et differencie partie nulle terminee d'une partie non-terminee
        :return: 1 si 'x' gagne, 2 si 'o' gagne, 'nulle' si terminer et pas de gagnant, sinon 'enCours'
        """

        #Verifie le gagnant s'il y a eu lieu
        completedGame = 0

        #Fait la liste des sous tic-tac-toe ou il y a un gagnant et
        gameWon = []
        for i in range(9):
            if isinstance(self.ultimateBoard[i].winner, int):
                gameWon.append(i)

            if self.ultimateBoard[i].winner != 'enCours':
                completedGame += 1

        for i in range(3):
            if i in gameWon:

                #Verifie les colonnes
                if self.ultimateBoard[i].winner == self.ultimateBoard[i+3].winner and self.ultimateBoard[i].winner == self.ultimateBoard[i+6].winner:
                    return self.ultimateBoard[i].winner

            if 3*i in gameWon:

                #Verifie les horizontales
                if self.ultimateBoard[3*i].winner == self.ultimateBoard[3*i + 1].winner and self.ultimateBoard[3*i].winner == self.ultimateBoard[3*i + 2].winner:
                    return self.ultimateBoard[3*i].winner

        if 4 in gameWon:
            #Verifie les diagonales
            if self.ultimateBoard[4].winner == self.ultimateBoard[0].winner and self.ultimateBoard[4].winner == self.ultimateBoard[8].winner:
                return self.ultimateBoard[4].winner

        #Si pas de victorieux et les tic-tac-toe sont tous remplis
        if completedGame == 9:
            return 'nulle'

        else:
             return 'enCours'

    # TODO TESTER
    def possibleMoves(self):
        """
        Donne la liste des coups permis a partir de la configuration actuelle
        """
        result = []
        for i in self.playableBoard:
            result = result + self.ultimateBoard[i].findMoves()
        return result



    # TODO
    def getInt(self,move):
        """
        :param move:
        :return: retourne la representation entiere de l'etat de la partie apres que le joueur actuel ait joué à la position move
        """

    def MonteCarloTreeSearch(self):
        pass
        #TODO
        #result = [] #le winRate
        # Cree un arbre de profondeur 1 a partir de la configuration

        # Si un des enfants est une victoire, le prendre

        #else:
        #   for i in range(len(root.children)):
        #       root.children[i].sample(1000)
        #       result[i] = root.children[i].winRate

        # Selectionner le noeud correspondant au result le plus grand
