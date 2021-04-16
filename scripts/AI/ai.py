# This is the script for the AI behind the handwritten digit recognizer program.

# Include relevant libraries
from __future__ import print_function # Allows us to do fancier print statements
from torch import nn, optim, cuda # Import neural network model and some optimization libraries
# Mathy libraries:
from torch.utils import data
from torchvision import datasets, transforms
import torch.nn.functional as F
import time # Lets us timestamp things nicely, makes working with time units simpler


