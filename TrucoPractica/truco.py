import random
import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#crear la ventana

ventana = tk.Tk()
ventana.title("Juego de Truco - EET N° 33")
ventana.geometry("900x700")
ventana.resizable(False, False)
ventana.configure(bg="#1e5631")


def obtener_mazo_desde_db():
    """ Lee las cartas de truco.db una por una y las guarda en el mazo. """
    conexion = sqlite3.connect("truco.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, numero, palo, imagen, valor FROM naipes")
    filas = cursor.fetchall()
    conexion.close()

    mazo = []
    for fila in filas:
        id_carta = fila[0]
        numero = fila[1]
        palo = fila[2]
        imagen = fila[3]
        valor = fila[4]

        carta = {
            "id": id_carta,
            "numero": numero,
            "palo": palo,
            "imagen": imagen,
            "valor": valor
        }
        mazo.append(carta)

    return mazo

entero="julieta"

ventana.mainloop()