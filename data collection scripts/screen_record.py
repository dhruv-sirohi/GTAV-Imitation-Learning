#TO DO:
#customizable recording lengths
#prune imports

import cv2
import time
from keyboard import is_pressed  # using module keyboard
import os
from PIL import Image
import numpy as np
from grabscreen import grab_screen
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import IPython.display as display
import matplotlib.pyplot as plt

def start(starting_value,time_start):
    file_name = 'video-training_data-{}.npy'.format(starting_value)
    #time_end = time_start + 10
    avg_fps = []
    time1 = time.time()
    bool_val = True
    i = 0
    paused = False
    data_array = []
    counter = 0
    while True:
        if counter == 25:
            print("done recording")
            break
        if not paused:
            screen = grab_screen(region=(0,0,799,599))
            screen = cv2.resize(screen, (80,60))
            
            #gray_screen = rgb2gray(screen)
            
            data_array.append([round(time.time(),2),screen])
            
            """
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            """
            if len(data_array) == 500*5:
                time_start = time.time()
                np.save(file_name,data_array)#,allow_pickle = True)
                print(time.time()-time_start)#> time_end:
                print('ALL DONE SAVED')            
                counter = counter +1
                data_array = []
                starting_value += 1
                file_name = 'video-training_data-{}.npy'.format(starting_value)
        if is_pressed('p'):
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
if __name__ == "__main__":
    starting_value = 0
    print("press q to start")
    while True:
        if is_pressed('q'):
            break
    while True:
        file_name = 'video-training_data-{}.npy'.format(starting_value)

        if os.path.isfile(file_name):
            print('File exists, moving along',starting_value)
            starting_value += 1
        else:
            print('File does not exist, starting fresh!',starting_value)
            break
    time_start = time.time()
    start(starting_value,time_start)
