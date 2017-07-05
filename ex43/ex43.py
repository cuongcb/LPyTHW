# Ex43 from LPyTHW - A Game
from ex43.maps import Map
from ex43.engine import Engine

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
