import cv2

cv2.namedWindow("camera")

vc = cv2.VideoCapture(0)

class Camera():

    def __init__(self,def_ref_rate:int=5,def_timeout:int=30):
        
        # internal parameters
        self.ref_rate = def_ref_rate
        self.timeout = def_timeout

        # capture content from video camera
        self.vc = cv2.VideoCapture(0)

    def __del__(self):
        self.vc.release()