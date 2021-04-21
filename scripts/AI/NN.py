from torch import nn # Import neural network model
import torch.nn.functional as F

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
