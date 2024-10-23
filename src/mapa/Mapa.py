from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.ParserRuleContext import ParseTree
from MapaTesoroParser import MapaTesoroParser
from MapaTesoroLexer import MapaTesoroLexer
from MapaListener import MapaListener
from TreePrinter import TreePrinter


class Mapa:
    def __init__(self, text: str, min_size: int = 0):
        self.min_size = min_size
        self.titulo, self.barcos, self.size, self.tree = self.parse_map(text)

        max_x, max_y = (
            max(self.size[0], min_size),
            max(self.size[1], min_size),
        )

        self.mapa = [[None for _ in range(max_x)] for _ in range(max_y)]

        for barco in self.barcos:
            self.mapa[barco.coordenadas[0] - 1][barco.coordenadas[1] - 1] = barco

    def __getitem__(self, key: int):
        return self.mapa[key]

    def __contains__(self, key: int):
        return key in self.mapa

    def get_barcos(self):
        return self.barcos

    def as_map(self):
        res = ""
        for row in self.mapa:
            for elem in row:
                res += " "
                res += "[ ]" if elem is None else "[█]"
            res += "\n"
        return res

    def as_tree(self):
        printer = TreePrinter()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

    def parse_map(self, text: str):
        lexer: MapaTesoroLexer = MapaTesoroLexer(InputStream(text))
        tokens: CommonTokenStream = CommonTokenStream(lexer)
        parser: MapaTesoroParser = MapaTesoroParser(tokens)
        tree: ParseTree = parser.mapa()

        print(tree.toStringTree(recog=parser))

        listener: MapaListener = MapaListener()
        walker: ParseTreeWalker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.titulo, listener.barcos, listener.size, tree
