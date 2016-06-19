import numpy as np
from network import NeuralNetwork
from trainer import Trainer
from csv import reader
from datetime import datetime
    
# Squares data
x = np.array([[i] for i in range(1,76)], dtype=float)
y = np.array([[i**2] for i in range(1,76)], dtype=float)

# Calculate to display data later
ymax = np.amax(y, axis=0)

# Normalize
x = x/np.amax(x, axis=0)
y = y/ymax


N = NeuralNetwork(1, 5, 1)
T = Trainer(N)
T.train(x, y)
testX = np.array([[i] for i in range(76,101)], dtype=float)
testY = np.array([[i**2] for i in range(76,101)], dtype=float)

# Normalize training data
testX /= np.amax(testX, axis=0)
testYMax = np.amax(testY, axis=0)
testY /= testYMax

yHat = N.forward(testX)

for i in range(len(yHat)):
    print testY[i]*testYMax, yHat[i]*testYMax
