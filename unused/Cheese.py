import time
import pygame
import pygame.camera

def take_picture():
    pygame.camera.init()
    camlist = pygame.camera.list_cameras() #Camera detected or not
    if camlist:
       cam = pygame.camera.Camera(camlist[0],(640, 480))
    else:
        print("Camera not found: Please check connection")
        return None, None
    cam.start()
    camstarttime = int(time.time())
    imgname = str(camstarttime) + ".jpg"
    while (camstarttime + 3) > time.time():
        if cam.query_image():
            img = cam.get_image()
            pygame.image.save(img, imgname)
            print("Image", imgname, "saved successfully and sent")
            cam.stop()
            return img, imgname
    print("Camera not stable: Please check connection")
    cam.stop()
    return None, None
