from antlr4 import InputStream, CommonTokenStream
from MapaTesoroParser import MapaTesoroParser
from MapaTesoroLexer import MapaTesoroLexer
from MapaTesoroListener import MapaTesoroListener


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


class MapaListener(MapaTesoroListener):
    def __init__(self):
        self.titulo = ""
        self.barcos = []
        self.coord_range = (99, 0)

    def enterTitulo(self, ctx):
        """Cuando llega a un nodo titulo, lo guarda en el atributo."""

        self.titulo = ctx.STRING().getText().strip('"')

    def enterPuntos(self, ctx):
        """Cuando llega a un nodo puntos, guarda el barco y su valor en puntos"""
        nombre = ctx.STRING().getText().strip('"')
        puntos = int(ctx.NUMBER().getText())

        for barco in self.barcos:
            if barco.nombre == nombre and not barco.puntos:
                barco.puntos = puntos
            else:
                new_barco = Barco(nombre, puntos=puntos)
                self.barcos.append(new_barco)

    def enterLocalizacion(self, ctx):
        """Cuando llega a un nodo localizacion:
        - Si hay un barco con ese nombre, sin coordenadas, se las asigna
        - Si no hay o tiene coordenadas, se crea un nuevo barco
        """
        nombre = ctx.STRING().getText().strip('"')
        coordenadas_str = ctx.STRING().getText().strip('"')
        coordenadas = list(map(int, coordenadas_str.split(",")))

        for barco in self.barcos:
            if barco.nombre == nombre:
                if barco.full():
                    new_barco = Barco(nombre, coordenadas, barco.puntos)
                    self.barcos.append(new_barco)
                else:
                    barco.coordenadas = coordenadas
            return

    def enterCoordenadas(self, ctx):
        coordenadas = tuple(map(int, ctx.NUMBER()))
        self.coord_range = (
            min(min(coordenadas), self.coord_range[0]),
            max(max(coordenadas), self.coord_range[1]),
        )


class Mapa:
    def __init__(self, filename, min_size=0):
        self.min_size = min_size
        self.barcos = self.parse_map(filename)

    def __getitem__(self, key):
        return self.mapa[key]

    def __contains__(self, key):
        return key in self.mapa

    def __str__(self):
        res = ""
        for row in self.mapa:
            for elem in row:
                res += elem
        return res

    def parse_map(self, filename):
        text = open(filename).read()
        lexer = MapaTesoroLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = MapaTesoroParser(stream)
        tree = parser.mapa()

        listener = MapaListener()
        walker = tree.depthfirst(listener)
        walker.walk()

        return listener.titulo, listener.barcos


def main():
    _ = Mapa("../ejemplo.field")


if __name__ == "__main__":
    main()
