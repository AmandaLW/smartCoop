# Camera class
from picamera import PiCamera
from time import sleep

class Camera:
    def __init__(self):
        self.camera = PiCamera()

    def takePhoto(self, rate):
        self.i = rate
        self.camera.start_preview()
        sleep(5)
        self.camera.capture('/home/pi/Desktop/image.jpg')
        self.camera.stop_preview()


    def takeVideo(self):
        pass


#Testing
cam1 = Camera()
cam1.takePhoto(2)
