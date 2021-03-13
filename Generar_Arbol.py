import os
os.environ["PATH"] = os.pathsep + 'D:/Program Files (x86)/Graphviz/bin'
from graphviz import Digraph

def generar_Arbol(menu_):
    dot = Digraph(comment='menu_ Circular, Matriz: ' + str(menu_.res_name))
    dot #doctestL +ELLIPSIS
    i = 0
    dot.node('A',menu_.res_name)
    section_id = ""
    for temp in menu_.token:
        try:
            name = 'B' + str(i)
            info = str(temp[1]) + " Q" + str(temp[2]) + " " + str(temp[3])
            dot.node(name, info)
            dot.edge(section_id,'B'+str(i))
        except:
            name = 'B' + str(i)
            section_id = name
            info = str(temp[0])
            dot.node(name, info)
            dot.edge('A','B'+str(i))
        i += 1
    dot.render('Grafica.dot', view=True)
