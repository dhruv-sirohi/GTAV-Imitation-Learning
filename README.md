# Autonomous Driving in GTA V using Imitation Learning

Using imitation learning to teach an agent to drive vehicles in GTA V, with the hopes of eventually applying the trained agent to real-world control tasks. 


## Algorithm Overview

The agent controlled the right joystick's position along the x-axis (which allows it to turn the vehicle left and right). A controller was used to allow for continuous control. Other implementations of this algorithm use key-strokes ('W', 'A', 'S', 'D'), which converts the regression task into a classification task. 

While a neural net can acheive passable performance on the classification task with minimal training, the regression task was chosen because it allows the neural network to better finetune its outputs.

The neural network consists of a [ResNet50](https://cv-tricks.com/keras/understand-implement-resnets/ 'ResNet50') trained on the ImageNet dataset (with its last 4 layers chopped off), 4 dense layers, and a single output layer. Dropout was initially used, but was removed due to [poor performance on regression tasks](https://towardsdatascience.com/pitfalls-with-dropout-and-batchnorm-in-regression-problems-39e02ce08e4d/ 'poor performance on regression tasks').

The Sentdex_GTAV training script was used to train an Alexnet using [Sentdex's training data](https://github.com/Sentdex/pygta5 "Sentdex's training data"). This was used an inital test. 

## Data Collection + Processing

Around 3.5 hours of driving data was recorded for the purposes of training. 

Data collection was done using the data collection scripts in this repository: screen_record.py was used to record the screen (with a timestamp) and to save this data to a .npy file. xinput.py was used to record controller inputs (with a time stamp) and to save this data to another .npy file. data_processing.py was used to merge these .npy files together and output a merged .npy file which stored each frame in the training set, along with the controller input at that frame.
  
This dataset was then balanced, as it did not evenly represent all parts of the action space. Training on the unbalanced dataset could bias the neural network to incorrectly acting a certain way because that action makes up a larger part of the dataset.

<br />

<p align="center">

<img src="https://github.com/dhruv-sirohi/GTAV-Imitation-Learning/blob/main/training_scripts/plots/dataset_breakdown.png"/>

  </p> 

<div align="center"> 
Breakdown of part of the unbalanced dataset
  <div align="left">  
    
<br />  
  
After balancing, the dataset was made up of ~50,000 individual datapoints.
  
## Training
  
This data was used to train the neural network. As is the case with Imitation Learning, the network was trained on 'expert data' in the hopes that it learns underlying patterns in the expert's control routine. 
  
After 105 epochs of training, test accuracy plateaued at ~80%, with training accuracy reaching ~85%. Originally, accuracy values platueaued at ~60%. However this was improved upon by saving weights and restarting training with a learning rate of 2 e-3 (training at Epoch 0 starts with a learning rate of 1.2 e-2). This helps the optimizer get out of local minima.
  
<br />

<p align="center">

<img src="https://github.com/dhruv-sirohi/GTAV-Imitation-Learning/blob/main/training_scripts/plots/Epoch105_accuracy_plot.png"/>

  </p> 
  
<div align="center"> 
Plot of training accuracy (in blue) and test accuracy (in red) over the course of training
  <div align="left">       
  
<br />

<p align="center">

<img src="https://github.com/dhruv-sirohi/GTAV-Imitation-Learning/blob/main/training_scripts/plots/Epoch105_loss.png"/>

  </p> 
  
<div align="center"> 
Plot of training loss (in blue) and test loss (in red) over the course of training. 

Some sudden spikes in test loss can be seen, likely caused by the training restarts, which may intitially have found a less favourable set of weights.
  <div align="left">     

## Agent Performance
    
After some tweaks to the training process and the control script to drive the vehicle, the agent was able to acheive solid performance, avoiding incoming traffic, and following through on turns (instead of reversing course in the middle of a turn). 
    
This is a significant improvement from the AlexNet trained on Sentdex's data, which generally just drives straight forward, and tries to avoid some obstacles (with... mixed performance).
    
There are still multiple avenues for improvement:

    • GTA V has a GPS functionality, which shows a path to a chosen destination. This could be made part of training data, so that the agent learns to follow a path instead of simply driving aimlessly.
    • Right now, the agent only controls the joystick's x-axis. A next step could be giving it control of the throttle as well
    • An RNN could be used to train on time series data. This could allow the agent to make complicated moves that take multiple frames to complete, and further increase follow through rate on maneuevers.
    • RL could be used to train the agent in game, and further improve its performance.


    
ReadMe To-Do: Attach a video of agent performance
