import webbrowser

def generar_Menu(menu_,limite):
    name = "Menu"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body>\n")
        f.write("\n<div><H1 style=\"align=center\">"+menu_.res_name+"</H1></div>")

        f.write("<div><table><tbody>")
        for temp in menu_.token:
            try:
                if(float(temp[2]) <= float(limite)):
                    f.write("<tr><td><b>" + temp[1] + "</b></td><td><b>Q" + temp[2] + "</b></td></tr><tr><td colspan = \"2\"><small>" + temp[3] + "</small></td></tr>\n")
                else:
                    continue
            except:
                f.write("</div><div><thead colspan = \"2\"><th>" + temp[0] + ":</th></thead>\n")
        f.write("</tbody></table></div>")
        f.write("\n</body>\n</html>")
        webbrowser.open("Menu.html")