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
        keys_pressed = ""
        if counter == 1000:
            print("done recording")
            break
        if not paused:
            screen = grab_screen(region=(0,0,1270,720))
            
            #plt.imshow(screen)
            #plt.show()
            screen = cv2.resize(screen, (299,299))
            
            #gray_screen = rgb2gray(screen)
            if is_pressed('w'):
                keys_pressed = "w"
            if is_pressed('a'):
                keys_pressed += "a"
            if is_pressed('s'):
                keys_pressed += "s"
            if is_pressed('d'):
                keys_pressed += "d"
            
            
            data_array.append([screen,keys_pressed])
            
            """
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            break
            """
            if len(data_array) == 100:
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
    starting_value = 65
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
    time.sleep(10)
    time_start = time.time()
    start(starting_value,time_start)
