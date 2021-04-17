# This is the script for the AI behind the handwritten digit recognizer program.

# Include relevant libraries
from __future__ import print_function # Allows us to do fancier print statements
from torch import nn, optim, cuda, save, load # Import neural network model and some optimization libraries
# Mathy libraries:
from torch.utils import data
from torchvision import datasets, transforms, io
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
model.load_state_dict(load('trained_models/trained.pth'))
model.to(device)
# Use cross entropy loss function
criterion = nn.CrossEntropyLoss()
# Try optimising with basic stochastic gradient descent setup first
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

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
                100. * batch_idx / len(train_loader), loss.item()))


def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        # sum up batch loss
        test_loss += criterion(output, target).item()
        # get the index of the max
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} '
          f'({100. * correct / len(test_loader.dataset):.0f}%)')

"""def test_input(user_input):
    model.eval()
    user_input = user_input.to(device)
    output = model(data)

    print(f'Model predicts: {output:.0f}')"""


if __name__ == '__main__':
    since = time.time()
    """for epoch in range(1, 10):
        epoch_start = time.time()
        train(epoch)
        m, s = divmod(time.time() - epoch_start, 60)
        print(f'Training time: {m:.0f}m {s:.0f}s')
        test()
        m, s = divmod(time.time() - epoch_start, 60)
        print(f'Testing time: {m:.0f}m {s:.0f}s')

    m, s = divmod(time.time() - since, 60)
    print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {device}!')"""
    save(model.state_dict(), 'trained_models/trained.pth')
    print('Model saved')
    image = io.read_image('user_data/test_9.jpg')
    user_input_process = transforms.Compose([transforms.Grayscale()])
    image = user_input_process(image)
    
    image = transforms.functional.invert(image) / 255
    #print(image)
    output = F.softmax(model(image))
    #print(test_dataset[0][0])
    #output = model(test_dataset[0][0])
    print(f'Probability of each possible digit:\n\
        0: {output[0][0]*100:.0f}%,\n\
        1: {output[0][1]*100:.0f}%,\n\
        2: {output[0][2]*100:.0f}%,\n\
        3: {output[0][3]*100:.0f}%,\n\
        4: {output[0][4]*100:.0f}%,\n\
        5: {output[0][5]*100:.0f}%,\n\
        6: {output[0][6]*100:.0f}%,\n\
        7: {output[0][7]*100:.0f}%,\n\
        8: {output[0][8]*100:.0f}%,\n\
        9: {output[0][9]*100:.0f}%,\n')



    """
    user_loader = data.DataLoader(dataset = image)
    for data in user_loader:
        data = data.to(device)
        output = model(data)
        print(output)
"""