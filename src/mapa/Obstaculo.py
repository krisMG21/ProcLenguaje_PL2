class Obstaculo:
    """Objeto que representa un obstáculo, con su nombre, coordenadas y daño."""

    def __init__(self, nombre: str, coordenadas: list = [], daño: int = 0):
        self.nombre = nombre
        self.daño = daño
        self.coordenadas = coordenadas

    def __str__(self):
        return f"{self.nombre}: (puntos={self.daño}, coordenadas={self.coordenadas})"

    def full(self):
        return self.coordenadas != ()
