from torchvision import datasets, transforms
from torch.utils import data


class Data():

    def import_dataset(self):
        # Import the MNIST Dataset from Torchvision.
        print('Downloading train dataset')
        self.train_dataset = datasets.MNIST(root='mnist_data/',
                                        train=True,
                                        transform=transforms.ToTensor(),
                                        download=True)
        print('Downloading test dataset')
        self.test_dataset = datasets.MNIST(root='mnist_data/',
                                        train=False,
                                        transform=transforms.ToTensor())
        print('Finished donwloading both datasets')
    def load_dataset(self, batch_size):
        # Data Loader (Input Pipeline)
        self.train_loader = data.DataLoader(dataset=self.train_dataset,
                                        batch_size=batch_size,
                                        shuffle=True)

        self.test_loader = data.DataLoader(dataset=self.test_dataset,
                                        batch_size=batch_size,
                                        shuffle=False)