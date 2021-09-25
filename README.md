# Autonomous Driving in GTA V using Imitation Learning

Using imitation learning to teach an agent to drive vehicles in GTA V, with the hopes of potentially applying the trained agent to real-world control tasks. 


## Algorithm Overview

The agent controlled the right joystick's position along the x-axis (which allows it to turn the vehicle left and right). A controller was used to allow for continuous control. Other implementations of this algorithm use key-strokes ('W', 'A', 'S', 'D'), which converts the regression task into a classification task. 

While a neural net can acheive passable performance on the classification task with minimal training, the regression task was chosen because it allows the neural network to better finetune it's outputs.

The neural network consists of a [ResNet50](https://cv-tricks.com/keras/understand-implement-resnets/ 'ResNet50') trained on the ImageNet dataset (with it's last 4 layers chopped off), 4 dense layers, and a single output layer. Dropout was initially used, but was removed due to [poor performance on regression tasks](https://towardsdatascience.com/pitfalls-with-dropout-and-batchnorm-in-regression-problems-39e02ce08e4d/ 'poor performance on regression tasks').


## Training

Around 3.5 hours of driving data was recorded for the purposes of training. 

Data collection was done using the data collection scripts in this repository: screen_record.py was used to record the screen (with a timestamp) and to save this data to a .npy file. xinput.py was used to record controller inputs (with a time stamp) and to save this data to another .npy file. data_processing.py was used to merge these .npy files together and output a merged .npy file which stored each frame in the training set, along with the controller input at that frame.
  
This dataset was then balanced, as it did not evenly represent all parts of the action space. Training on the unbalanced dataset could bias the neural network to incorrectly acting a certain way because that action makes up a larger part of the dataset.

<br />

<p align="center">

<img src="https://github.com/dhruv-sirohi/GTAV-Imitation-Learning/blob/main/training_scripts/plots/dataset_breakdown.png"/>

</p> 

<div align="center"> 
Breakdown of the unbalanced dataset
<div align="left"> 

After balancing, the dataset was made up of ~50,000 individual datapoints.
  
This data was used to train the neural network. As is the case with Imitation Learning, the network was trained on 'expert data' in the hopes that it learns underlying patterns in the expert's control routine. 
  
After 
  
  Currently a Work In Progress, the ReadME will be updated and documentation for project code will be written shortly.

The Sentdex_GTAV training script was used to train an Alexnet using Sentdex's training data (https://github.com/Sentdex/pygta5). This was used an inital test. 
The Train_GTA5 training script uses the training files generated using this repo's data collection scripts to train a ResNet-50 pre-trained on ImageNet. 
