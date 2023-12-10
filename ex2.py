import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')

plt.figure(figsize=(10,10))
plt.plot(df.index,df['Durata'],label='Durata',marker='x')
plt.plot(df.index,df['Puls'],label='Puls',marker='x')
plt.plot(df.index,df['MaxPuls'],label='MaxPuls',marker='x')
plt.plot(df.index,df['Calorii'],label='Calorii',marker='x')
plt.title('Toate valorile')
plt.legend()

plt.figure(figsize=(10,10))
plt.plot(df['Durata'][:10],marker='x',label='Durata')
plt.plot(df['Puls'][:10],marker='x',label='Puls')
plt.title('Primele 10 Valori')
plt.legend()

ult=df[['Durata','Puls']].tail(15)
plt.figure(figsize=(10,10))
plt.plot(ult['Durata'],marker='x',label='Durata')
plt.plot(ult['Puls'],marker='x',label='Puls')
plt.title('Ultimele 15 Valori')
plt.legend()

plt.tight_layout()
plt.show()
