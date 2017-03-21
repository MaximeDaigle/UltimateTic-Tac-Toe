#Gère l'entier représentant le jeu
from Game import Game
from GameTree import GameTree
from random import randint


class MetaGame:

    def __init__(self,entier):
        """
        :param entier: entier representant l'etat du jeu
        :return:
        """
        self.entier = entier #configuration en entier
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

    #TODO Afficher le dernier move en majuscule
    def afficherMeta(self):
        # Cette méthode affichera l'état de la méta game.
        stringMeta = ""
        for k in range(3):
            for i in range(3):
                stringMeta = ""
                for j in range(3):
                    cellContent = (self.entier >> ((80-(i+j+i*2+27*k))<<1) & 3)
                    if cellContent == 0:
                        stringMeta += " . "
                    if cellContent == 1:
                        stringMeta += " x "
                    if cellContent == 2:
                        stringMeta += " o " 
                    if (j+1)%3 == 0:
                        stringMeta += "|"
                for j in range(3):
                    cellContent = (self.entier >> ((80-(i+j+9+i*2+27*k))<<1) & 3)
                    if cellContent == 0:
                        stringMeta += " . "
                    if cellContent == 1:
                        stringMeta += " x "
                    if cellContent == 2:
                        stringMeta += " o " 
                    if (j+1)%3 == 0:
                        stringMeta += "|"
                for j in range(3):
                    cellContent = (self.entier >> ((80-(i+j+18+(i*2)+27*k))<<1) & 3)
                    if cellContent == 0:
                        stringMeta += " . "
                    if cellContent == 1:
                        stringMeta += " x "
                    if cellContent == 2:
                        stringMeta += " o " 
                print(stringMeta) 
            if k != 2:    
                print("-----------------------------")

    def winner(self):
        """
        Donne gagnant s'il y en a un et differencie partie nulle terminee d'une partie non-terminee
        :return: 1 si 'x' gagne, 2 si 'o' gagne, 'nulle' si terminer et pas de gagnant, sinon 'enCours'
        """

        completedGame = 0 #compte le nombre de sous-partie completer

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


        if completedGame == 9:
            return 'nulle'   #Si pas de victorieux et les tic-tac-toe sont tous completer

        else:
             return 'enCours'

    def possibleMoves(self):
        """
        :return: la liste des coups permis a partir de la configuration (l'entier) dans la metagame
        """
        result = []
        for i in self.playableBoard:
            result = result + self.ultimateBoard[i].findMoves()
        return result

    def getInt(self,move):
        """
        :param move: numero de la case ou le mouvement est fait
        :return: retourne la representation entiere de l'etat de la partie apres que le joueur actuel ait joué à la position move
        """

        configBinAvecLast = bin(self.entier)[2:] #configuration en binaire

        #Si depart de la partie, mettre la configuration en 169 bits
        if self.entier == 0:
            configBinAvecLast = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        #pad pour le manque de 0 vu que si last = '0000000' et joueur est X = '01', on perd les 8 bits premiers bits de '0'
        if len(configBinAvecLast) < 162:
            configBinAvecLast = '0' + configBinAvecLast

        configBin = configBinAvecLast[7 + (len(configBinAvecLast) - 169):] #enleve les bits donnant la dernier case jouer

        #modifie la case ou le joueur met sa marque
        newConfigBin = configBin[:move*2] + self.player + configBin[move*2 + 2:]
        last = bin(move)[2:]
        # while len(last) < 7:        #construit le 7 bits de la derniere case jouer
        #     last = '0' + last
        newConfigBin = last + newConfigBin #ajouter les 7 bits donnant la case où le dernier mouvement a été fait
        return int(newConfigBin, 2)

    def monteCarloTreeSearch(self,n):
        """
        Fait recherche arborescente montecarlo pour trouver le prochain move a faire selon l'entier de la metagame
        :param n: nombre de simulation a faire par possibilite de move
        :return: retourne l'entier representant la partie apres avoir fait le move qui est la plus grande probabiliter de victoire
                Si la partie est finie, retourne l'entier de la metagame sans changement
        """

        # Cree un arbre de profondeur 1 a partir de la configuration
        self.childrenMaker(1)

        #Verifie si la partie est deja finie
        if self.winner() != 'enCours':
            return self.entier

        if self.entier == 0: #S'il y a aucun move de fait dans la partie
            return self.getInt(randint(0,80)) #eviter de calculer et jouer au hasard

        # Si un des enfants est une victoire, le prendre
        for child in self.tree.root.children:
            if MetaGame(child.entier).winner() == int(self.player,2):
                return child.entier

        bestNode = None  # le noeud qui a le plus de succes

        for child in self.tree.root.children:  #pour chacun des moves possible
            count = 0 # compte le nombre de fois quon fait une simulation

            # Faire les simulations
            while(n > count):
                simulation = MetaGame(child.entier)

                while(simulation.winner() == 'enCours'): #complete la partie
                    nextMoves = simulation.possibleMoves()  #les moves permis parmis lequel on va choisir
                    simulation = MetaGame(simulation.getInt(nextMoves[randint(0,len(nextMoves)-1)]))  #fait un move au hasard

                count += 1 #une simulation de plus de completer
                child.updateWinCount(simulation.winner(), self.player)  #mets a jour le nombre fois que le joueur a gagner avec ce mouvement
            #/Fin de la simulation pour ce noeud

            #Choisir le move qui maximise le taux de succes
            #en comparant le noeud auquel on vient de finir de faire les simulations avec le meilleur noeud qu'on avait avant
            if bestNode is None:   #S'il y a pas encore de node selectionner
                bestNode = child
                # if bestNode is None:  #Si le bestNode est toujours None, child est None, alors il n'a pas eu de possibiliter de faire ou mouvement
                #     return self.entier    #alors retourne l'entier de depart car pas possible d'envoyer un entier suite a un move
            elif child.winCount > bestNode.winCount: #si child a gagner plus souvent que bestNode
                bestNode = child   #child devient le bestNode

        return bestNode.entier



    def childrenMaker(self,depth, etageCourant = None, show = False):
        """
         Cree les children des noeud feuilles de facon recursive jusqu'a ce que l'arbre ait la profondeur voulue
         :param depth: profondeur de children a faire
         :param etageCourant: l'etage de noeud dans larbre qui se fait ajouter des enfants si il en a pas deja
         :param print: si vrai, print les entiers de l'arbre etage par etage
         :return:
         """
        if depth == self.tree.depth:
            if depth == 0 and show:
                print(self.tree.root.entier)

            elif show:#imprimer la derniere etage si on veut show
                toPrint = ''
                etageParent = etageCourant
                etageCourant = []
                for e in etageParent:
                    etageCourant = etageCourant + e.children
                for e in etageCourant:
                    toPrint = toPrint + ' ' + str(e.entier)
                print(toPrint[1:])

            return

        end = False  #boolean disant si on a atteint la fin de l'arbre et qu'on a bien ajouter des enfants a l'etageCourant

        if etageCourant is None:
            etageCourant = self.tree.root #commencer par la racine de larbre

        #Cas ou root est la profondeur maximale
        if self.tree.depth == 0:
            if show:
                print(self.tree.root.entier)
            self.ajoutDesChildren(self.tree.root)
            self.tree.depth += 1
            return self.childrenMaker(depth, [self.tree.root], show)

        #Cas ou les enfants de root sont la profondeur maximale
        if self.tree.depth == 1:
            etageCourant = self.tree.root.children #prend les enfant de root
            toPrint = ''
            for noeud in etageCourant:
                toPrint = toPrint + ' ' + str(noeud.entier)
                if self.ajoutDesChildren(noeud):
                    end = True
            if show:
                print(toPrint[1:])
            if end:
                self.tree.depth += 1
                return self.childrenMaker(depth, etageCourant, show)
            else:
                return False #peut pas ajouter plus de profondeur a l'arbre

        while (not end):
            etageParent = etageCourant #etageParent permet de mettre tous les enfants de letage suivant dans l'etageCourant
            etageCourant = []
            toPrint = ''
            for e in etageParent: #pour chaque noeud parent
                etageCourant = etageCourant + e.children     #ajoute ses enfants dans letage qui suit
                if show:
                    for noeud in e.children:
                        toPrint = toPrint + ' ' + str(noeud.entier)
            if show:
                print(toPrint[1:])
            count = 0
            for noeud in etageCourant:
                if noeud.no_child():
                    if self.ajoutDesChildren(noeud): #sil y a eu lajout denfant
                        end = True                   #fin de lajout dune etage quand terminer de passer pour chaque noeud dans letage
                    else:
                        count +=1 #compte le nombre de noeud sans enfant auqel on ne peut pas ajouter denfant
            if count == len(etageCourant): #Si chaque noeud sans enfant ne peuvent pas se faire ajouter d'enfant
                return False  #retourner False car il est faux qu'on peut ajouter des enfants jusqu'a la profondeur souhaiter
        self.tree.depth += 1
        return self.childrenMaker(depth, etageCourant, show)

    def ajoutDesChildren(self, currentNode):
        """
        Trouve tous les entiers possible d'obtenir apres un mouvement a partir de l'entier stocker dans le noeud courant
        puis creer les enfants au noeud courant pour stocker les entiers obtenus
        :param currentNode: le noeud auquel on ajoute les enfants
        :return: True sil y a eu lajout denfant sinon False
        """

        currentGame = MetaGame(currentNode.entier)
        moveToDo = currentGame.possibleMoves() #contient tous les moves possible a faire a partir de la configuration dans le noeud courant

        if len(moveToDo) == 0:  #Sil ny pas de move possible a partir du noeud courant, ajoutDesChildrens renvoie False
            return False

        entierPourNewNode = []  #tous les entiers possibles d'obtenir a partir du noeud courant
        for move in moveToDo:
            entierPourNewNode.append(currentGame.getInt(move))

        #Ajoute tous les enfants
        for e in entierPourNewNode:
            currentNode.addChild(e)

        return True