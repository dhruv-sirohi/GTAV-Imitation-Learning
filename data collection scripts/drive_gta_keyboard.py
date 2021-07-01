from pynput.keyboard import Key, Controller
import time
import cv2
import os
from alexnet import alexnet
import matplotlib.pyplot as plt
from grabscreen import grab_screen
import tensorflow as tf
from skimage.color import rgb2gray
import numpy as np
from keyboard import is_pressed  # using module keyboard


WIDTH = 160
HEIGHT = 120

keyboard = Controller()


def straight():
    keyboard.press('w')
    keyboard.release('a')
    keyboard.release('d')
    #keyboard.release('s')
    
def left():
    keyboard.press('a')
    keyboard.press('w')
    #keyboard.release('a')
    keyboard.release('d')
    #keyboard.release('s')
    time.sleep(0.09)
    
def right():
    keyboard.press('d')
    keyboard.press('w')
    keyboard.release('a')
    #keyboard.release('d')
    #keyboard.release('s')
    time.sleep(0.09)

#model = alexnet()
#model.load("gta_sentdex_model_epoch_30.h5")
model = tf.keras.models.load_model("gta_sentdex_model_epoch_30.h5")

def main():
    print("bike should be in 3rd person view!")
    print("starting in 5 seconds")
    for i in range(4,-1,-1):
        print(i)
        time.sleep(1)
    paused = False

    while(True):
        if is_pressed('o'):
            if paused:
                print("unpaused!")
                time.sleep(1)
                paused = False
            else:
                print("paused")
                paused = True
        if not paused:
            #screen = grab_screen(region=(0,0,1366,768))
            screen = grab_screen(region=(0,25,800,625))
            screen = cv2.resize(screen, (160,120))
            gray_tensor = tf.convert_to_tensor(rgb2gray(screen))
            input_data_shape = [1] + list(gray_tensor.shape) + [1]
            gray_tensor_reshaped = tf.reshape(gray_tensor,input_data_shape)
            prediction = model.predict(gray_tensor_reshaped)[0]
            print(prediction)
            turn_confidence = 0.75
            straight_confidence = 0.7
            if prediction[0] > turn_confidence:
                left()
            elif prediction[1] > turn_confidence:
                straight()
            elif prediction[2] > turn_confidence:
                right()
            #break
            #print(model.summary)
                

if __name__ == "__main__":
    main()
    

    #screen = grab_screen(region=(0,25,800,625))
    #screen = grab_screen(region=(0,0,1366,768))
    #print("started")
    """
    data = np.load('training_data-22-balanced.npy',allow_pickle=True)
    for entry in data:
        plt.imshow(entry[0])
        plt.show()
        #X = np.array(entry[0]).reshape(WIDTH,HEIGHT,1)
        #plt.imshow(X)
        #plt.show()
    
    #tf.reshape(gray_tensor,
    #screen = cv2.resize(screen, (160,120))
    plt.imshow(screen)
    plt.show()
    
    gray_tensor = tf.convert_to_tensor(rgb2gray(screen))
    input_data_shape = [1] + list(gray_tensor.shape) + [1]
    print(gray_tensor.shape)
    gray_tensor_reshaped = tf.reshape(gray_tensor,input_data_shape)
                    
    prediction = model.predict(gray_tensor_reshaped)
    print(prediction)
    print(model.summary)
    """

