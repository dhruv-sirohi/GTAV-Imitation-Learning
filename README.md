# Autonomous Driving in GTA V using Imitation Learning

Using imitation learning to teach an agent to drive a car in GTA V, with the hopes of potentially applying the trained agent to real-world control tasks. 

Currently a Work In Progress, the ReadME will be updated and documentation for project code will be written shortly.

The Sentdex_GTAV training script was used to train an Alexnet using Sentdex's training data (https://github.com/Sentdex/pygta5). This was used an inital test. 
The Train_GTA5 training script uses the training files generated using this repo's data collection scripts to train a ResNet-50 pre-trained on ImageNet. 
