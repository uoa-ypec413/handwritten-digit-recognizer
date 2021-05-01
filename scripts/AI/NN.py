from torch import nn # Import neural network model
import torch.nn.functional as F

# Basic, 2-layer, linear NN.
class BasicNN(nn.Module):

    def __init__(self):
        super(BasicNN, self).__init__()
        self.l1 = nn.Linear(784, 392)
        self.l2 = nn.Linear(392, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        return F.softmax(self.l2(x), 1)

# LeNet-5 Model by Yann LeCun
class LeNet5(nn.Module):
    
    def __init__(self):
        super(LeNet5, self).__init__()
        # Image is padded to get an input size of 32x32
        self.conv1 = nn.Conv2d(in_channels= 1, out_channels= 6, kernel_size= 5, stride= 1, padding= 2)
        self.conv2 = nn.Conv2d(in_channels= 6, out_channels= 16, kernel_size= 5, stride= 1)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.dropout = nn.Dropout(p=0.2)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.tanh(self.conv1(x))
        x = F.avg_pool2d(input= x, kernel_size= 2, stride= 2)
        x = F.tanh(self.conv2(x))
        x = F.avg_pool2d(input= x, kernel_size= 2, stride= 2)
        x = x.view(-1, 16*5*5)
        x = F.tanh(self.fc1(x))
        x = F.tanh(self.fc2(x))
        x = self.dropout(x)
        x = F.softmax(self.fc3(x))
        return x

# Adjusted LeNet-5 Model
class AdjustedLeNet5(nn.Module):
    
    def __init__(self):
        super(AdjustedLeNet5, self).__init__()
        # Image is padded to get an input size of 32x32
        self.conv1 = nn.Conv2d(in_channels= 1, out_channels= 6, kernel_size= 5, stride= 1, padding= 2)
        self.conv2 = nn.Conv2d(in_channels= 6, out_channels= 16, kernel_size= 5, stride= 1)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(input= x, kernel_size= 2, stride= 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(input= x, kernel_size= 2, stride= 2)
        x = x.view(-1, 16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x))
        return x