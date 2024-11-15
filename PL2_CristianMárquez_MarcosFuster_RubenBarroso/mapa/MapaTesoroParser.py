# Generated from MapaTesoro.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,3,0,27,8,0,1,1,
        1,1,1,1,1,1,3,1,33,8,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,5,1,42,
        8,1,10,1,12,1,45,9,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,
        88,0,26,1,0,0,0,2,28,1,0,0,0,4,52,1,0,0,0,6,57,1,0,0,0,8,60,1,0,
        0,0,10,67,1,0,0,0,12,73,1,0,0,0,14,79,1,0,0,0,16,84,1,0,0,0,18,88,
        1,0,0,0,20,21,3,2,1,0,21,22,3,4,2,0,22,27,1,0,0,0,23,24,3,4,2,0,
        24,25,3,2,1,0,25,27,1,0,0,0,26,20,1,0,0,0,26,23,1,0,0,0,27,1,1,0,
        0,0,28,29,5,1,0,0,29,30,5,16,0,0,30,32,3,6,3,0,31,33,3,8,4,0,32,
        31,1,0,0,0,32,33,1,0,0,0,33,37,1,0,0,0,34,36,3,10,5,0,35,34,1,0,
        0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,43,1,0,0,0,39,37,
        1,0,0,0,40,42,3,12,6,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,
        43,44,1,0,0,0,44,49,1,0,0,0,45,43,1,0,0,0,46,48,3,14,7,0,47,46,1,
        0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,0,0,0,51,
        49,1,0,0,0,52,53,5,2,0,0,53,54,5,16,0,0,54,55,3,18,9,0,55,56,5,16,
        0,0,56,5,1,0,0,0,57,58,5,14,0,0,58,59,5,16,0,0,59,7,1,0,0,0,60,61,
        5,3,0,0,61,62,5,15,0,0,62,63,5,4,0,0,63,64,5,15,0,0,64,65,5,5,0,
        0,65,66,5,16,0,0,66,9,1,0,0,0,67,68,5,14,0,0,68,69,5,6,0,0,69,70,
        5,15,0,0,70,71,5,7,0,0,71,72,5,16,0,0,72,11,1,0,0,0,73,74,5,14,0,
        0,74,75,5,8,0,0,75,76,5,15,0,0,76,77,5,9,0,0,77,78,5,16,0,0,78,13,
        1,0,0,0,79,80,5,14,0,0,80,81,5,10,0,0,81,82,3,16,8,0,82,83,5,16,
        0,0,83,15,1,0,0,0,84,85,5,15,0,0,85,86,5,11,0,0,86,87,5,15,0,0,87,
        17,1,0,0,0,88,89,5,12,0,0,89,90,5,18,0,0,90,91,5,13,0,0,91,92,5,
        16,0,0,92,19,1,0,0,0,5,26,32,37,43,49
    ]

