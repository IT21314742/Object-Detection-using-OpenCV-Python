import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

video = cv2.VideoCapture(1)

while True:
    ret, Frame = video.read()
    bbox, label, conf = cv.detect_common_objects