#Ejemplo diagramas de Venn
#Autor: Javier Arturo Hernández Sosa
#Fecha: 3/Sep/2017
#Descripcion: Curso Python FES Acatlán

import matplotlib_venn
import matplotlib.pyplot as plt

animales = {'perro', 'vaca', 'raton', 'conejo', 'aguila', 'vaca', 'conejo'}
animales2 = {'conejo', 'burro', 'ballena', 'gato', 'perico', 'perro', 'gato', 'ballena'}
plt.figure(figsize=(6,8))
v = matplotlib_venn.venn2(subsets=[animales,animales2],set_labels=('Animales','animales2'))
v.get_label_by_id('10').set_text(animales - animales2)
v.get_label_by_id('11').set_text(animales.intersection(animales2))
v.get_label_by_id('01').set_text(animales2 - animales)
c = matplotlib_venn.venn2_circles(subsets=[animales, animales2], linestyle="dashed")
c[0].set_ls('solid')
plt.show()