class MapaTesoroParser ( Parser ):

    grammarFileName = "MapaTesoro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Mapa:'", "'Jugador:'", "'El mapa tiene'", 
                     "'filas y'", "'columnas'", "'te da'", "'puntos'", "'hace '", 
                     "'puntos de da\\u00F1o'", "'est\\u00E1 enterrado en'", 
                     "','", "'Tiene '", "' puntos de vida'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "NEWLINE", 
                      "WS", "INT" ]

    RULE_nivel = 0
    RULE_mapa = 1
    RULE_jugador = 2
    RULE_titulo = 3
    RULE_tamaño = 4
    RULE_puntos = 5
    RULE_daño = 6
    RULE_localizacion = 7
    RULE_coordenada = 8
    RULE_vida = 9

    ruleNames =  [ "nivel", "mapa", "jugador", "titulo", "tamaño", "puntos", 
                   "daño", "localizacion", "coordenada", "vida" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    STRING=14
    NUMBER=15
    NEWLINE=16
    WS=17
    INT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NivelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapa(self):
            return self.getTypedRuleContext(MapaTesoroParser.MapaContext,0)


        def jugador(self):
            return self.getTypedRuleContext(MapaTesoroParser.JugadorContext,0)


        def getRuleIndex(self):
            return MapaTesoroParser.RULE_nivel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNivel" ):
                listener.enterNivel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNivel" ):
                listener.exitNivel(self)




    def nivel(self):

        localctx = MapaTesoroParser.NivelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nivel)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.mapa()
                self.state = 21
                self.jugador()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.jugador()
                self.state = 24
                self.mapa()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def titulo(self):
            return self.getTypedRuleContext(MapaTesoroParser.TituloContext,0)


        def tamaño(self):
            return self.getTypedRuleContext(MapaTesoroParser.TamañoContext,0)


        def puntos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapaTesoroParser.PuntosContext)
            else:
                return self.getTypedRuleContext(MapaTesoroParser.PuntosContext,i)


        def daño(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapaTesoroParser.DañoContext)
            else:
                return self.getTypedRuleContext(MapaTesoroParser.DañoContext,i)


        def localizacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapaTesoroParser.LocalizacionContext)
            else:
                return self.getTypedRuleContext(MapaTesoroParser.LocalizacionContext,i)


        def getRuleIndex(self):
            return MapaTesoroParser.RULE_mapa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapa" ):
                listener.enterMapa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapa" ):
                listener.exitMapa(self)




    def mapa(self):

        localctx = MapaTesoroParser.MapaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mapa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MapaTesoroParser.T__0)
            self.state = 29
            self.match(MapaTesoroParser.NEWLINE)
            self.state = 30
            self.titulo()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 31
                self.tamaño()


            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.puntos() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.daño() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 46
                self.localizacion()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JugadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MapaTesoroParser.NEWLINE)
            else:
                return self.getToken(MapaTesoroParser.NEWLINE, i)

        def vida(self):
            return self.getTypedRuleContext(MapaTesoroParser.VidaContext,0)


        def getRuleIndex(self):
            return MapaTesoroParser.RULE_jugador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJugador" ):
                listener.enterJugador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJugador" ):
                listener.exitJugador(self)




    def jugador(self):

        localctx = MapaTesoroParser.JugadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_jugador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MapaTesoroParser.T__1)
            self.state = 53
            self.match(MapaTesoroParser.NEWLINE)
            self.state = 54
            self.vida()
            self.state = 55
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TituloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MapaTesoroParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_titulo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitulo" ):
                listener.enterTitulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitulo" ):
                listener.exitTitulo(self)




    def titulo(self):

        localctx = MapaTesoroParser.TituloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_titulo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MapaTesoroParser.STRING)
            self.state = 58
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TamañoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MapaTesoroParser.NUMBER)
            else:
                return self.getToken(MapaTesoroParser.NUMBER, i)

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_tamaño

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTamaño" ):
                listener.enterTamaño(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTamaño" ):
                listener.exitTamaño(self)




    def tamaño(self):

        localctx = MapaTesoroParser.TamañoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tamaño)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MapaTesoroParser.T__2)
            self.state = 61
            self.match(MapaTesoroParser.NUMBER)
            self.state = 62
            self.match(MapaTesoroParser.T__3)
            self.state = 63
            self.match(MapaTesoroParser.NUMBER)
            self.state = 64
            self.match(MapaTesoroParser.T__4)
            self.state = 65
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PuntosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MapaTesoroParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(MapaTesoroParser.NUMBER, 0)

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_puntos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPuntos" ):
                listener.enterPuntos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPuntos" ):
                listener.exitPuntos(self)




    def puntos(self):

        localctx = MapaTesoroParser.PuntosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_puntos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MapaTesoroParser.STRING)
            self.state = 68
            self.match(MapaTesoroParser.T__5)
            self.state = 69
            self.match(MapaTesoroParser.NUMBER)
            self.state = 70
            self.match(MapaTesoroParser.T__6)
            self.state = 71
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DañoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MapaTesoroParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(MapaTesoroParser.NUMBER, 0)

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_daño

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDaño" ):
                listener.enterDaño(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDaño" ):
                listener.exitDaño(self)




    def daño(self):

        localctx = MapaTesoroParser.DañoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_daño)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MapaTesoroParser.STRING)
            self.state = 74
            self.match(MapaTesoroParser.T__7)
            self.state = 75
            self.match(MapaTesoroParser.NUMBER)
            self.state = 76
            self.match(MapaTesoroParser.T__8)
            self.state = 77
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MapaTesoroParser.STRING, 0)

        def coordenada(self):
            return self.getTypedRuleContext(MapaTesoroParser.CoordenadaContext,0)


        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_localizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalizacion" ):
                listener.enterLocalizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalizacion" ):
                listener.exitLocalizacion(self)




    def localizacion(self):

        localctx = MapaTesoroParser.LocalizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_localizacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MapaTesoroParser.STRING)
            self.state = 80
            self.match(MapaTesoroParser.T__9)
            self.state = 81
            self.coordenada()
            self.state = 82
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordenadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MapaTesoroParser.NUMBER)
            else:
                return self.getToken(MapaTesoroParser.NUMBER, i)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_coordenada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordenada" ):
                listener.enterCoordenada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordenada" ):
                listener.exitCoordenada(self)




    def coordenada(self):

        localctx = MapaTesoroParser.CoordenadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordenada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MapaTesoroParser.NUMBER)
            self.state = 85
            self.match(MapaTesoroParser.T__10)
            self.state = 86
            self.match(MapaTesoroParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapaTesoroParser.INT, 0)

        def NEWLINE(self):
            return self.getToken(MapaTesoroParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapaTesoroParser.RULE_vida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVida" ):
                listener.enterVida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVida" ):
                listener.exitVida(self)




    def vida(self):

        localctx = MapaTesoroParser.VidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MapaTesoroParser.T__11)
            self.state = 89
            self.match(MapaTesoroParser.INT)
            self.state = 90
            self.match(MapaTesoroParser.T__12)
            self.state = 91
            self.match(MapaTesoroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





