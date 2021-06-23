from game.game import Game

class Monopoly(Game):

    def __init__(self) -> None:
        super().__init__()
    

    def start(self) -> bool:
        myVariable = True
        return myVariable and super().start()