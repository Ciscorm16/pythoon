import time
from gpiozero import MotionSensor
import Adafruit_DHT
import RPi.GPIO as GPIO
from Documentos import documentos as Doc

class raspberry(object):
    def __init__(self,idi):
        self.idi = idi 
    
    def SensorPir(self):
        pir=MotionSensor(4)
        while True:
            pir.wait_for_motion()
            print("Movimiento")
            pir.wait_for_no_motion
            print("Movimiento Detenido")
    
    def SensorPir2(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)   
        while True:
            i=GPIO.input(11)
            if i==0:                 #When output from motion sensor is LOW
                print( "No intruders",i)
                time.sleep(0.1)
            elif i==1:               #When output from motion sensor is HIGH
                print("Intruder detected",i)
                time.sleep(0.1)
    
    def SensorTemperatura(self):
        DHT_SENSOR = Adafruit_DHT.DHT11
        DHT_PIN = 4
        while True:
            temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
            if temperature is not None:
                print("temp={0:0.1f}C)".format(temperature))
            else:
                print("Fallo Lectura")
            time.sleep(3)
    
    def SensorHumedad(self):
        DHT_SENSOR = Adafruit_DHT.DHT11
        DHT_PIN = 4
        while True:
            humidity = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
            if humidity is not None:
                print("humidity={1:0.1f}C)".format(humidity))
            else:
                print("Fallo Lectura")
            time.sleep(3)
    
    def SensorUltrasonico(self):
        GPIO.setmode(GPIO.BCM)
        TRIG = 23 
        ECHO = 24
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
    try:
        while True:

            GPIO.output(TRIG, False)
            print("Esperando que el sensor se estabilice")
            time.sleep(2)

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150

            distance = round(distance, 2)

            print("Distancia:",distance,"cm")

    except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        gpio.cleanup()
        