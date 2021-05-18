from tpdataset import RawDataSet, DataDownloader
from torchvision import datasets
from torchvision import transforms
from pyctlib import vector
import math
import torch

class MINIST:

    def __init__(self, root="", transform="default"):

        root = path(root)

        if isinstance(transform, str) and transform == "default":
            self.trans = transforms.ToTensor()
        else:
            self.trans = transform

        self.train_set = vector(datasets.MNIST(root=root, train=True, transform=self.trans,download=True), str_function=lambda x: "\n".join(["Dataset MNIST", "    Number of datapoints: {}".format(x.length), "    Split: Train"]))
        self.test_set = datasets.MNIST(root=root, train=False, transform=trans, download=False, str_function=lambda x: "\n".join(["Dataset MNIST", "    Number of datapoints: {}".format(x.length), "    Split: Test"]))

    def show_image(self, image, y_labels=None):

        import matplotlib.pyplot as plt
        if image.dim() == 2 or image.shape[0] == 1:
            image = image.squeeze()
            plt.imshow(image, cmap="gray", interpolation=None)
            if y_labels is not None:
                plt.title("Ground Truth: {}".format(y_labels))
            plt.xticks([])
            plt.yticks([])
            plt.show()
        else:
            n = image.shape[0]
            if n > 100:
                raise RuntimeError("{} images are displaied simutaneously".format(n))
            width = math.ceil(math.sqrt(n))
            for index in range(n):
                plt.subplot(index // width, index % width, index + 1)
                plt.tight_layout()
                plt.imshow(image[index, :, :], cmap="gray", interpolation=None)
                if y_labels is not None:
                    plt.title("Ground Truth: {}".format(y_labels[index]))
                plt.xticks([])
                plt.yticks()
            plt.show()
