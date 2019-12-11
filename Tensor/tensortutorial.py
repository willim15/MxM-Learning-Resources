from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


#HELPER FUNCTIONS
def plot_image(i, predictions_array, true_label, img):
	predictions_array, true_label, img = predictions_array, true_label[i], img[i]
	plt.grid(False)
	plt.xticks([])
	plt.yticks([])

	plt.imshow(img, cmap=plt.cm.binary)

	predicted_label = np.argmax(predictions_array)
	if predicted_label == true_label:
		color = 'blue'
	else:
		color = 'red'
	plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],100*np.max(predictions_array),class_names[true_label]), color=color)

def plot_value_array(i, predictions_array, true_label):
	predictions_array, true_label = predictions_array, true_label[i]
	plt.grid(False)
	plt.xticks(range(10))
	plt.yticks([])
	thisplot = plt.bar(range(10), predictions_array, color="#777777")
	plt.ylim([0, 1])
	predicted_label = np.argmax(predictions_array)

	thisplot[predicted_label].set_color('red')
	thisplot[true_label].set_color('blue')


#THIS IS HOW YOU LOAD THE DATA SET
#LOADING THEM BY PUTTING THE CLASS FASHION ITEM WITH A NUMBERED LABEL
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(test_images.shape)
print(test_labels)
print(len(test_labels))

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

#Verifying that the data is in the correct form
plt.figure(figsize=(10,10))
for i in range(25):
	plt.subplot(5,5,i+1)
	plt.xticks([])
	plt.yticks([])

	#plt.grid(True)
	plt.grid(False)
	plt.imshow(train_images[i], cmap=plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])
plt.show()

#Building the models
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),

    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#Compiling the Model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

'''
Sample Output:
60000/60000 [==============================] - 5s 85us/sample - loss: 0.4978 - accuracy: 0.8245
Epoch 2/10
60000/60000 [==============================] - 4s 69us/sample - loss: 0.3798 - accuracy: 0.8624
Epoch 3/10
60000/60000 [==============================] - 4s 62us/sample - loss: 0.3411 - accuracy: 0.8762
Epoch 4/10
60000/60000 [==============================] - 4s 61us/sample - loss: 0.3164 - accuracy: 0.8838
Epoch 5/10
60000/60000 [==============================] - 4s 61us/sample - loss: 0.2956 - accuracy: 0.8902
Epoch 6/10
60000/60000 [==============================] - 4s 64us/sample - loss: 0.2815 - accuracy: 0.8955
Epoch 7/10
60000/60000 [==============================] - 4s 65us/sample - loss: 0.2691 - accuracy: 0.9009
Epoch 8/10
60000/60000 [==============================] - 4s 62us/sample - loss: 0.2579 - accuracy: 0.9029
Epoch 9/10
60000/60000 [==============================] - 4s 63us/sample - loss: 0.2485 - accuracy: 0.9062
Epoch 10/10
60000/60000 [==============================] - 4s 60us/sample - loss: 0.2388 - accuracy: 0.9100
'''

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('Testing: ', test_acc)

predictions = model.predict(test_images)

i = 3
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
	plt.subplot(num_rows, 2*num_cols, 2*i+1)
	plot_image(i, predictions[i], test_labels, test_images)
	plt.subplot(num_rows, 2*num_cols, 2*i+2)
	plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

# Grab an image from the test dataset.
img = test_images[1]

print(img.shape)