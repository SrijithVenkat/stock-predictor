import numpy as np
import matplotlib.pyplot as plt


#Polynomial Model Class of Data
class PolyRegModel:
    def __init__(self, data) -> None:
        self.data = data
        self.bound = len(data)
        self.x = self.getX()
        self.y = self.getY()
        self.model = np.poly1d(np.polyfit(self.x, self.y, 3))
        self.polyline = np.linspace(1, self.bound+1, 100)

    
    def getX(self):
        x_norm = np.arange(1,self.bound+1,1)
        return x_norm

    def getY(self):
        y = np.array(self.data)
        return y
    
    def predictXDays(self, x):
        return self.model(self.bound+x)

    def modelFunc(self, x):
        return self.model(x)

    def show(self):
        plt.scatter(self.x, self.y)
        plt.plot(self.polyline, self.model(self.polyline))
        plt.show()
