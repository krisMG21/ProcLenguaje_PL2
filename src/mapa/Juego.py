import tkinter as tk
from tkinter import messagebox
from Nivel import Nivel  # Importa tus clases correctamente
from Jugador import Jugador
from Barco import Barco
from Obstaculo import Obstaculo


class Juego:
    def __init__(self, niveles_files):
        self.ventana = tk.Tk()
        self.ventana.title("Juego")

        # Inicialización de niveles
        self.niveles_files = niveles_files
        self.nivel_actual = 0
        self.aciertos = 0
        self.jugador = Jugador(vida=100, puntos=0)
        self.cargar_nivel()

        # Configuración de UI
        self.crear_ui()

    def cargar_nivel(self):
        """Carga el nivel actual basado en el archivo de configuración con codificación UTF-8"""

        try:
            with open(
                self.niveles_files[self.nivel_actual], "r", encoding="utf-8"
            ) as file:
                text = file.read()
            self.nivel = Nivel(text)
        except IndexError:
            messagebox.showinfo("Juego terminado", "¡Has completado todos los niveles!")
            self.ventana.destroy()

    def crear_ui(self):
        # Crear tablero
        self.tablero_frame = tk.Frame(self.ventana)
        self.tablero_frame.pack()
        self.crear_tablero()

        # Barra de vida
        self.barra_vida_canvas = tk.Canvas(
            self.ventana, width=200, height=20, bg="grey"
        )
        self.barra_vida_canvas.pack(pady=10)
        self.actualizar_barra_vida()

        # Marcador de puntos
        self.marcador_puntos = tk.Label(
            self.ventana, text=f"Puntos: {self.jugador.puntos}", font=("Arial", 12)
        )
        self.marcador_puntos.pack()

    def crear_tablero(self):
        """Genera el tablero de botones según el tamaño del mapa"""
        for widget in self.tablero_frame.winfo_children():
            widget.destroy()

        self.botones = []
        for i in range(self.nivel.size[1]):
            fila = []
            for j in range(self.nivel.size[0]):
                boton = tk.Button(
                    self.tablero_frame,
                    text=" ",
                    width=4,
                    height=2,
                    command=lambda x=i, y=j: self.revisar_casilla(x, y),
                    font=("Arial", 30),
                )
                boton.grid(row=i, column=j)
                fila.append(boton)
            self.botones.append(fila)

    def revisar_casilla(self, x, y):
        """Maneja la lógica de un clic en una casilla (x, y)"""
        contenido = self.nivel.try_coord(x, y)
        if isinstance(contenido, Barco):
            # Barco (tesoro) encontrado
            self.aciertos += 1
            self.jugador.add_puntos(contenido.puntos)
            self.botones[x][y].config(text="💰", bg="yellow", state="disabled")
            messagebox.showinfo(
                "Tesoro encontrado",
                f"¡Encontraste {contenido.nombre} de {contenido.puntos} puntos!",
            )
            self.marcador_puntos.config(text=f"Puntos: {self.jugador.puntos}")
        elif isinstance(contenido, Obstaculo):
            # Obstáculo encontrado
            self.jugador.dañar(contenido.daño)
            self.botones[x][y].config(text="💣", bg="red", state="disabled")
            messagebox.showwarning(
                "Obstáculo",
                f"Encontraste una {contenido.nombre} que te quita {contenido.daño} puntos de vida.",
            )
            self.actualizar_barra_vida()
        else:
            messagebox.showinfo("Nada aquí", "No hay nada en esta casilla.")
            self.botones[x][y].config(text="X", state="disabled")

        # Verificar si el nivel está completado
        if self.aciertos >= self.nivel.numero_barcos:
            messagebox.showinfo(
                "Nivel completado", "¡Has encontrado todos los tesoros de este nivel!"
            )
            self.siguiente_nivel()

        # Verificar si el jugador sigue vivo
        if self.jugador.vida <= 0:
            messagebox.showinfo(
                "Juego terminado", "Has perdido toda tu vida. ¡Juego terminado!"
            )
            self.ventana.destroy()

    def actualizar_barra_vida(self):
        """Actualiza la barra de vida en función de la vida actual del jugador"""
        self.barra_vida_canvas.delete("vida")
        vida_actual = max(0, (self.jugador.vida / 100) * 200)
        self.barra_vida_canvas.create_rectangle(
            0, 0, vida_actual, 20, fill="green", tags="vida"
        )
        self.barra_vida_canvas.update()

    def siguiente_nivel(self):
        """Avanza al siguiente nivel si existe, o termina el juego"""
        self.nivel_actual += 1
        self.aciertos = 0
        self.cargar_nivel()
        self.crear_tablero()
        self.actualizar_barra_vida()

    def iniciar(self):
        self.ventana.mainloop()


# Archivos de nivel que deberás tener preparados
niveles_files = ["Nivel1.txt", "Nivel2.txt", "Nivel3.txt"]

juego = Juego(niveles_files)
juego.iniciar()
