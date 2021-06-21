import os
import numpy as np
from skimage.color import rgb2gray
import cv2
import time
import matplotlib.pyplot as plt



starting_value = 0
controller_file_name = 'controller-training_data-{}.npy'.format(starting_value)
unprocessed_data = []
while os.path.isfile(controller_file_name):
    print(starting_value)
    if unprocessed_data == []:
        unprocessed_data = list(np.load(controller_file_name,allow_pickle=True))
    else:
        unprocessed_data = unprocessed_data + list(np.load(controller_file_name,allow_pickle=True))
    starting_value += 1
    controller_file_name = 'controller-training_data-{}.npy'.format(starting_value)

    print(len(unprocessed_data))
    """
    Format:
    [[['left_trigger', 0.0],
    ['right_trigger', 0.0],
    ['l_thumb_x', -0.015274280918593118],
    ['l_thumb_y', -0.04847791256580453],
    ['r_thumb_x', 0.08467231250476845],
    ['r_thumb_y', -0.031906614785992216]]]
    """
controller_timestamps = []
control_data = []
for entry in unprocessed_data:
    controller_timestamps.append(entry[0])
    control_vector = entry[1][:3] + [entry[1][4]]
    control_data.append(control_vector)
    #print(entry[1][:3])
    #control_data.append(unprocessed_data[1][1])
    #print(controller_timestamps)
    #print(control_data)
    #break
print("done with controller arrays")
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
        for video_entry in video_data:
            """
            ltrig_vals_to_be_averaged = []
            rtrig_vals_to_be_averaged = []
            lthumbx_vals_to_be_averaged = []
            lthumby_vals_to_be_averaged = []
            rthumbx_vals_to_be_averaged = []
            rthumby_vals_to_be_averaged = []
            """
            control_vals_to_be_averaged = []
            #plt.imshow(video_entry[1])
            #plt.show()
            time_value = video_entry[0]
            i = controller_index_mark
            if i < len(controller_timestamps):                
                while controller_timestamps[i] <= time_value:
                    control_vals_to_be_averaged.append(control_data[i])
                    i+=1
                    if i == len(controller_timestamps):
                        break
                controller_index_mark = i
                mean_control_vals = []
                if len(control_vals_to_be_averaged) > 0:
                    mean_control_vals = list(np.mean(control_vals_to_be_averaged,0))
                    #print(mean_control_vals)
                    for index in range(0,len(mean_control_vals)):
                        dec_places = 1
                        translation_value = 0
                        if index > 1:
                            dec_places = 2
                            translation_value = 0.5
                        mean_control_vals[index] = round(mean_control_vals[index],dec_places) + translation_value
                    prev_control_vals = mean_control_vals
                    #print(prev_control_vals)
                else:
                    mean_control_vals = prev_control_vals
                processed_data.append([mean_control_vals,video_entry[1]])
            else:
                break
        processed_data_file_name = 'processed-training_data-{}.npy'.format(starting_value)
        #print(len(processed_data))
        #print(len(video_data))
        np.save(file=processed_data_file_name,arr=np.array(processed_data),allow_pickle = True) 
        #print(len(processed_data))
        starting_value += 1  
    else:
        if starting_value > 233:
            break
        else:
            starting_value += 1  


"""
while continue_loop:
    
    processed_array = []
 
            video_file_name = 'video-training_data-{}.npy'.format(starting_value)
            unprocessed_data = np.load(controller_file_name,allow_pickle=True)
            video_data = np.load(video_file_name,allow_pickle=True)
            
            break
            for entry in unprocessed_data:
                #print(entry)
                #print(entry[0])
                time = round(entry[0],2)
                unprocessed_control_data = entry[1]
                control_vector = []
                for entry in unprocessed_control_data:
                    control_vector.append(entry[2])
                processed_array.append([time,control_vector])
            #print("length: ", len(unprocessed_data))
            #print(processed_array)
            starting_value += 1
    else:
        print("done")
        continue_loop = False
"""
print("finished")
