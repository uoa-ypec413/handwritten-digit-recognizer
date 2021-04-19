from torchvision import datasets
from torch.utils import data


class Data():

    def importDataSet()
        # Import the MNIST Dataset from Torchvision.
        self.train_dataset = datasets.MNIST(root='mnist_data/',
                                        train=True,
                                        transform=transforms.ToTensor(),
                                        download=True)

        self.test_dataset = datasets.MNIST(root='mnist_data/',
                                        train=False,
                                        transform=transforms.ToTensor())

    def loadDataSet()
        # Data Loader (Input Pipeline)
        self.train_loader = data.DataLoader(dataset=train_dataset,
                                        batch_size=batch_size,
                                        shuffle=True)

        self.test_loader = data.DataLoader(dataset=test_dataset,
                                        batch_size=batch_size,
                                        shuffle=False)