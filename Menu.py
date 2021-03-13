from Generar_Factura import generar_Factura
from Generar_Menu import generar_Menu
from Generar_Arbol import generar_Arbol
from Cargar_Orden import cargar_Orden
from Cargar_Menu import cargar_Menu
import tkinter as tk

def menu(menu_, orden_, x):
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        try:
            menu_ = cargar_Menu()
            menu_.generar_HTML()
        except:
            print("ERROR: Error con el archivo de Menu")
        return menu_, orden_
    elif(x == 2):
        try:
            orden_ = cargar_Orden()
            orden_.generar_HTML()
        except:
            print("ERROR: Error con el archivo de Orden")
        return menu_, orden_
    elif(x == 3):
        try:
            print("Ingresar limite de precio: ", end = "")
            limite = float(input())
            generar_Menu(menu_,limite)
        except:
            print("ERROR: Error con el ingreso de limite o El Menu esta vacio")
        return menu_, orden_
    elif(x == 4): # Menu Opcion 4: Mostrar datos del estudiante
        try:
            generar_Factura(menu_, orden_)
        except:
            print("ERROR: Menu/Orden esta vacio")
        return menu_, orden_
    elif(x == 5):
        try:
            generar_Arbol(menu_)
        except:
            print("ERROR: Menu esta vacio")
        return menu_, orden_
    elif(x == 6):
        print("Saliendo del applicacion")
        raise SystemExit(0)  # Se cierra la aplicacion
    else:
        print("Opcion Invalida")