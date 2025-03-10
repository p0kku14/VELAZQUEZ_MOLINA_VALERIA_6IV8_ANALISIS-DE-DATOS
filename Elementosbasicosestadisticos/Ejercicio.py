import pandas as pd
import matplotlib.pyplot as plt
import numpy as pd

df = pd.read_csv('Elementosbasicosestadisticos/housing.csv')
df = pd.DataFrame([df.min() , df.max() , df.mean() , df.std()])

