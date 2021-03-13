from Generar_Factura import generar_Factura
from Generar_Menu import generar_Menu
from Generar_Arbol import generar_Arbol
from Cargar_Orden import cargar_Orden
from Cargar_Menu import cargar_Menu
import tkinter as tk

def menu(menu_, orden_, x):
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        menu_ = cargar_Menu()
        menu_.generar_HTML()
        return menu_, orden_
    elif(x == 2):
        orden_ = cargar_Orden()
        orden_.generar_HTML()
        return menu_, orden_
    elif(x == 3):
        print("Ingresar limite de precio: ", end = "")
        limite = int(input())
        generar_Menu(menu_,limite)
        return menu_, orden_
    elif(x == 4): # Menu Opcion 4: Mostrar datos del estudiante
        generar_Factura(menu_, orden_)
        return menu_, orden_
    elif(x == 5):
        generar_Arbol(menu_)
        return menu_, orden_
    elif(x == 6):
        print("Saliendo del applicacion")
        raise SystemExit(0)  # Se cierra la aplicacion
    else:
        print("Opcion Invalida")
        print("Placeholder")