import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from flask import Flask, send_file

app = Flask(__name__)

df = pd.read_csv('data.csv')

@app.route('/plot1')
def plot1():
    fig = plt.figure(figsize=(10,10))
    plt.plot(df.index,df['Durata'],label='Durata',marker='x')
    plt.plot(df.index,df['Puls'],label='Puls',marker='x')
    plt.plot(df.index,df['MaxPuls'],label='MaxPuls',marker='x')
    plt.plot(df.index,df['Calorii'],label='Calorii',marker='x')
    plt.title('Toate valorile')
    plt.legend()
    buf = BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    return send_file(buf,mimetype='image/png')

@app.route('/plot2')
def plot2():
    fig = plt.figure(figsize=(10,10))
    plt.plot(df['Durata'][:10],marker='x',label='Durata')
    plt.plot(df['Puls'][:10],marker='x',label='Puls')
    plt.title('Primele 10 Valori')
    plt.legend()
    buf = BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    return send_file(buf,mimetype='image/png')

@app.route('/plot3')
def plot3():
    ult = df[['Durata','Puls']].tail(15)
    fig = plt.figure(figsize=(10,10))
    plt.plot(ult['Durata'],marker='x',label='Durata')
    plt.plot(ult['Puls'],marker='x',label='Puls')
    plt.title('Ultimele 15 Valori')
    plt.legend()
    buf = BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    return send_file(buf,mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True,port=5001)
