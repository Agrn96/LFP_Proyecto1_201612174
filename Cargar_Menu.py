from os import stat
from tkinter import *
from tkinter import filedialog
import codecs


def cargar_Menu():
    """Funcion para abrir el archivo que se utiliza para la programa

    Args:
        lista (class): Listas para guardar informacion del archivo
    """
    with codecs.open(filedialog.askopenfilename(filetypes=[("Text files","*.lfp")]), encoding='utf-8') as filename:
        token, error = afd(filename)
        for i in token:
            print(i)
        #    try:
        #        i[2] = "%.2f" % float(i[2])
        #        print(i[0] + " " + i[1] + " " + i[2] + " " + i[3])
        #    except:
        #        print("\nSection: " + i[0] + "\n")
        for i in error:
            print(i)
    filename.close()

def afd(file):
    cnt = 0
    err_cnt = 1
    token = [[]]
    error = []
    res_name = ""
    
    i = 0
    for line in file:
        state = 0
        cache = ""
        j = 0
        for char in line:
            charCode = ord(char)
            if(i == 0): #Restaurant Name
                if(state == 0):
                    if(charCode == 32):
                        j+=1
                        continue
                    elif(charCode >= 97 and charCode <= 122 or charCode == 61):
                        cache += str(char)
                    elif(charCode == 39):
                        cache = ""
                        state = 1
                    else:
                        if(cache == "restaurante="):
                            error.append([err_cnt, cnt, char, "Caracter Invalido"])
                            err_cnt += 1
                        elif(char == "\n"):
                            continue
                        else:
                            error.append([err_cnt, cnt, cache+char, "Caracter Invalido"])
                            cache == ""
                            err_cnt += 1
                elif(state==1):
                    if(charCode == 39):
                        res_name = cache
                        cache = ""
                        state = 0
                    else:
                        cache += str(char)
            else: # Sections
                if(state == 0): # Section or data checker
                    if(charCode == 39):
                        state = 1
                    elif(charCode == 91):
                        state = 2
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
                        err_cnt += 1
                elif(state == 1): # String Collector
                    if(charCode == 39):
                        token[cnt].append(cache)
                        cache = ""
                        state = 2
                    else:
                        cache += str(char)
                elif(state == 2): # Check Delimiter
                    if(charCode == 32):
                        j+=1
                        continue
                    elif(charCode == 39):
                        state = 1
                    elif((charCode >= 97 and charCode <= 122) or charCode == 95):
                        cache += str(char)
                    elif(charCode >= 48 and charCode <= 57):
                        if(cache == ""):
                            cache += str(char)
                            state = 3
                        else:
                            cache += str(char)
                    elif(charCode == 59):
                        if(cache == ""):
                            j+=1
                            continue
                        token[cnt].append(cache)
                        cache = ""
                    elif(charCode == 58):
                        token.append([])
                        cache = ""
                        cnt += 1
                    elif((charCode == 93) and (j >= (len(line)-2))):
                        token.append([])
                        cache = ""
                        cnt += 1
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
                elif(state == 3): # Number Collector
                    if(charCode >= 48 and charCode <= 57):
                        cache += str(char)
                    elif(charCode == 46 and ((char in cache) == False)):
                        cache += str(char)
                    elif(charCode == 59):
                        token[cnt].append(cache)
                        cache = ""
                        state = 2
                    else:
                        if(char == "\n"):
                            continue
                        error.append([err_cnt, cnt, char, "Caracter Invalido"])
            j+=1
        i += 1
    print(res_name) 
    return token, error
cargar_Menu()