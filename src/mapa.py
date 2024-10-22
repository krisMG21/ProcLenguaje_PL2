from antlr4 import InputStream, CommonTokenStream
from MapaTesoroParser import MapaTesoroParser
from MapaTesoroLexer import MapaTesoroLexer
from MapaTesoroListener import MapaTesoroListener

class Barco:
    '''
    Objeto que representa un barco, con su nombre, coordenadas y puntos.
    '''

    def __init__(self, nombre, coordenadas = None, puntos = None):
        '''
        nomber: str
        coordenadas: (int, int)
        puntos: int
        '''
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

    def enterTitulo(self, ctx):
        assert not self.titulo, "Titulo ya definido"
        self.titulo = ctx.STRING().getText().strip('"')

    def enterPuntos(self, ctx):
        nombre = ctx.STRING().getText().strip('"')
        puntos = int(ctx.NUMBER().getText())

        for barco in self.barcos:
            if barco.nombre == nombre and not barco.puntos:
                barco.puntos = puntos

    def enterLocalizacion(self, ctx):
        nombre = ctx.STRING().getText().strip('"')
        coordenadas_str = ctx.STRING().getText().strip('"')
        coordenadas = tuple(map(int, coordenadas_str.split(",")))

        for barco in self.barcos:
            if barco.nombre == nombre and not barco.full():
                barco.coordenadas = coordenadas
            else :
                new_barco = Barco(nombre, coordenadas)
                new_barco.puntos = barco.puntos
                self.barcos.append(new_barco)


class Mapa:
    def __init__(self, filename, min_size=0):
        self.mapa = {}
        self.min_size = min_size

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
        lexer = MapaPruebasLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = MapaPruebasParser(stream)
        tree = parser.mapa()

        listener = 

        return tree


def main():
    _ = Mapa("../ejemplo.field")


if __name__ == "__main__":
    main()
