import random
import numpy as np


# Each of the 784 pixels
input = [0] * 784

# Digits from 0-9
output = [ [] * 16 ] * 10

# Hidden layers
f1 = [ [0] * 784 ] * 16
f2 = [ [0] * 16 ] * 16

