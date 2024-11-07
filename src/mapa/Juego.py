from Jugador import Jugador
from Nivel import Nivel


class Juego:
    def __init__(self, jugador: Jugador, nivel: Nivel):
        self.jugador = jugador
        self.nivel = nivel
