import csv
import shutil
from tempfile import NamedTemporaryFile
class documentos(object):
    def __init__(self,idi,id_sensor=None,datos=None,nombre=None,descripcion=None):
        self.datos=datos
        self.idi=idi
        self.id_sensor = id_sensor
        self.nombre = nombre
        self.descripcion = descripcion

    def ResultadosSensor(self,idi,id_sensor,datos,fecha):
        with open('resultados.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','id_sensor','Datos','fecha'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id': idi,'id_sensor':id_sensor,'Datos': datos,'fecha':fecha})

    def verSensor(self,id_sensor):
        with open('resultados.csv','r') as resultados:
            verCsv = csv.DictReader(resultados)
            for resultados in verCsv:
                print(resultados)

    def Sensores(self,id_sensor,nombre,descripcion):
        with open('sensores.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','sensor','descripcion'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id': id_sensor,'sensor':nombre,'descripcion': descripcion})

    def crearSensorTemperatura(self,idi,datos,fecha):
        with open('Temperatura.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','Temperatura','fecha'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id': idi,'Temperatura': datos,'fecha':fecha})

    def verSensorTemperatura(self):
        with open('Temperatura.csv','r') as temperatura:
            verCsv = csv.DictReader(temperatura)
            for temp in verCsv:
                print(temp)
    
    def crearSensorUltrasonic(self,idi,datos,fecha):
        with open('Ultrasonico.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','Ultrasonico','fecha'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id':idi,'Ultrasonico':datos,'fecha':fecha})

    def verSensorUltrasonic(self):
        with open('Ultrasonico.csv','r') as Ultrasonico:
            verCsv = csv.DictReader(Ultrasonico)
            for Ultrasonic in verCsv:
                print(Ultrasonic)

    def crearSensorHumedad(self,idi,datos,fecha):
        with open('Humedad.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','Humedad','fecha'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id':idi,'Humedad':datos,'fecha':fecha})

    def verSensorHumedad(self):
        with open('Humedad.csv','r') as Humedad:
            verCsv = csv.DictReader(Humedad)
            for Humedada in verCsv:
                print(Humedada)

    def crearSensorPir(self,idi,datos,fecha):
        with open('Pir.csv', 'a', newline='\n') as archivo:
            csvW = csv.DictWriter(archivo, fieldnames=['id','PIR','fecha'])
            if archivo.tell() == 0:
                csvW.writeheader()
            csvW.writerow({'id':idi,'PIR':datos,'fecha':fecha})

    def verSensorPir(self):
        with open('Pir.csv','r') as PIR:
            verCsv = csv.DictReader(PIR)
            for PIR in verCsv:
                print(PIR)

    def obtenerId(self):
        Idie = 0
        with open('obtenerId.csv','r') as oia:
            cvsR = csv.DictReader(oia)
            for row in cvsR:
                for(x,y) in row.items():
                    if x == 'id':
                        Idie = int(y)+1
                    else:
                     Idie = 1
        with open('obtenerId.csv','w') as write:
               cvsW = csv.DictWriter(write, fieldnames=['id'])
               cvsW.writeheader()
               cvsW.writerow({'id': Idie})
               return Idie