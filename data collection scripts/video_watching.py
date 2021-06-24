import os
import numpy as np
from skimage.color import rgb2gray
import cv2
import time
import matplotlib.pyplot as plt


def start():
    print("start")
    starting_value = input("which video #?")
    video_file_name = 'video-training_data-{}.npy'.format(starting_value)

    if os.path.isfile(video_file_name):
        unprocessed_data = np.load(video_file_name,allow_pickle=True)
        for entry in unprocessed_data:
            cv2.imshow("gta",entry[1])
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
    start()

start()
