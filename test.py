from MetaGame import MetaGame

#entier = 459329034283597291728327479273734123420780266358036
entier = 0
mainGame = MetaGame(entier)
mainGame.afficherMeta()
print()
#
for i in range(80):
    firstMove = MetaGame(mainGame.monteCarloTreeSearch(1000))
    firstMove.afficherMeta()
    mainGame = firstMove
    print()

# firstMove = MetaGame(mainGame.monteCarloTreeSearch(1000))
# firstMove.afficherMeta()
# print()
# secondMove = MetaGame(firstMove.monteCarloTreeSearch(1))
# secondMove.afficherMeta()
# print()
# thirdMove = MetaGame(secondMove.monteCarloTreeSearch(1000))
# thirdMove.afficherMeta()
# print()
# firstMove2 = MetaGame(thirdMove.monteCarloTreeSearch(1000))
# firstMove2.afficherMeta()
# print()
# secondMove2 = MetaGame(firstMove2.monteCarloTreeSearch(1000))
# secondMove2.afficherMeta()
# print()
# thirdMove2 = MetaGame(secondMove2.monteCarloTreeSearch(1000))
# thirdMove2.afficherMeta()
# print()

#
# # print(mainGame.getPlayableBoard())
# # print(mainGame.winner())
# #print(mainGame.possibleMoves())
#
# afterMove = MetaGame(mainGame.getInt(54))    #cree nouveau metagame ou un 'o' est fait a la case 54
# afterMove.afficherMeta()
# print(int(afterMove.player,2))
# print()
# #print(afterMove.getPlayableBoard())
# #print(afterMove.possibleMoves())
#
# secondMove = MetaGame(afterMove.getInt(12))
# secondMove.afficherMeta()
# print(int(secondMove.player,2))
# #print(secondMove.possibleMoves())