#Gère un jeu de tic-tac-toe standard

class Game:

    def __intit__(self,entier,board):
        """
        :param entier: l'entier representant la partie
        """
        self.board = board # le board de tic-tac-toe classic a regarder parmi les 9 de l'ultimate (peut aller de 0 a 8)
        self.entier = entier
        self.winner = self.gameStatus() #etat du board: 1(pour winner x) ou 2(pour winner o) ou 'nulle' ou 'enCours'
        # TODO

    #TODO TESTER
    def gameStatus(self):
        """
        Verifie si la partie est fini et donne le gagnant s'il y a eu
        :return: 1 ou 2 ou 'nulle' ou 'enCours'
        """
        firstCase = self.board*9 #Premiere case du board

        #Verifie s'il y a un tic-tac-toe
        upperLeft = self.entier >> ((80-firstCase)<<1) & 3
        upperRight = self.entier >> ((80-(firstCase + 2))<<1) & 3

        #top horizontal
        if upperLeft == upperRight and upperRight == (self.entier >> ((80-(firstCase + 1))<<1) & 3):
            return upperLeft

        lowerLeft = self.entier >> ((80-(firstCase + 6))<<1) & 3

        #premiere colonne
        if upperLeft == lowerLeft and lowerLeft == (self.entier >> ((80-(firstCase + 3))<<1) & 3):
            return upperLeft

        lowerRight = self.entier >> ((80 - (firstCase + 8)) << 1) & 3

        #3e horizontale
        if lowerLeft == lowerRight and lowerLeft == (self.entier >> ((80-(firstCase + 7))<<1) & 3):
            return lowerLeft

        # 3e colonne
        if upperRight == lowerRight and lowerRight == (self.entier >> ((80 - (firstCase + 5)) << 1) & 3):
            return upperRight

        middle = (self.entier >> ((80-(firstCase + 4))<<1) & 3)

        #premiere diagonale
        if upperLeft == lowerRight and lowerRight == middle:
            return upperLeft

        #deuxieme diagonale
        if upperRight == lowerLeft and upperRight == middle:
            return upperRight

        #2e horizontale
        if middle == (self.entier >> ((80-(firstCase + 3))<<1) & 3) and middle == (self.entier >> ((80-(firstCase + 5))<<1) & 3):
            return middle

        #2e colonne
        if middle == (self.entier >> ((80-(firstCase + 1))<<1) & 3) and middle == (self.entier >> ((80-(firstCase + 7))<<1) & 3):
            return middle

        #Verifie si tous les cases sont remplis et donc la partie est nulle, ou si la partie est en cours
        total = 0 #total de case remplie
        for i in range(firstCase, firstCase + 9): #les cases dans le board de la game specifique
            if (self.entier >> ((80-i)<<1) & 3) != 0:
                total += 1                           #si pas vide, augmente le total de case remplie
        if total == 9:
            return 'nulle'
        else:
            return 'enCours'

    #TODO
    def move(self,case):
        """
        Fait un move sur le board selon le field /player/
        :param case: numero de la case ou le move est fait
        :return: True s'il fait un move, False sinon
        """
        if self.winner == 'enCours':
            pass
            #TODO fait le move
            self.gameStatus()
            return True
        else:
            return False

    #TODO TESTER
    def findMoves(self):
        """
        :return: une liste de move possible
        """
        result = []
        firstCase = self.board * 9  # Premiere case du board
        for i in range(firstCase, firstCase + 9):  #pour toutes les cases de ce board
            if (self.entier >> ((80-i)<<1) & 3) == 0: #si la case est vide, l'ajouter dans les  mouvements possibles
                result.append(i)
        return result