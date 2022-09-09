import json
import urllib3
import boto3
#Bryan Garavito
#Creacion de la funcion que hace el scraping de la pagina del banco de la republica
#y lo guarda en un archivo txt llamado dolar-timestamp.txt

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    http = urllib3.PoolManager()
    url = 'https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario'

    resp = http.request('GET', url)
    archivo = open("dolar-timestamp.txt", "w")
    archivo.write(print(resp.data.decode('utf -8')))

    archivo.close()
    #se usa boto3 para subir el archivo a el bucket
    data = open('dolar-timestamp.txt', 'rb')
    s3.Bucket('dolarraw01').put_object(Key='dolar-timestamp.txt', Body=data)

