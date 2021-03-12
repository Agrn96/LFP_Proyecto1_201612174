from os import O_APPEND
from tkinter import *
from tkinter import filedialog
import codecs


def cargar_Orden():
    """Funcion para abrir el archivo que se utiliza para la programa

    Args:
        lista (class): Listas para guardar informacion del archivo
    """
    token = [""]
    temp = ""
    with codecs.open(filedialog.askopenfilename(filetypes=[("Text files","*.lfp")]), encoding='utf-8') as filename:
        afd(filename)
    filename.close()


def afd(file):
    cnt = 0
    err_cnt = 1
    client = []
    order = [[]]
    error = []
    

    i = 0
    for line in file:
        state = 0
        cache = ""
        j=0
        for char in line:
            charCode = ord(char)
            if(i == 0): # informacion del cliente
                if(state == 0):
                    if(charCode == 32):
                        continue
                    elif(charCode == 39):
                        state = 1
                    elif(charCode >= 48 and charCode <= 57):
                        cache += str(char)
                        state = 2
                elif(state == 1): # String Collector
                    if(charCode == 39):
                        client.append(cache)
                        cache = ""
                        state = 0
                    else:
                        cache += str(char)
                elif(state == 2): # tip collector
                    if(charCode == 37):
                        client.append(cache)
                        cache = ""
                    elif((charCode >= 48 and charCode <= 57) or charCode == 46):
                        cache += str(char)
                    else:
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
                        err_cnt += 1
            else: # ordenes
                if(state == 0): #cantidad
                    if(charCode >= 48 and charCode <= 57):
                        cache += str(char)
                    elif(charCode == 44):
                        order[cnt].append(cache)
                        cache = ""
                        state = 1
                    else:
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
                elif(state == 1): #id
                    if((charCode >= 97 and charCode <= 122) or charCode == 95 or (charCode >= 48 and charCode <= 57)):
                        cache += str(char)
                    else:
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
                    if(j == (len(line) - 1)):
                        order[cnt].append(cache)
                        order.append([])
                        cache = ""
                        cnt += 1
                    
            j+=1
        i+=1
    order.pop()
    print(cache)
    for i in client:
        print(i)

    for i in order:
        print(i)
