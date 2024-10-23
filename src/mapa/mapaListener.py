from MapaTesoroListener import MapaTesoroListener
from barco import Barco


class MapaListener(MapaTesoroListener):
    def __init__(self):
        self.titulo = ""
        self.curr_barco = None
        self.barcos = []
        self.size = (0, 0)

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
                return

        self.barcos.append(Barco(nombre, puntos=puntos))

        for barco in self.barcos:
            print(barco)

    def enterLocalizacion(self, ctx):
        """Cuando llega a un nodo localizacion:
        - Si hay un barco con ese nombre, sin coordenadas, se las asigna
        - Si no hay o tiene coordenadas, se crea un nuevo barco
        """
        self.curr_barco = ctx.STRING().getText().strip('"')

    def enterCoordenada(self, ctx):
        coordenadas = [int(ctx.NUMBER(i).getText()) for i in range(2)]
        print(coordenadas)

        self.size = (
            max(min(coordenadas), self.size[0]),
            max(max(coordenadas), self.size[1]),
        )

        for barco in self.barcos:
            if barco.nombre == self.curr_barco:
                if barco.full():
                    new_barco = Barco(self.curr_barco, coordenadas, barco.puntos)
                    self.barcos.append(new_barco)
                    break
                else:
                    barco.coordenadas = coordenadas
        return
