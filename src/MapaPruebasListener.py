# Generated from MapaPruebas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapaPruebasParser import MapaPruebasParser
else:
    from MapaPruebasParser import MapaPruebasParser

# This class defines a complete listener for a parse tree produced by MapaPruebasParser.
class MapaPruebasListener(ParseTreeListener):

    # Enter a parse tree produced by MapaPruebasParser#mapa.
    def enterMapa(self, ctx:MapaPruebasParser.MapaContext):
        pass

    # Exit a parse tree produced by MapaPruebasParser#mapa.
    def exitMapa(self, ctx:MapaPruebasParser.MapaContext):
        pass


    # Enter a parse tree produced by MapaPruebasParser#titulo.
    def enterTitulo(self, ctx:MapaPruebasParser.TituloContext):
        pass

    # Exit a parse tree produced by MapaPruebasParser#titulo.
    def exitTitulo(self, ctx:MapaPruebasParser.TituloContext):
        pass


    # Enter a parse tree produced by MapaPruebasParser#puntos.
    def enterPuntos(self, ctx:MapaPruebasParser.PuntosContext):
        pass

    # Exit a parse tree produced by MapaPruebasParser#puntos.
    def exitPuntos(self, ctx:MapaPruebasParser.PuntosContext):
        pass


    # Enter a parse tree produced by MapaPruebasParser#localizacion.
    def enterLocalizacion(self, ctx:MapaPruebasParser.LocalizacionContext):
        pass

    # Exit a parse tree produced by MapaPruebasParser#localizacion.
    def exitLocalizacion(self, ctx:MapaPruebasParser.LocalizacionContext):
        pass


    # Enter a parse tree produced by MapaPruebasParser#coordenada.
    def enterCoordenada(self, ctx:MapaPruebasParser.CoordenadaContext):
        pass

    # Exit a parse tree produced by MapaPruebasParser#coordenada.
    def exitCoordenada(self, ctx:MapaPruebasParser.CoordenadaContext):
        pass



del MapaPruebasParser