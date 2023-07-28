import random
import numpy as np
import tf as tf
import keras

#tf.keras.datasets.mnist.load_data(path="mnist.npz")


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)

# Each of the 784 pixels
input = [0] * 784

# Digits from 0-9
output = [ [] * 16 ] * 10

# Hidden layers
f1 = [ [0] * 784 ] * 16
f2 = [ [0] * 16 ] * 16

print(x_train[1])
