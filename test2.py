tokens  = []

#line = "restaurante='Restaurante LFP' 'Bebidas'  : [bebida_1;'Bebida #1';11.;'Descripción Bebida 1'    ] [ bebida_2;'Bebida #2';10.50;    'Descripción Bebida 2'] Cafe'"
#line = "restaurante='Restaurante LFP'"
#line = "1241"

line = "rest@restaurante='Restaurante LFP' 'Bebid21as'  : [bebidñda-_-1;'Bebida #1';1-&1.;'Descripci12ón Bebida 1'    ] [ be1♣bida_2;'Bebida #2';&1&0&.&5&0&;    'Descripción Bebida 2'] 'Desayuno♠s': [d1;'Desayuno 1';45.00;'DescripciUón Desayuno 1'] [d2 ;'Desayuno 2';    40.   ;'Descripción Desayuno 2'] [d3;'Desayuno 3';35;'Descripción Desayuno 3'] '  Postres': [   pos_001;'Postre 1'   ;25;'Descripción Postre 1'] "


def afd(line):
    cnt = 0
    err_cnt = 1
    state = 0
    token = [[]]
    error = []
    section_name = ""
    res_name = ""
    products = ""
    cache = ""
    for i in line:
        charCode = int(ord(i))
        #print(i,charCode)
        if(state == 0): #get restaurant name
            if(charCode == 32):
                continue
            elif(charCode == 39 and cache == "restaurante="):
                cache = ""
                state = 1
            elif(charCode >= 97 and charCode <= 122 or charCode == 61):
                cache += str(i)
            else:
                if(cache == "restaurante"):
                    error.append([err_cnt, cnt, i, "Caracter Invalido"])
                    err_cnt += 1
                else:
                    error.append([err_cnt, cnt, cache+i, "Caracter Invalido"])
                    err_cnt += 1
                    cache = ""
                    
            #print("p0")
        elif(state == 1): # strings
            if(charCode == 39):
                #print ("state -> 2")
                state = 2
            else:
                cache += str(i)
            #print("p1")
        elif(state == 2): #check delimiters
            if(charCode == 32):
                continue
            elif(charCode == 39):
                res_name += cache
                cache = ""
                state = 1
            elif(charCode == 58):
                section_name += cache
                token[cnt].append(cache)
                token.append([])
                cnt += 1
                cache = ""
                state = 3
                #print("stage -> 3")
            elif(charCode == 91):
                state = 3
                cache = ""
            elif(charCode == 93):
                products += cache
                token[cnt].append(cache)
                token.append([])
                cnt += 1
                cache = ""
                state = 3
            elif(i == ';'):
                products += cache
                token[cnt].append(cache)
                cache = ""
                state = 3
            #print("p2")
        elif(state == 3): #inside section
            if(charCode == 32):
                continue
            if(charCode == 39):
                state = 1
            elif(charCode == 59):
                products += cache
                token[cnt].append(cache)
                cache = ""
            elif(charCode == 91):
                continue
            elif(charCode >= 48 and charCode <= 57):
                if(cache == ""):
                    cache += str(i)
                    state = 5
                else:
                    cache += str(i)
            elif(charCode == 46):
                cache += str(i)
                state = 4
            elif(charCode >= 97 and charCode <= 122 or charCode == 95):
                cache += str(i)
            else:
                error.append([err_cnt, cnt, i, "Identificador Invalido"])
                err_cnt += 1
            #print("p3")
        elif(state == 4): #Check Decimals
            if(charCode >= 48 and charCode <= 57):
                cache += str(i)
            elif(charCode == 59):
                token[cnt].append(cache)
                cache = ""
                state = 3
            else:
                error.append([err_cnt, cnt, i, "Caracter Invalido"])
                err_cnt += 1
        elif(state == 5):
            if(charCode >= 48 and charCode <= 57):
                cache += str(i)
            elif(charCode == 46):
                cache += str(i)
                state = 4
            elif(charCode == 59):
                token[cnt].append(cache)
                cache = ""
                state = 3
            else:
                error.append([err_cnt, cnt, i, "Caracter Invalido"])
                err_cnt += 1


    token.pop()
    print(res_name)
    for i in token:
        try:
            i[2] = "%.2f" % float(i[2])
            print(i[0] + " " + i[1] + " " + i[2] + " " + i[3])
        except:
            print("\nSection: " + i[0] + "\n")

    print()
    for i in error:
        print(i)
afd(line)
