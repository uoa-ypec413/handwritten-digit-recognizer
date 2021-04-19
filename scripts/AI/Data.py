from torchvision import datasets, transforms
from torch.utils import data


class Data():

    def import_train_dataset(self):
        # Import the MNIST Train Dataset from Torchvision.
        self.train_dataset = datasets.MNIST(root='mnist_data/',
                                        train=True,
                                        transform=transforms.ToTensor(),
                                        download=True)

    def import_test_dataset(self):
        # Import the MNIST Test Dataset from Torchvision.
        self.test_dataset = datasets.MNIST(root='mnist_data/',
                                        train=False,
                                        transform=transforms.ToTensor())

    def load_dataset(self, batch_size):
        # Data Loader (Input Pipeline)
        self.train_loader = data.DataLoader(dataset=self.train_dataset,
                                        batch_size=batch_size,
                                        shuffle=True)

        self.test_loader = data.DataLoader(dataset=self.test_dataset,
                                        batch_size=batch_size,
                                        shuffle=False)