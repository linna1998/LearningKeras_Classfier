# Learn Keras Classfier from https://morvanzhou.github.io/tutorials/machine-learning/keras/2-2-classifier/
# Linna 2017.11.1
import numpy as np
np.random.seed(1337)  # Reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential  # Build the neural network
from keras.layers import Dense, Activation  # Activation: encouraging function
from keras.optimizers import RMSprop  

# Download the minst dataset to the path '~./keras/datasets' if it's the first time being called
# X shape (60,000 28*28), Y shape (10,000 )
print('Data downloading------')
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Data pre-processing
# Normalize
print('Data pre-processing------')
X_train = X_train.reshape(X_train.shape[0],-1)/225.  
X_test = X_test.reshape(X_test.shape[0],-1)/225.
Y_train = np_utils.to_categorical(Y_train, num_classes=10)  
Y_test = np_utils.to_categorical(Y_test, num_classes=10)

print(X_train[1].shape)

print(Y_train[:3])

# Build the neural network
model = Sequential([
    Dense(32,input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    ])

# Define the optimizer
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# Activate the model
model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
print('Training------')
model.fit(X_train, Y_train, epochs=2, batch_size=32)

print('\nTesting------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, Y_test)

print('test loss:', loss)
print('test accuracy:', accuracy)


