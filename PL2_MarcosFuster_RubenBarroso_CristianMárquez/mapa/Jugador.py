class Jugador:
    def __init__(self, vida: int, puntos: int):
        self.vida = vida
        self.puntos = puntos

    def __str__(self):
        return f"Jugador: {vida: {self.vida} puntos: {self.puntos}}"

    def dañar(self, puntos: int):
        self.vida -= puntos
        if self.vida <= 0:
            self.vida = 0

    def add_puntos(self, puntos: int):
        self.puntos += puntos
