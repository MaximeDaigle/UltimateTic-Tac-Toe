from MetaGame import MetaGame


entier = 427544177957277136960806942631752826923977077466713
#entier = 2247201493984387763534656311314468204100707460697
game = MetaGame(entier)
# game.afficherMeta()

game = MetaGame(game.getInt(0))
game.afficherMeta()

game = MetaGame(game.getInt(2))
game.afficherMeta()







# game = MetaGame(game.getInt(1))
# game.afficherMeta()
# print()
# for i in range(10):
#     game = MetaGame(game.getInt(i+20))
#     game.afficherMeta()
#     print()
#
# game = MetaGame(game.getInt(0))
# game.afficherMeta()
# print()
#