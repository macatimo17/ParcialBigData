import csv
import boto3
import pandas as pd
#Bryan Garavito
#Creacion de la funcion que hace la conversion del archivo txt a cvs
def lambda_handler2(event, context):
    s3 = boto3.resource('s3')
    out = open('dolar-timestamp.csv', 'w', newline='')
    csv_writer = csv.writer(out, dialect='excel')
    f = open("https://dolarraw01.s3.amazonaws.com/dolar-timestamp.txt", "r")
    #Se crean las columnas del cvs
    websites = pd.read_csv("dolar-timestamp.txt", header=None)
    websites.columns = ['Fecha Hora', 'Valor']
    websites.to_csv('dolar-timestamp.csv',index=None)
    for line in f.readlines():
        line = line.replace(',', '\ t')  # Reemplaza la coma de cada línea con un espacio
        list = line.split()  # Convierta la cadena en una lista, para que pueda escribir csv por celda
    csv_writer.writerow(list)
    # se usa boto3 para subir el archivo a el bucket
    data = open('dolar-timestamp.csv', 'rb')
    s3.Bucket('ddolarprocessed01').put_object(Key='dolar-timestamp.txt', Body=data)