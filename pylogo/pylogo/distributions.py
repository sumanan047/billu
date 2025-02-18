"""Distributions in 2-D Space."""

import numpy as np
import matplotlib.pyplot as plt

class Distribution_1D:
    def __init__(self):
        self.data = None

    def __getitem__(self, index):
        return self.data[index]

    def normal(self, mean, std, size):
        self.data = np.random.normal(mean, std, size)

    def uniform(self, low, high, size):
        self.data = np.random.uniform(low, high, size)

    def exponential(self, scale, size):
        self.data = np.random.exponential(scale, size)

    def gamma(self, shape, scale, size):
        self.data = np.random.gamma(shape, scale, size)


class Distribution_2D:
    def __init__(self) -> None:
        self.x_arr = None
        self.y_arr = None

    def normal(self, mean, cov, size):
        x, y = np.random.multivariate_normal(mean, cov, size).T
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr
    
    def uniform(self, low, high, size):
        """Generates a bivariate uniform distribution.

        Args:
            low: The lower bounds for x and y (tuple or list).
            high: The upper bounds for x and y (tuple or list).
            size: The number of samples to generate.
        """
        x = np.random.uniform(low[0], high[0], size)
        y = np.random.uniform(low[1], high[1], size)
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr
    
    def exponential(self, scale, size):
        """
        Generate random numbers from an exponential distribution.

        Parameters:
        - scale (list of floats): The scale parameter of the exponential distribution.
        - size (list of ints): The shape of the output array.

        Returns:
        - x_arr (ndarray): Array of random numbers drawn from the exponential distribution.
        - y_arr (ndarray): Array of random numbers drawn from the exponential distribution.
        """
        assert isinstance(scale, list) and isinstance(size, list), "The scale parameter must be a list."
        assert size[0] == size[1], "The size of the output arrays must be the same."
        x = np.random.exponential(scale[0], size[0])
        y = np.random.exponential(scale[1], size[1])
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr
    
    def gamma(self, shape, scale, size):
        """
        Generate random numbers from a gamma distribution.

        Parameters:
        - shape (float): The shape parameter of the gamma distribution.
        - scale (float): The scale parameter of the gamma distribution.
        - size (int or tuple of ints): The size of the output array.

        Returns:
        - x_arr (ndarray): Array of random numbers drawn from the gamma distribution.
        - y_arr (ndarray): Array of random numbers drawn from the gamma distribution.
        """
        assert isinstance(shape, list) and isinstance(scale, list) and isinstance(size, list) , "The shape and scale parameters must be lists."
        assert size[0] == size[1], "The size of the output arrays must be the same."
        x = np.random.gamma(shape[0], scale[0], size[0])
        y = np.random.gamma(shape[0], scale[1], size[1])
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr