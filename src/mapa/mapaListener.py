from MapaTesoroListener import MapaTesoroListener
from Barco import Barco
from Obstaculo import Obstaculo


class MapaListener(MapaTesoroListener):
    def __init__(self):
        self.titulo = ""
        self.curr_barco = None
        self.barcos = []
        self.obstaculo = []
        self.size = (0, 0)

    def enterTitulo(self, ctx):
        """Cuando llega a un nodo titulo, lo guarda en el atributo."""

        self.titulo = ctx.STRING().getText().strip('"')

    def enterTamaño(self, ctx):
        """Cuando llega a un nodo tamaño, se guarda el tamaño del mapa y se queda fijo."""

        self.size = (
            int(ctx.NUMBER(0).getText()),
            int(ctx.NUMBER(1).getText()),
        )

    def enterPuntos(self, ctx):
        """Cuando llega a un nodo puntos, guarda el barco y su valor en puntos"""
        nombre = ctx.STRING().getText().strip('"')
        puntos = int(ctx.NUMBER().getText())

        for barco in self.barcos:
            if barco.nombre == nombre and not barco.puntos:
                barco.puntos = puntos
                return

        self.barcos.append(Barco(nombre, puntos=puntos))

    def enterObstaculo(self, ctx):
        """Cuando llega a un obstáculo, crea y guarda el objeto"""
        nombre = ctx.STRING().getText().strip('"')
        daño = int(ctx.NUMBER().getText())

        self.obstaculo.append(Obstaculo(nombre, daño))

    def enterLocalizacion(self, ctx):
        """Cuando llega a un nodo localizacion:
        - Si hay un barco con ese nombre, sin coordenadas, se las asigna
        - Si no hay o tiene coordenadas, se crea un nuevo barco
        """
        self.elem_actual = ctx.STRING().getText().strip('"')

    def enterCoordenada(self, ctx):
        coordenadas = [int(ctx.NUMBER(i).getText()) for i in range(2)]

        # Si no se establece el tamaño, se ajusta al contenido
        self.size = (
            max(coordenadas[0], self.size[0]),
            max(coordenadas[1], self.size[1]),
        )

        # Si el barco ya existe, se actualiza
        # Si no existe, se crea
        for barco in self.barcos:
            if barco.nombre == self.elem_actual:
                if barco.full():
                    new_barco = Barco(self.elem_actual, coordenadas, barco.puntos)
                    self.barcos.append(new_barco)
                else:
                    barco.coordenadas = coordenadas
                break

        for obstaculo in self.obstaculo:
            if obstaculo.nombre == self.elem_actual:
                if obstaculo.full():
                    new_obstaculo = Obstaculo(
                        self.elem_actual, coordenadas, obstaculo.daño
                    )
                    self.obstaculo.append(new_obstaculo)
                else:
                    obstaculo.coordenadas = coordenadas
                break
        return
