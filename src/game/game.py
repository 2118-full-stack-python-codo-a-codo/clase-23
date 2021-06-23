from src.game.player import Player


class Game:
    player1 = Player
    player2 = Player

    def __init__(self) -> None:
        """
        Solo el constructor
        """
        pass
    
    def __str__(self) -> str:
        return f"Esto es el objeto Game"
    
    def start(self) -> bool:
        pass

    def end(self) -> bool:
        pass
    
    def update(self) -> bool:
        pass