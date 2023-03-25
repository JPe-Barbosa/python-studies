
import matplotlib.pyplot as plt
import numpy as np

labels=valores["type"][:5]
values=valores["%"][:5]
plt.figure(figsize=(5,3),dpi=100)
bars=plt.bar(labels,values)

plt.title("Porcentagem dos tipos de produtos") #Título do gráfico
plt.xlabel("Tipos") #Título do eixo X
plt.ylabel("Porcentagem") #Título do eixo Y
bars[0].set_hatch("/")
bars[1].set_hatch("O")
plt.xticks(rotation = 90)
plt.show()