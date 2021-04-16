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

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # Start with a basic 2-layer neural network
        self.l1 = nn.Linear(784, 392)
        self.l2 = nn.Linear(392, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        return self.l2(x)

# Create the model
model = Net()
model.to(device)
# Use cross entropy loss function
criterion = nn.CrossEntropyLoss()
# Try optimising with basic stochastic gradient descent setup first
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9

def train(epoch):
    model.train() # Puts the model into training mode
    for batch_idx, (data, target) in enumerate(train_loader): # iterate through the training dataset
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item())))