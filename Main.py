from datetime import date
import os
from Arduino import arduino as Ardui
from Documentos import documentos as Doc
os.system ("clear") 
option=""
Menu = True
Opcion = 0
IdP=0
IdTH=0
IdU=0
MId=0
Id=0
datos=""
doc = Doc(Id)
Fecha = date.today()
Ard = Ardui(Id)
os.system ("clear") 
while Menu == True:
    print("Bienvenido Que deseas realizar?")
    selection=int(input("1)Leer arduino 2)Leer raspberry pi?"))
    if selection==1:
        print("---------------")
        print("1)Leer el sensor Pir \n"
        "2)Leer el sensor Temperatura \n"
        "3)Leer eL sensor ultrasónico \n"
        "4)Leer eL sensor humedad\n"
        "5)Mostrar datos Pir\n"
        "6)Mostrar datos Temperatura\n"
        "7)Mostrar Datos Ultrasonico\n"
        "8)Mostrar datos Humedad\n"
        "9)Correr Servidor Web\n"
        "0)Salir")
        Opcion = int(input("Seleccione la accion que desea realizar:"))
        if Opcion==1:
            Ard.SensorPir()
            pass
        if Opcion==2:
            Ard.SensorTemperatura()
            pass 
        if Opcion==3:
            Ard.SensorUltrasonico()
            pass
        if Opcion==4: 
            Ard.SensorHumedad()
            pass
        if Opcion==5:
            doc.verSensorPir()
            pass
        if Opcion==6:
            doc.verSensorTemperatura()
            pass
        if Opcion==7:
            doc.verSensorUltrasonic()
            pass
        if Opcion==8:
            doc.verSensorHumedad()
            pass
        if Opcion==9:
            pass
        if Opcion==0:
            os.system ("clear") 
            print("Hasta luego!.")
            break
    if selection==2:
        print("---------------")
        print("1)Leer el sensor Pir \n"
        "2)Leer el sensor Temperatura \n"
        "3)Leer eL sensor ultrasónico \n"
        "4)Leer eL sensor humedad\n"
        "5)Mostrar datos Pir\n"
        "6)Mostrar datos Temperatura\n"
        "7)Mostrar Datos Ultrasonico\n"
        "8)Mostrar datos Humedad\n"
        "9)Correr Servidor Web\n"
        "0)Salir")
        Opcion = int(input("Seleccione la accion que desea realizar:"))
        if Opcion==1:
            sensore.SensorPir()
            pass
        if Opcion==2:
            sensore.SensorTemperatura()
            pass 
        if Opcion==3:
            sensore.SensorUltrasonico()
            pass
        if Opcion==4: 
            sensore.SensorHumedad()
            pass
        if Opcion==5:
            doc.verSensorPir()
            pass
        if Opcion==6:
            doc.verSensorTemperatura()
            pass
        if Opcion==7:
            doc.verSensorUltrasonic()
            pass
        if Opcion==8:
            doc.verSensorHumedad()
            pass
        if Opcion==9:
            pass
        if Opcion==0:
            os.system ("clear") 
            print("Hasta luego!.")
            break
    else:
        print("Eliga una opcion")