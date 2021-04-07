import cv2
import numpy as np
import urllib.request
import urllib
import time
from PIL import Image, ImageOps
class imageReader():
    def __init__(self,streamurl):
        self.stream = urllib.request.urlopen(streamurl)
        self.bytes=b''
    def getFrame(self):
        a=-1
        b=-1
        while(a==-1 or b ==-1):
            self.bytes+=self.stream.read(8192)
            a=self.bytes.find(b'\xff\xd8') # JPEG start
            b=self.bytes.find(b'\xff\xd9') # JPEG end
        jpg = self.bytes[a:b+2] # actual image
        self.bytes = self.bytes[b+2:] # other informations
        img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        #img = img[50:185, 80:250]
        return img
        