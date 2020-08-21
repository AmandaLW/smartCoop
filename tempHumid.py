#sensor module
#imports
import sys
import time
import datetime
import SDL_Pi_HDC1000

class Humidity:
    def __init__(self):
        self.hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

    def getReading(self):
        self.humidity = self.hdc1000.readHumidity()

class Temperature:
    def __init__(self):
        self.hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

    def getReading(self):
        self.temp = self.hdc1000.readTemperature()


temp1 = Temperature()
temp1.getReading()
print(temp1.temp)