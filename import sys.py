import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE = 'map.png'

# (UL-X, UL-Y, LR-X, LR-Y)
SA1_CORNERS = (130, 265, 180, 315)
SA2_CORNERS = (80, 255, 130, 305) 
SA3_CORNERS = (105, 205, 155, 255) 

class Search():
    """Bayesian Search & Rescue project"""
    def __init__(self, name):
        self.name = name;
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img == None:
            print('U forgot to add the file dumas.')
            sys.exit(1)
        
        self.area_actual = 0;
        self.sailor_actual = [0, 0] # As "local" coordinates within search area

        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3], SA1_CORNERS[0] : SA1_CORNERS[2]]
        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3], SA2_CORNERS[0] : SA2_CORNERS[2]]
        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], SA3_CORNERS[0] : SA3_CORNERS[2]]

        self.p1 = .2
        self.p2 = .5
        self.p3 = .3

        self sep1 = 0
        self sep2 = 0
        self sep3 = 0