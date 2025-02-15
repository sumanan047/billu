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
        - scale (float): The scale parameter of the exponential distribution.
        - size (int or tuple of ints): The shape of the output array.

        Returns:
        - x_arr (ndarray): Array of random numbers drawn from the exponential distribution.
        - y_arr (ndarray): Array of random numbers drawn from the exponential distribution.
        """
        x = np.random.exponential(scale, size)
        y = np.random.exponential(scale, size)
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr
    
    def gamma(self, shape, scale, size):
        """Generate random numbers from a gamma distribution.
        
        This method generates random numbers from a gamma distribution with the given shape and scale parameters.
        
        Parameters:
        shape (float): The shape parameter of the gamma distribution.
        scale (float): The scale parameter of the gamma distribution.
        size (int or tuple of ints): The size of the output array.
        
        Returns:
        tuple: A tuple containing two arrays of random numbers drawn from the gamma distribution.
        """
        x = np.random.gamma(shape, scale, size)
        y = np.random.gamma(shape, scale, size)
        self.x_arr = x
        self.y_arr = y
        return self.x_arr, self.y_arr


if __name__ == "__main__":
    d1 = Distribution_2D()
    d2 = Distribution_2D()
    d3 = Distribution_2D()
    d4 = Distribution_2D()
    d1.normal(mean=[1.0, 0.0],
                cov=[[0,0.5], [0.5,0]], size=1000)
    d2.uniform(low=[0,0], high=[1,2], size=1000)
    d3.exponential(scale=1, size=1000)
    d4.gamma(shape=2, scale=1, size=1000)
    # plt.scatter(d1.x_arr, d1.y_arr, color = "red")
    # plt.scatter(d2.x_arr, d2.y_arr, color = "blue")
    # plt.scatter(d3.x_arr, d3.y_arr, color = "green")
    # plt.scatter(d4.x_arr, d4.y_arr, color = "yellow")
    #plot headtmaps instead
    plt.hist2d(d4.x_arr, d4.y_arr, bins=50, cmap='hot')
    plt.colorbar()
    plt.show()
    plt.show()  