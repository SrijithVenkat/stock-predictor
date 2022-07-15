import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


#Linear Model Class of Data
class LinearRegModel:
    def __init__(self, data) -> None:
        self.data = data
        self.bound = len(data)
        self.x = self.getX()
        self.y = self.getY()
        slope, intercept, r, p, std_err = stats.linregress(self.x, self.y)
        self.slope = slope
        self.intercept = intercept
        self.r_squared = r**2
        self.p = p
        self.error = std_err

    def getX(self):
        x_norm = np.arange(1,self.bound+1,1)
        return x_norm

    def getY(self):
        y = np.array(self.data)
        return y
    
    def predictXDays(self, x):
        return (self.slope * (self.bound+x)) + self.intercept

    def modelFunc(self, x):
        return (self.slope * x) + self.intercept

    def show(self):
        mymodel = list(map(self.modelFunc, self.x))
        plt.scatter(self.x, self.y)
        plt.plot(self.x, mymodel)
        plt.show()
