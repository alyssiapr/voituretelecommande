from machine import Pin, PWM
import time

# Set up la MANETTE
from machine import Pin, ADC
from machine import Pin, PWM
import random 
import utime

xAxis = ADC(Pin(28))
yAxis = ADC(Pin(27))
button = Pin(16,Pin.IN, Pin.PULL_UP)

#Set up les moteurs

#moteur 1
motor1_pin1 = Pin(6, Pin.OUT)
motor1_pin2 = Pin(7, Pin.OUT)
EN_A = Pin(8, Pin.OUT)

#moteur 2
motor2_pin1 = Pin(4, Pin.OUT)
motor2_pin2 = Pin(3, Pin.OUT)
EN_B = Pin(2, Pin.OUT)

EN_A.high()
EN_B.high()


def avancer():
        motor1_pin1.high()
        motor1_pin2.low()
        motor2_pin1.high()
        motor2_pin2.low()

def reculer():
    motor1_pin1.low()
    motor1_pin2.high()
    motor2_pin1.low()
    motor2_pin2.high()
        

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    """if xValue <= 600:
        xStatus = "GAUCHE"
    elif xValue >= 60000:
        xStatus = "DROITE"
    if yValue <= 600:
        yStatus = "AVANCE"
    elif yValue >= 60000:
        yStatus = "RECULE"
    
    print(" " + xStatus + " " + yStatus)"""
    if yValue <= 600:
        print("a")
        avancer()
    time.sleep(0.1)
    
    
#     FAIRE AVANCER LA VOITURE AVEC LA MANETTE

#avancer
#if yValue <= 600:
 #   avancer()
    
#if yValue >= 60000:
   # reculer()

    

