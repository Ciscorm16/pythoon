import serial
import csv
from datetime import datetime
import simplejson
from Documentos import documentos as Doc
import time
Id=0
valors = ""
doc=Doc(Id,valors)
fecha = datetime.now()
fecha = fecha.strftime("%Y-%m-%d %H:%M:%S")
class arduino(object):
    def __init__(self,idi):
        self.idi = idi    
    def SensorUltrasonico(self):
        serialArduino = serial.Serial("COM4",9600,timeout=1.0)
        time.sleep(1) 
        valor = 0
        while True:
            cad = serialArduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'dis':
                    if valor != value:
                        print("Es val de la distancia es: {} Cm\n **************".format(value)) 
                        doc.crearSensorUltrasonic(1,value,fecha)
                        valor = value
                #Doc.SensorTemperatura(value)

    def SensorHumedad(self):
        serialArduino = serial.Serial("COM4",9600,timeout=1.0)
        time.sleep(1) 
        valor = 0
        while True:
            cad = serialArduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'Humedad': 
                    if valor != value:
                        print("Es valor de la humedad es: {} %\n **************".format(value))
                        doc.crearSensorHumedad(1,value,fecha)
                        valor = value

    def SensorTemperatura(self):
        serialArduino = serial.Serial("COM4",9600,timeout=1.0)
        time.sleep(1) 
        valor = 0
        while True:
            cad = serialArduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'Temperatura': 
                    if valor != value:
                        print("Es valor de la Temperatura es: {} C\n **************".format(value))
                        doc.crearSensorTemperatura(1,value,fecha)
                        valor = value
    
    def SensorPir(self):
        serialArduino = serial.Serial("COM4",9600,timeout=1.0)
        time.sleep(1)
        datos="Hay movimiento" 
        while True:
            cad = serialArduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'Hay Movimiento': 
                    print("Hay movimiento")
                    doc.crearSensorPir(1,datos,fecha)
    
    def MostrarDatoss(self,idi):
        print("Archivos")
        Doc.verSensor()