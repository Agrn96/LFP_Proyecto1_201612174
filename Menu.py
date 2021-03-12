from Cargar_Menu import cargar_Menu
import tkinter as tk

def menu(x):
    window1 = tk.Tk()
    #window1.withdraw()
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        #ruta, lista, lista_red = cargar_Menu()
        #print("Opcion 1 terminado, ruta es: " + ruta);
        #return lista,lista_red
        #window1.deiconify()
        greeting = tk.Label(window1, text = "Test")
        greeting.pack()
        print("Placeholder 1")
    elif(x == 2):
        #procesar(temp_);
        #return lista,lista_red
        #window1.deiconify()
        greeting = tk.Label(window1, text = "Test1")
        greeting.pack()
        print("Placeholder 2")
    elif(x == 3):
        #try:
        #    salida_Archivo(temp_)
        #    print("Se escribio el archivo satisfactorio")
        #except:
        #    print("ERROR: error con la ruta")
        #return lista,lista_red
        greeting = tk.Label(window1, text = "Test2")
        greeting.pack()
        print("Placeholder 3")
    elif(x == 4): # Menu Opcion 4: Mostrar datos del estudiante
        #print("\nAlberto Gabriel Reyes Ning\n201612174\nIPC2-A\nIngenieria en Ciencias y Sistemas\n4to Semestre")
        #return lista,lista_red
        greeting = tk.Label(window1, text = "Test3")
        greeting.pack()
        print("Placeholder 4")
    elif(x == 5):
        # Imprimir opciones
        #ran = temp
        #i = 1
        #while(ran.next != None):
        #    print(str(i) + ": ", end="")
        #    print(ran.head.data)
        #    ran = ran.next
        #    i += 1
        #l = 0
        #while(l<1 or l>=i):
        #    print("\nChoose List: ", end="")
        #    try:
        #        l = int(input())
        #    except:
        #        print("ERROR: Opcion no es un numero")
        #    if(l<1 or l>=i):
        #        print("ERROR: Opcion Invalido")
        # Iterar al grafica selecionado
        #for i in range(1,l):
        #    temp = temp.next
        # Generar la grafica selecionado
        #generate(temp)
        #return lista,lista_red
        greeting = tk.Label(window1, text = "Test5")
        greeting.pack()
        print("Placeholder 5")
    elif(x == 6):
        #print("Saliendo del applicacion")
        #raise SystemExit(0)  # Se cierra la aplicacion
        print("Placeholder 6")
    else:
        print("Opcion Invalida")
        print("Placeholder")