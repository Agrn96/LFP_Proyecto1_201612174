import webbrowser

class Menu():
    def __init__(self):
        self.token = None
        self.res_name = None
        self.error = None

    def update(self, res_name, token, error, tokens):
        for i in token:
            try:
                temp = i[2]
                i[2] = "%.2f" % float(i[2])
                if(str(i[2]) != str(temp)):
                    print(i[2], temp)
                    error.append(["n","x","y",temp,"Numero Invalido"])
                
            except:
                continue
        self.token = token
        self.res_name = res_name
        self.error = error
        self.tokens = tokens
    
    def generar_HTML(self):
        name = "Error_Menu"
        with open(name + ".html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<body>\n")
            f.write("\n<div><H1 style=\"align=center\">Tokens en el Menu</H1></div>")

            # tokens.append([tokens_cnt, i, j, cache,"Float"])
            f.write("<div><table>")
            f.write("<thead><th>No.</th><th>Lexema</th><th>Fila</th><th>Columna</th><th>Token</th></thead><tbody>")
            for temp in self.tokens:          
                f.write("<tr><td>" + str(temp[0]) + "</td><td>" + str(temp[3]) + "</td><td>" + str(temp[1]) + "</td><td>" + str(temp[2]) + "</td><td>" + str(temp[4]) + "</td></tr>")    
            f.write("</tbody></table></div>")

            f.write("\n<div><H1 style=\"align=center\">Errores en el Menu</H1></div>")
            # error.append([err_cnt, i, j, char, "Caracter Invalido"])
            f.write("<div><table>")
            f.write("<thead><th>No.</th><th>Lexema</th><th>Fila</th><th>Columna</th><th>Token</th></thead><tbody>")
            for temp in self.error:          
                f.write("<tr><td>" + str(temp[0]) + "</td><td>" + str(temp[3]) + "</td><td>" + str(temp[1]) + "</td><td>" + str(temp[2]) + "</td><td>" + str(temp[4]) + "</td></tr>")    
            f.write("</tbody></table></div>")

            f.write("\n</body>\n</html>")
            webbrowser.open("Error_Menu.html")