"""


from PIL import Image
import IPython.display as display


from tensorflow import keras
"""
"""
import vgamepad as vg
import time
import math

print("hey")

def start(model_file_name):
    gamepad = vg.VX360Gamepad()
    cnn_model = tf.keras.models.load_model(model_file_name)
    #start_time = time.time()
    #screen = grab_screen(region=(0,0,1270,720))
            
            #plt.imshow(screen)
            #plt.show()
    #screen = cv2.resize(screen, (160,120))
    #gray_tensor = tf.convert_to_tensor(rgb2gray(screen))
    #print(gray_tensor.shape)       
    #x = np.random.rand(2,160,120,1)
    #X = tf.convert_to_tensor(x)
    #input_data_shape = [1] + list(gray_tensor.shape) + [1]
            
    #gray_tensor_reshaped = tf.reshape(gray_tensor,input_data_shape)
    #print(gray_tensor_reshaped.shape)
    
    #predictions = cnn_model.predict(gray_tensor_reshaped)
    #print(predictions)
    #print(time.time()-start_time)
    #h+=1
    #time_end = time_start + 10
    avg_fps = []
    time1 = time.time()
    bool_val = True
    i = 0
    paused = False
    data_array = []
    counter = 0
    print("paused")
    while True:
        starting_value = 210
        if not paused:
            video_file_name = 'training_data/video-training_data-{}.npy'.format(starting_value)
            starting_value += 1
            if os.path.isfile(video_file_name):
                print("started")
                video_data = np.load(video_file_name,allow_pickle=True)
                for video_entry in video_data:
                    #start_time = time.time()
                    screen = video_entry[1]

                    #print(gray_tensor.shape)
                    #h+=1
                    gray_tensor = tf.convert_to_tensor(rgb2gray(screen))

                    input_data_shape = [1] + list(gray_tensor.shape) + [1]

                    gray_tensor_reshaped = tf.reshape(gray_tensor,input_data_shape)
                                
                    control_vector = cnn_model.predict(gray_tensor_reshaped)
                            
                            
                    lt = control_vector[0][0]
                    rt = control_vector[0][1]
                    ls = control_vector[0][2]

                    #modifying controls for vgamepad
                    ls = float((ls - 0.5)*2)
                    
                    print("left trigger val: {}, right trigger val: {}, left stick xval: {}".format(lt,rt,ls)) 
                    
                    #print(1/(time.time()-start_time))

                    #if (control_vector[0][2]-0.5)*2 > 0.05:
                    #    print((control_vector[0][2]-0.5)*2)
                    #    plt.imshow(video_entry[1])
                    #    plt.show()
                            
            
            screen = grab_screen(region=(0,0,1270,720))
                    
            screen = cv2.resize(screen, (160,120))

            gray_tensor = tf.convert_to_tensor(rgb2gray(screen))

            input_data_shape = [1] + list(gray_tensor.shape) + [1]

            gray_tensor_reshaped = tf.reshape(gray_tensor,input_data_shape)
                        
            control_vector = cnn_model.predict(gray_tensor_reshaped)
                    
                    
            lt = control_vector[0][0]
            rt = control_vector[0][1]
            ls = control_vector[0][2]

            #modifying controls for vgamepad
            ls = float((ls - 0.5)*2)
            #gamepad.left_trigger_float(1)
            gamepad.left_trigger_float(float(lt))
            gamepad.right_trigger_float(float(rt))
            gamepad.left_joystick_float(x_value_float=ls, y_value_float=0.0)
            gamepad.update()
            
            print("left stick xval: {}".format(ls)) 
                    
            time.sleep(0.001)
        else:
            #gamepad.right_trigger_float(1.00)
            gamepad.right_joystick_float(x_value_float=(time.time()%5-2.5)/2.5, y_value_float=0.0)
            print((time.time()%5-2.5)/2.5)
            gamepad.update()
            #time.sleep(0.01)
        
        if is_pressed('o'):
            if paused:
                gamepad.right_joystick_float(x_value_float=0, y_value_float=0.0)
                gamepad.update()
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                gamepad.right_joystick_float(x_value_float=0, y_value_float=0.0)
                gamepad.update()
                print('Pausing!')
                paused = True
                time.sleep(1)
    
if __name__ == "__main__":
    print("press q to start")
    while True:
        if is_pressed('q'):
            break
    print("STARTING")
    start("gta_cnn_model_epoch_150.h5")
"""
