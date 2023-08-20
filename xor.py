# Training a perceptron to learn the XOR function - use gradient-based learning

import numpy as np

x_train = [ [0,1], [0,0], [1,0], [1,1] ]
x_labels = [1,0,1,0]

inputL = [0] * 2
hiddenL1 = [[0,0]] * 2
output = 0

