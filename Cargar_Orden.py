from os import O_APPEND
from tkinter import *
from tkinter import filedialog
import codecs
from Class_Orden import Orden


def cargar_Orden():
    """Funcion para abrir el archivo que se utiliza para la programa

    Args:
        lista (class): Listas para guardar informacion del archivo
    """
    orden_ = Orden()
    with codecs.open(filedialog.askopenfilename(filetypes=[("Text files","*.lfp")]), encoding='utf-8') as filename:
        client, order, error, tokens = afd(filename)
        orden_.update(client, order, error, tokens)
    filename.close()
    return orden_


def afd(file):
    cnt = 0
    err_cnt = 1
    tokens_cnt = 1
    client = []
    order = [[]]
    error = []
    tokens = []
    

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
                        tokens.append([tokens_cnt, i, j, char,"Delimiter"])
                        tokens_cnt += 1
                        state = 1
                    elif(charCode >= 48 and charCode <= 57):
                        cache += str(char)
                        state = 2
                    else:
                        if(char == "\n" or charCode == 44):
                            continue
                        error.append([err_cnt, i, j, char, "Caracter Invalido"])
                        err_cnt += 1
                elif(state == 1): # String Collector
                    if(charCode == 39):
                        tokens.append([tokens_cnt, i, j, cache,"String"])
                        client.append(cache)
                        cache = ""
                        state = 0
                    else:
                        cache += str(char)
                elif(state == 2): # tip collector
                    if(charCode==32):
                        j+=1
                        continue
                    elif(charCode == 37):
                        tokens.append([tokens_cnt, i, j, char,"Identificador"])
                        tokens_cnt += 1
                        tokens.append([tokens_cnt, i, j, cache,"String"])
                        tokens_cnt += 1
                        client.append(cache)
                        cache = ""
                    elif((charCode >= 48 and charCode <= 57) or charCode == 46):
                        cache += str(char)
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, i, j, char, "Caracter Invalido"])
                        err_cnt += 1
            else: # ordenes
                if(state == 0): #cantidad
                    if(charCode==32):
                        j+=1
                        continue
                    elif(charCode >= 48 and charCode <= 57):
                        cache += str(char)
                    elif(charCode == 44):
                        tokens.append([tokens_cnt, i, j, char,"Delimiter"])
                        tokens_cnt += 1
                        tokens.append([tokens_cnt, i, j, cache,"Numero"])
                        tokens_cnt += 1
                        order[cnt].append(cache)
                        cache = ""
                        state = 1
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, i, j, char, "Caracter Invalido"])
                        err_cnt += 1
                elif(state == 1): #id
                    if(charCode==32):
                        j+=1
                        continue
                    elif((charCode >= 97 and charCode <= 122) or charCode == 95 or (charCode >= 48 and charCode <= 57)):
                        cache += str(char)
                    elif(j == (len(line) - 2)):
                        tokens.append([tokens_cnt, i, j, cache,"Identificador"])
                        tokens_cnt += 1
                        order[cnt].append(cache)
                        order.append([])
                        cache = ""
                        cnt += 1
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, i, j, char, "Caracter Invalido"])
                        err_cnt += 1
                    
                    
            j+=1
        i+=1
    order.pop()
    return client, order, error, tokens
