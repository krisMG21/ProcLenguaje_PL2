class Jugador:
    def __init__(self, vida: int, puntos: int, nombre: str = "Jugador"):
        self.nombre = nombre
        self.vida = vida
        self.puntos = puntos

    def __str__(self):
        return f"{self.nombre}, vida: {self.vida} puntos: {self.puntos}"

    def dañar(self, puntos: int):
        self.vida -= puntos
        if self.vida <= 0:
            self.vida = 0

    def add_puntos(self, puntos: int):
        self.puntos += puntos
