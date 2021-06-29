import os
import numpy as np
from skimage.color import rgb2gray
import cv2
import time
import matplotlib.pyplot as plt
import random
from random import shuffle


w =  [1,0,0,0,0,0,0]
s =  [0,1,0,0,0,0,0]
wa = [0,0,1,0,0,0,0]
wd = [0,0,0,1,0,0,0]
sa = [0,0,0,0,1,0,0]
sd = [0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,1]


starting_value = 0
continue_loop = True
while continue_loop:
    print(starting_value)
    video_file_name = 'video-training_data-{}.npy'.format(starting_value)
    if os.path.isfile(video_file_name):
        video_data = np.load(video_file_name,allow_pickle=True)
        #want to find range of controller values (by time) to average over
        processed_data = []
        prev_control_vals = []
        controller_index_mark = 0
                
        w_list = []
        s_list = []
        wa_list = []
        wd_list = []
        sa_list = []
        sd_list = []
        nk_list = []
        for video_entry in video_data:
           screen = video_entry[0]
           keys_pressed = video_entry[1]
           screen_flipped = cv2.flip(screen, 1)

            if keys_pressed == 'w':
                w_list.append(screen,w)
                w_list.append(screen_flipped,w)
            elif keys_pressed == 's':
                s_list.append(screen,s)
                s_list.append(screen_flipped,s)
            elif keys_pressed == 'wa':
                wa_list.append(screen,wa)
                wd_list.append(screen_flipped,wd)
            elif keys_pressed == 'wd':
                wd_list.append(screen,wd)
                wa_list.append(screen_flipped,wa)
            elif keys_pressed == 'sa':
                sa_list.append(screen,sa)
                sd_list.append(screen_flipped,sd)
            elif keys_pressed == 'sd':
                sd_list.append(screen,sd)
                sa_list.append(screen_flipped,sa)
            elif keys_pressed == '':
                nk_list.append(screen,nk)
                nk_list.append(screen_flipped,nk)
        
        shuffle(w_list)
        
        #balancing
        processed_data = w_list[0:len(wa_list)] + wa_list + wd_list + sa_list + sd_list + nk_list + s_list
            
        processed_data_file_name = 'processed-training_data-{}.npy'.format(starting_value)
        #print(len(processed_data))
        #print(len(video_data))
        np.save(file=processed_data_file_name,arr=np.array(processed_data),allow_pickle = True) 
        #print(len(processed_data))
        starting_value += 1  
    else:
        if starting_value > 1000:
            break
        else:
            starting_value += 1  

print("finished")