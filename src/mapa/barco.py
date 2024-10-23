class Barco:
    """Objeto que representa un barco, con su nombre, coordenadas y puntos."""

    def __init__(self, nombre, coordenadas=[], puntos=0):
        """
        nomber: str
        coordenadas: int[2]
        puntos: int
        """
        self.nombre = nombre
        self.puntos = puntos
        self.coordenadas = coordenadas

    def __str__(self):
        return f"{self.nombre}: (puntos={self.puntos}, coordenadas={self.coordenadas})"

    def full(self):
        return self.puntos and self.coordenadas
