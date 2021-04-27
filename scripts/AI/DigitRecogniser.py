# This is the script for the AI behind the handwritten digit recognizer program.
# Current version is 1.0.1, most recent change 1.0.0-->1.0.1: Add header.
# Model is 2-layer 784-->392, 392-->10
# Relu function is applied after the first layer

# Include relevant libraries
from __future__ import print_function # Allows us to do fancier print statements
from torch import nn, optim, cuda, save, load # Import neural network model and some optimization libraries
import time # Lets us timestamp things nicely, makes working with time units simpler
from AI.NN import *
from AI.Data import Data
from PyQt5.QtCore import pyqtSignal, QObject
from torchvision import transforms, io
import torch.nn.functional as F

class DigitRecogniser(QObject):
    progress_signal = pyqtSignal(int)
    status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.data = Data()
        # Training settings
        self.batch_size = 32
        self.device = 'cuda' if cuda.is_available() else 'cpu'
        self.create_model(AdjustedLeNet5)

    def create_model(self, model):
        self.model = model()
        self.model.to(self.device)
        # Use cross entropy loss function
        self.criterion = nn.CrossEntropyLoss()
        # Try optimising with basic stochastic gradient descent setup first
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.005, momentum=0.9)

    def load_model(self, file):
        self.model = load(file[0])
        self.model.eval()
    
    def save_model(self, file):
        save(self.model, file[0])

    def train_network(self, epoch):
        self.model.train() # Puts the model into training mode
        for batch_idx, (data, target) in enumerate(self.data.train_loader): # iterate through the training dataset
            if self.run_flag == False:
                return

            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

            if batch_idx % 10 == 0:
                portion_completed = 100. * batch_idx / len(self.data.train_loader)
                self.progress_signal.emit(int(portion_completed))
                print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(self.data.train_loader.dataset),
                    100. * batch_idx / len(self.data.train_loader), loss.item()))
        self.progress_signal.emit(100)

    def test(self):
        self.model.eval()
        test_loss = 0
        correct = 0
        for data, target in self.data.test_loader:
            if self.run_flag == False:
                return
            data, target = data.to(self.device), target.to(self.device)
            output = self.model(data)
            # sum up batch loss
            test_loss += self.criterion(output, target).item()
            # get the index of the max
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

        test_loss /= len(self.data.test_loader.dataset)
        self.status_signal.emit(f'Accuracy: {(correct/len(self.data.test_loader.dataset)) * 100:.1f}%\n')
        print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(self.data.test_loader.dataset)} '
            f'({100. * correct / len(self.data.test_loader.dataset):.0f}%)')

    def cancel_train_model(self):
        self.run_flag = False

    def train_model(self):
        since = time.time()
        self.run_flag = True
        for epoch in range(1, 26):
            if self.run_flag == False:
                break

            self.status_signal.emit(f'Training Epoch: {epoch} of 25\n')
            epoch_start = time.time()
            self.train_network(epoch)
            m, s = divmod(time.time() - epoch_start, 60)
            print(f'Training time: {m:.0f}m {s:.0f}s')
            self.test()
            m, s = divmod(time.time() - epoch_start, 60)
            print(f'Testing time: {m:.0f}m {s:.0f}s')

        if self.run_flag == False:
            print('Cancelled training')
            self.status_signal.emit('Cancelled training\n')
            self.progress_signal.emit(0)
        else:
            m, s = divmod(time.time() - since, 60)
            print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {self.device}!')

    def recognise_user_digit(self):
        image = io.read_image('user_data/digit_drawing.jpg')
        image = transforms.functional.invert(image) / 255
        user_input_process = transforms.Compose([transforms.Grayscale(), transforms.Resize((28, 28))])
        image = user_input_process(image)
        image = image.unsqueeze(0)
        output = self.model(image)
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
        return output[0]
