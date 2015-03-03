import pandas as pd
from collections import OrderedDict

df = pd.read_csv('formulario.csv')

counts = {c: sum(df[c] == 'Principiante') for c in df.columns}

l = counts.items()

s = sorted(l, key=lambda x: x[1])
