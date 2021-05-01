# This is the script for the AI behind the handwritten digit recognizer program.

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
    progress_signal = pyqtSignal(int) # Signal for reporting progress of training, %
    status_signal = pyqtSignal(str) # Signal for reporting progress of training, text

    def __init__(self):
        super().__init__()
        self.data = Data() # Initialise data object

        # Training settings
        self.batch_size = 32
        self.device = 'cuda' if cuda.is_available() else 'cpu'
        self.create_model(AdjustedLeNet5) # Adjusted LeNet-5 is the default model type

    def create_model(self, model):
        self.model = model() # Initialise model object using given model type
        self.model.to(self.device)
        # Use cross entropy loss function
        self.criterion = nn.CrossEntropyLoss()
        # Try optimising with basic stochastic gradient descent setup first
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01, momentum=0.9)

    # Given a file path, load a model
    def load_model(self, file):
        self.model = load(file[0])
        self.model.eval()
    
    # Given a file path, save a model
    def save_model(self, file):
        save(self.model, file[0])

    # Train a model for a given epoch
    def train_network(self, epoch):
        self.model.train() # Puts the model into training mode
        for batch_idx, (data, target) in enumerate(self.data.train_loader): # iterate through the training dataset
            if self.run_flag == False: # End function if the cancel button has been pressed
                return

            data, target = data.to(self.device), target.to(self.device) # Use CUDA if available
            self.optimizer.zero_grad() # Set gradient to 0
            output = self.model(data) # Get predictions from model
            loss = self.criterion(output, target) # Find loss
            loss.backward() # Backwards propogation
            self.optimizer.step() # Optimisation function for learnign

            # Report progress every 10 batch indexes.
            if batch_idx % 10 == 0:
                portion_completed = 100. * batch_idx / len(self.data.train_loader)
                self.progress_signal.emit(int(portion_completed))
                print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(self.data.train_loader.dataset),
                    100. * batch_idx / len(self.data.train_loader), loss.item()))
        self.progress_signal.emit(100)

    # Test a model.
    def test(self):
        self.true_positives = [0,0,0,0,0,0,0,0,0,0] # Track true positives for each number
        self.false_positives = [0,0,0,0,0,0,0,0,0,0] # Track false positives for each number
        self.false_negatives = [0,0,0,0,0,0,0,0,0,0] # Track false negatives for each number
        self.total = [0,0,0,0,0,0,0,0,0,0] # Track total for each number
        self.precision = [0,0,0,0,0,0,0,0,0,0] # Track precision of each number
        self.recall = [0,0,0,0,0,0,0,0,0,0] # Track recall of each number

        self.model.eval() # Evaluation (testing) mode

        test_loss = 0
        correct = 0

        for data, target in self.data.test_loader: # Iterate through testing dataset
            if self.run_flag == False: # End function if cancel button has been pressed
                return
            data, target = data.to(self.device), target.to(self.device) # Use CUDA if available
            output = self.model(data) # Get predictions from the model
            test_loss += self.criterion(output, target).item() # sum up batch loss
            predictions = output.data.max(1, keepdim=True)[1] # get the index of the max to get prediction
            correct += predictions.eq(target.data.view_as(predictions)).cpu().sum() # get the number of correct guesses

            # get the number of true and false positives
            for i in range(len(predictions)):
                self.total[predictions[i]] += 1
                if predictions[i] == target[i]:
                    self.true_positives[predictions[i]] += 1                    
                else:
                    self.false_positives[predictions[i]] += 1
                    self.false_negatives[target[i]] += 1
        # calculate precision and recall rates for each number
        for i in range(10):
            if self.true_positives[i] == (self.true_positives[i] + self.false_positives[i]):
                self.precision[i] = 1
            else:
                self.precision[i] = self.true_positives[i]/(self.true_positives[i] + self.false_positives[i])
            self.recall[i] = self.true_positives[i]/(self.true_positives[i] + self.false_negatives[i])
        # find the overall precision, recall rate and f1 score
        precision_rate = sum(self.precision)/len(self.precision)
        recall_rate = sum(self.recall)/len(self.recall)
        f1_score = 2 * (precision_rate * recall_rate)/(precision_rate + recall_rate)
        # find the loss in test dataset, send accuracy to GUI
        test_loss /= len(self.data.test_loader.dataset)
        self.status_signal.emit(f'Accuracy: {(correct/len(self.data.test_loader.dataset)) * 100:.1f}%\n')
        print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(self.data.test_loader.dataset)} '
            f'({100. * correct / len(self.data.test_loader.dataset):.0f}%)')
        print(f'Precision Rate: {precision_rate}\nRecall Rate: {recall_rate}\n F1 Score: {f1_score}')

    def cancel_train_model(self):
        self.run_flag = False

    # this function runs a training reigime of 25 epochs, testing after each epoch.
    def train_model(self):
        since = time.time() # Get the time-stamp at the beginning of training
        self.run_flag = True
        for epoch in range(1, 26):
            if self.run_flag == False: # Stop training if cancelled
                break

            self.status_signal.emit(f'Training Epoch: {epoch} of 25\n') # Print to console
            epoch_start = time.time() # Get time-stamp at beginning of epoch
            self.train_network(epoch) # Train for one epoch
            m, s = divmod(time.time() - epoch_start, 60) # Find time since beginning of epoch
            print(f'Training time: {m:.0f}m {s:.0f}s')
            self.test() # Test the model at the end of each epoch
            m, s = divmod(time.time() - epoch_start, 60)
            print(f'Testing time: {m:.0f}m {s:.0f}s')

        if self.run_flag == False: # If cancelled, echo this to console
            print('Cancelled training')
            self.status_signal.emit('Cancelled training\n')
            self.progress_signal.emit(0)
        else:
            m, s = divmod(time.time() - since, 60)
            print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {self.device}!')

    def recognise_user_digit(self):
        image = io.read_image('user_data/digit_drawing.jpg')
        # Put into format expected by model
        image = transforms.functional.invert(image) / 255
        user_input_process = transforms.Compose([transforms.Grayscale(), transforms.Resize((28, 28))])
        image = user_input_process(image)
        image = image.unsqueeze(0) # Add empty dimension
        # Get prediction from model
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
        return output[0] # Return list of probabilities
