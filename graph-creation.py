import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """Captura os valores da planilha excel e converte em uma matrix -- Retona um objeto do tipo np.array()"""
    data = pd.read_excel(filename)
    matrix = data.to_numpy(copy=True)
    return matrix

pd.set_option('display.max_rows', None)
data = load_data("megasena-results.xlsx")

v_dict = {}
k_values = []
v_values = []

for c in range(0, 60):
    f = np.count_nonzero(data == c) # Se quiser acessar uma coluna, substitua "data" por data[:, número da coluna]
    v_dict[c] = f

for k, v in v_dict.items():
    k_values.append(k) # x
    v_values.append(v) # y

plt.xlabel("Números das Casas")
plt.ylabel("Quantidade de repetições")
plt.title("Números X Frequência - Geral")

x_points = np.array(k_values)
y_points = np.array(v_values)

plt.plot(x_points, y_points)
plt.xticks(np.arange(min(x_points), max(y_points), 2))
plt.grid()
plt.show()






