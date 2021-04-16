# This is the script for the AI behind the handwritten digit recognizer program.

# Include relevant libraries
from __future__ import print_function # Allows us to do fancier print statements
from torch import nn, optim, cuda # Import neural network model and some optimization libraries
# Mathy libraries:
from torch.utils import data
from torchvision import datasets, transforms
import torch.nn.functional as F
import time # Lets us timestamp things nicely, makes working with time units simpler

# Training settings
batch_size = 32
device = 'cuda' if cuda.is_available() else 'cpu'

# Import the MNIST Dataset from Torchvision.
train_dataset = datasets.MNIST(root='mnist_data/',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='mnist_data/',
                              train=False,
                              transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
train_loader = data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)