import os
import numpy as np

starting_value = 0
controller_file_name = 'controller-training_data-{}.npy'.format(starting_value)
if os.path.isfile(controller_file_name):
    print('Controller file exists, loading: ',starting_value)
    unprocessed_data = np.load(controller_file_name,allow_pickle=True)
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
        control_data.append(entry[1])
        #control_data.append(unprocessed_data[1][1])
        #print(controller_timestamps)
        #print(control_data)
        #break
    starting_value = 0
    continue_loop = True
    while continue_loop:
        video_file_name = 'video-training_data-{}.npy'.format(starting_value)
        if os.path.isfile(video_file_name):
            video_data = np.load(video_file_name,allow_pickle=True)
            #want to find range of controller values (by time) to average over
            processed_data = []
            controller_index_mark = 0
            for video_entry in video_data:
                ltrig_vals_to_be_averaged = []
                rtrig_vals_to_be_averaged = []
                lthumbx_vals_to_be_averaged = []
                lthumby_vals_to_be_averaged = []
                rthumbx_vals_to_be_averaged = []
                rthumby_vals_to_be_averaged = []
                
                time_value = video_entry[0]
                i = controller_index_mark

                while controller_timestamps[i] <= time_value:
                    ltrig_vals_to_be_averaged.append(control_data[i][0])
                    rtrig_vals_to_be_averaged.append(control_data[i][1])
                    lthumbx_vals_to_be_averaged.append(control_data[i][2])
                    lthumby_vals_to_be_averaged.append(control_data[i][3])
                    rthumbx_vals_to_be_averaged.append(control_data[i][4])
                    rthumby_vals_to_be_averaged.append(control_data[i][5])
                    i+=1
                controller_index_mark = i
                ltrig_mean = np.mean(ltrig_vals_to_be_averaged,1)
                rtrig_mean = np.mean(rtrig_vals_to_be_averaged,1)
                lthumbx_mean = np.mean(lthumbx_vals_to_be_averaged,2)
                lthumby_mean = np.mean(lthumby_vals_to_be_averaged,2)
                rthumbx_mean = np.mean(rthumbx_vals_to_be_averaged,2)
                rthumby_mean = np.mean(rthumby_vals_to_be_averaged,2)
                average_control_vector = [ltrig_mean,rtrig_mean,lthumbx_mean,lthumby_mean,rthumbx_mean,rthumby_mean]
                processed_data.append([average_control_vector,video_entry[1]])
            processed_data_file_name = 'processed-training_data-{}.npy'.format(starting_value)
            #grayscale here
            np.save(file=file_name,arr=np.array(data_arr),allow_pickle = True)

            
            starting_value += 1


            
        else:
            break
    
    
else:
    print("Controller File doesn't exist")


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
