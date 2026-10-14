import pandas as pd

from pathlib import Path

import pandas as pd

archivo = Path(__file__).with_name("Prueba.xlsx")
df = pd.read_excel(archivo)

print(df.head())
from sklearn.tree import DecisionTreeClassifier
x = [[10000], [20000], [30000], [40000], [50000]]
y = [0, 0, 1, 1, 1]
modelo = DecisionTreeClassifier()
modelo.fit(x, y)
predictions = modelo.predict([[80000]])
if predictions[0] == 1:
    print("el cliente puede comprar")

else:
    print("el cliente no puede comprar")