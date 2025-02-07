import numpy as np
import matplotlib.pyplot as plt

class Distribution:
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

if __name__ == "__main__":
    d1 = Distribution()
    d2 = Distribution()
    d1.normal(mean=[1.0, 0.0],
                cov=[[0,0.5], [0.5,0]], size=1000)
    d2.uniform(low=[0,0], high=[1,2], size=1000)
    plt.scatter(d1.x_arr, d1.y_arr, color = "red")
    plt.scatter(d2.x_arr, d2.y_arr, color = "blue")
    plt.show()