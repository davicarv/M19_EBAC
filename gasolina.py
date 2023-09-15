import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_plot = sns.lineplot(x=gasolina_df.dia,y=gasolina_df.venda)
plt.savefig("gasolina_plot.png")