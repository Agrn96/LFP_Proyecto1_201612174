from Cargar_Orden import cargar_Orden
from Cargar_Menu import cargar_Menu
from Menu import menu
import tkinter as tk
from Class_Menu import Menu
from Class_Orden import Orden

menu_ = Menu()
orden_ = Orden()
def main(menu_, orden_): 
    """Mientras x != 6, el menu sigue apareciendo
    """     
    x = 0
    while(x != 6):
        print("")
        print("Menu Principal")
        print("1. Cargar Menu")
        print("2. Cargar Orden")
        print("3. Generar Menu")
        print("4. Generar Factura")
        print("5. Generar Arbol")
        print("6. Salir")
        print("Choose Menu Option: ", end="\t")
        #try:
        x = int(input())                                #opcion del Menu
        menu_, orden_ = menu(menu_, orden_, x)          #Llamada al Menu utilizando el input del usuario
        #except:
        #   print("ERROR: Opcion Invalido")

main(menu_, orden_)