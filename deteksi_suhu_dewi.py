from Adafruit_AMG88xx import Adafruit_AMG88xx
import Adafruit_DHT
import pygame
import os
import math
import time
import RPi.GPIO as GPIO
import numpy as np
from scipy.interpolate import griddata

from colour import Color
GPIO_TRIGGER = 24
GPIO_ECHO = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(27 , GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
GPIO.output(27,0)

#low range of the sensor (this will be blue on the screen)
MINTEMP = 19

#high range of the sensor (this will be red on the screen)
MAXTEMP = 32

#how many color values we can have
COLORDEPTH = 1024

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

#initialize the sensor
sensor = Adafruit_AMG88xx()
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 22

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

#sensor is an 8x8 grid so lets do a square
height = 570
width = 570

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

lcd = pygame.display.set_mode((width, height),pygame.FULLSCREEN)

lcd.fill((255,0,0))

pygame.display.update()
pygame.mouse.set_visible(False)

lcd.fill((0,0,0))
pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)
pygame.font.init()
font = pygame.font.Font(None, 60)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def h():
    h,t=Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return h
def t():
    h,t=Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return t

def msgtoscrn(msg,color,x):
    text = font.render("Suhu: ", True,color)
    raw = font.render(str(msg), True, color)
    maxs = font.render(str(sensor.readPixels()[7]), True, color)
    lcd.blit(raw,[620,200])
    lcd.blit(text,[620,150])
    lcd.blit(maxs,[620,300])

def limabelas(max_temp):
    suhu1 = (max_temp*0.7757)+11.851
    return suhu1

def limapuluh(max_temp):
    suhu2 = (max_temp*0.8129)+11.9
    return suhu2

def tujuhlima(max_temp):
    suhu3 = (max_temp*0.8791)+10.588
    return suhu3

def seratus(max_temp):
    suhu4 = (max_temp*0.9186)+13.051
    return suhu4

for x in range(0,5):
    GPIO.output(27,1)
    time.sleep(0.1)
    GPIO.output(27,0)
    time.sleep(0.1)
while(1):

    #read the pixels
    pixels = sensor.readPixels()
    pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
 
    
    #perdorm interpolation
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
    
    #draw everything
    for ix, row in enumerate(bicubic):
        for jx, pixel in enumerate(row):
            pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)], (displayPixelHeight * ix, displayPixelWidth * jx, displayPixelHeight, displayPixelWidth))
    # RUMUS
#    h,t=Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
#    hk=(0.7794*h())-0.5422
#    tk=(0.9781*t())-0.2572
#    hkk=hk*0.01
#    tkk=tk+273.15

    #HC-SR04
#    d=distance()
#    dk=(1.0133*d)-1.2866
#    dkk=dk*(10**(-2))

    #Rumus W
#    w1=1.5587
#    w2=6.939*0.01*tk
#    w3=-2.7816*0.0001*tk*tk
#    w4=6.8455*0.0000001*tk*tk*tk
#    w1234=w1+w2+w3+w4
#    expw=math.exp(w1234)
#    w=hkk*expw

    #Rumus Transmisi
#    sqrtdk=dkk**(0.5)
#    sqrtw=w**(0.5)
#    expt1a=(-sqrtdk)*(0.0066+(-0.0023*sqrtw))
#    expt2a=(-sqrtdk)*(0.0126+(-0.0067*sqrtw))
#    expt1=math.exp(expt1a)
#    expt2=math.exp(expt2a)
#    transmisi=(1.9*expt1)+(-0.9*expt2)

    #Rumus Utama
#    boltzmann=5.67*(10**(-8))
#    emisivity=0.95
#   maxx=round(sensor.readPixels()[27]*0.9186+10.551,2)
#    total=((maxx+273.15)**(4))*boltzmann
#    refleksi=(1-emisivity)*transmisi*boltzmann*(tkk**(4))
#   atmosfer=(1-transmisi)*boltzmann*(tkk**(4))
#    pembilang=total-refleksi-atmosfer
#    pembagi=boltzmann*emisivity*transmisi
#    suhuobjekc=round(((pembilang/pembagi)**(0.25))-273.15,2)

    maxx =round((sensor.readPixels()[28] * 0.8791) + 10.588,2)
    x=round(sensor.readPixels()[7],2)
    if maxx > 37.01:
        GPIO.output(27,1)
#       time.sleep(0.05)
#       GPIO.output(27,0)
#       time.sleep(0.05)
    else:
        GPIO.output(27,0)
    msgtoscrn(str(maxx),(255,255,255),x)
    pygame.display.update()
    lcd.fill((0,0,0))
#15 cm
#suhu = (max_temp*0.7757)+11.851

#50 cm
#suhu = (max_temp*0.8129)+11.9

#75 cm
#suhu = (max_temp*0.8791)+10.588

#100cm
#suhu = (max_temp*0.9186)+12.051
