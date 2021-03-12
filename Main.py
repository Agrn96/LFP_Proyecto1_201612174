from Cargar_Orden import cargar_Orden
from Cargar_Menu import cargar_Menu
from tkinter.constants import CENTER
from Menu import menu
import tkinter as tk

def main(): 
    """Mientras x != 6, el menu sigue apareciendo
    """     
    window = tk.Tk()
    frame_Info = tk.Frame()
    frame_Menu = tk.Frame()

    title = tk.Label(master = frame_Info, text = "Proyecto 1 - LFP", width=50)
    title.pack()

    author = tk.Label(master = frame_Info, text = "Alberto Gabriel Reyes Ning, 201612174\nLFP A+\n",)
    author.pack()
        
    info_0 = tk.Label(master = frame_Menu, text = "Menu Principal")
    info_0.pack()

    button_0 = tk.Button(master = frame_Menu, text = "1. Cargar Menu",command=lambda: cargar_Menu(), width= 20, height=2, activebackground="#989898")
    button_0.pack()

    button_1 = tk.Button(master = frame_Menu, text = "2. Cargar_Orden",command=lambda: cargar_Orden(), width= 20, height=2, activebackground="#989898")
    button_1.pack()

    button_2 = tk.Button(master = frame_Menu, text = "3. Generar Menu",command=lambda: menu(3), width= 20, height=2, activebackground="#989898")
    button_2.pack()

    button_3 = tk.Button(master = frame_Menu, text = "4. Generar Factura",command=lambda: menu(4), width= 20, height=2, activebackground="#989898")
    button_3.pack()

    button_4 = tk.Button(master = frame_Menu, text = "5. Generar Arbol",command=lambda: menu(5), width= 20, height=2, activebackground="#989898")
    button_4.pack()

    button_5 = tk.Button(master = frame_Menu, text = "6. Salida",command= window.destroy, width= 20, height=2, activebackground="#989898")
    button_5.pack()

    frame_Info.pack()
    frame_Menu.pack()
    window.mainloop()
main()