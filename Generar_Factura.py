import webbrowser
from datetime import date
def generar_Factura(menu_, orden_):
    txt = ["Nombre", "NIT", "Direccion"]
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    name = "Factura"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body>\n")
        f.write("\n<div><H1 style=\"align=center\">"+menu_.res_name+"</H1></div>\n<div>Factura No. XX\n<br>Fecha: " + d1 + "</div>")

        i = 0
        f.write("<br><div>Datos del Cliente:")
        for temp in orden_.client:
            if(i==3):
                break
            f.write("<br>" + txt[i] + ": " + temp + "\n")
            i += 1
        
        f.write("\n</div><br><div>Descripcion:")
        f.write("<table><thead>")
        f.write("\n<tr><th>Cantidad</th>\n<th>Concepto</th>\n<th>Precio</th>\n<th>Total</th>\n</tr></thead>")

        total = 0
        f.write("<tbody>")
        for temp in orden_.order:
            f.write("<tr>")
            for temp_ in menu_.token:
                try:
                    if(str(temp[1]) == str(temp_[0])):
                        amount = float(temp_[2]) * float(temp[0])
                        total += amount
                        f.write("\n<td style=\"text-align: center; vertical-align: middle\">" + temp[0] + "</td><td>" + temp_[1] + "</td><td>Q" + temp_[2] + "</td><td>Q" + str("%.2f" % amount) + "</td>")
                        break
                    else:
                        continue
                except:
                    continue
            f.write("</tr>")
        
        f.write("\n<tr> <th>SubTotal</th><td></td><td></td><td>Q" + str("%.2f" % total) + "</td></tr>")

        propina = float(orden_.client[3]) / float("100")
        propina_ = "%.2f" % (total * propina)
        f.write("\n<tr><th>Propina (%" + str(orden_.client[3]) + ")" + "</th><td></td><td></td><td>Q" + str(propina_) + "</td></tr>")

        total = total + float(propina_)
        f.write("\n<tr><th>Total</th><td></td><td></td><td><b>Q" + str(total) + "</b></td></tr>") # Propina
        f.write("</tbody></table></div>")
        f.write("\n</body>\n</html>")
        webbrowser.open("Factura.html")