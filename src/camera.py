import time
import pygame
import pygame.camera

class Camera():
    def __init__(self):
        pygame.camera.init()
        camlist = pygame.camera.list_cameras() #Camera detected or not
        self.cam = None
        if camlist:
            self.cam = pygame.camera.Camera(camlist[0],(640, 480))
            self.cam.start()
        else:
            print("Camera not found: Please check connection")

    def take_picture(self):
        camstarttime = int(time.time())
        imgname = str(camstarttime) + ".jpg"
        while (camstarttime + 3) > time.time():
            if self.cam.query_image():
                img = self.cam.get_image()
                return img, imgname
        print("Camera not stable: Please check connection")
        return None, None

    def stop_camera(self):
        self.cam.stop()