# This is the script for the AI behind the handwritten digit recognizer program.
# Current version is 1.0.1, most recent change 1.0.0-->1.0.1: Add header.
# Model is 2-layer 784-->392, 392-->10
# Relu function is applied after the first layer

# Include relevant libraries
from __future__ import print_function # Allows us to do fancier print statements
from torch import nn, optim, cuda, save, load # Import neural network model and some optimization libraries
import time # Lets us timestamp things nicely, makes working with time units simpler
from AI.NN import Net
from AI.Data import Data

class DigitRecogniser():
    def __init__(self):
        self.data = Data()
        # Training settings
        self.batch_size = 32
        self.device = 'cuda' if cuda.is_available() else 'cpu'
        self.create_model()

    def create_model(self):
        self.model = Net()
        self.model.to(self.device)
        # Use cross entropy loss function
        self.criterion = nn.CrossEntropyLoss()
        # Try optimising with basic stochastic gradient descent setup first
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01, momentum=0.9)

    def load_model(self):
        self.model.load_state_dict(load('trained_models/trained.pth'))

    def train_network(self, epoch):
        self.model.train() # Puts the model into training mode
        for batch_idx, (data, target) in enumerate(self.data.train_loader): # iterate through the training dataset
            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()
            if batch_idx % 10 == 0:
                print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(self.data.train_loader.dataset),
                    100. * batch_idx / len(self.data.train_loader), loss.item()))

    def test(self):
        self.model.eval()
        self.test_loss = 0
        self.correct = 0
        for data, target in self.data.test_loader:
            data, target = data.to(self.device), target.to(self.device)
            output = self.model(data)
            # sum up batch loss
            test_loss += criterion(output, target).item()
            # get the index of the max
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

        test_loss /= len(test_loader.dataset)
        print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} '
            f'({100. * correct / len(test_loader.dataset):.0f}%)')

    def train_model(self):
        since = time.time()
        for epoch in range(1, 10):
            epoch_start = time.time()
            train_network(epoch)
            m, s = divmod(time.time() - epoch_start, 60)
            print(f'Training time: {m:.0f}m {s:.0f}s')
            test()
            m, s = divmod(time.time() - epoch_start, 60)
            print(f'Testing time: {m:.0f}m {s:.0f}s')

        m, s = divmod(time.time() - since, 60)
        print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {self.device}!')

    def save_model(self):
        save(self.model.state_dict(), 'trained_models/trained.pth')
        print('Model saved')