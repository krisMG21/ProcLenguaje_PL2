from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.ParserRuleContext import ParseTree
from MapaTesoroParser import MapaTesoroParser
from MapaTesoroLexer import MapaTesoroLexer
from MapaListener import MapaListener
from ToStrTreeListener import ToStrTreeListener
from Barco import Barco
from Obstaculo import Obstaculo


class Mapa:
    def __init__(self, text: str):
        self.titulo, self.barcos, self.obstaculos, self.size, self.tree = (
            self.parse_map(text)
        )

        self.mapa = [[None for _ in range(self.size[0])] for _ in range(self.size[1])]

        for barco in self.barcos:
            x, y = barco.coordenadas[0] - 1, barco.coordenadas[1] - 1
            assert self.mapa[x][y] is None

            self.mapa[x][y] = barco

        for obs in self.obstaculos:
            x, y = obs.coordenadas[0] - 1, obs.coordenadas[1] - 1
            assert self.mapa[x][y] is None

            self.mapa[x][y] = obs

    def __getitem__(self, key: int):
        return self.mapa[key]

    def __contains__(self, key: int):
        return key in self.mapa

    def get_barcos(self):
        return self.barcos

    def get_obstaculos(self):
        return self.obstaculos

    def try_coord(self, x: int, y: int):
        """Extrae el barco en la coordenada x,y, o None si no existe"""
        try:
            if self.mapa[x][y] is None:
                return None

            barco = self.mapa[x][y]
            self.mapa[x][y] = None
            return barco

        except IndexError:
            return None

    def as_map(self):
        """Devuelve una representación del mapa como casillas simples"""
        res = ""
        for row in self.mapa:
            for elem in row:
                res += " "
                res += (
                    "[█]"
                    if isinstance(elem, Barco)
                    else "[X]"
                    if isinstance(elem, Obstaculo)
                    else "[ ]"
                )
            res += "\n"
        return res

    def as_matrix(self):
        """Devuelve el contenido del mapa de forma ordenada en forma de cadena"""
        res = " "
        for row in self.mapa:
            for elem in row:
                res += str(elem) + ", "
            res = res[:-2] + "\n"
        return res

    def as_tree(self):
        """Recorre e imprime el mapa en forma de árbol detallado"""
        printer = ToStrTreeListener(MapaTesoroParser)
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        return printer.output

    def parse_map(self, text: str):
        """Procesa el archivo de entrada, y extrae los datos del mapa:
        - titulo
        - tamaño
        - barcos (puntos y coordenadas)
        - arbol de parseo
        """
        lexer: MapaTesoroLexer = MapaTesoroLexer(InputStream(text))
        tokens: CommonTokenStream = CommonTokenStream(lexer)
        parser: MapaTesoroParser = MapaTesoroParser(tokens)
        tree: ParseTree = parser.nivel()

        # print(tree.toStringTree(recog=parser))

        listener: MapaListener = MapaListener()
        walker: ParseTreeWalker = ParseTreeWalker()
        walker.walk(listener, tree)

        return (
            listener.titulo,
            listener.barcos,
            listener.obstaculos,
            listener.size,
            tree,
        )
