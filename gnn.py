from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.layers import Dropout
from keras.layers import BatchNormalization
from keras.layers import Activation
from keras.layers import Concatenate
from keras.layers import AveragePooling1D
from keras.layers import GlobalMaxPooling1D
from keras.layers import GlobalAveragePooling1D
from keras.layers import Conv1D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
def GCN_block(inputs, feature_dims, activation):
    # Graph Convolution Layer
    outputs = Conv1D(feature_dims, 1, activation=None, use_bias=False)(inputs)
    outputs = BatchNormalization()(outputs)
    outputs = Activation(activation)(outputs)
    return outputs
# Define the input shape
data = pd.read_csv('./data.csv',delimiter=",")
#Seperating features and labels
X = np.array(data.iloc[: , :-1])
y = np.array(data.iloc[: , -1])
#print("y.unque",data['Class'].unique())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=np.random.seed(7))
x_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1],1))
x_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1],1)) 
inputs = Input(shape=([X_train.shape[0], X_train.shape[1],1]))
# Define the model architecture
x = GCN_block(inputs, 64, 'relu')
x = Dropout(0.5)(x)
x = GCN_block(x, 64, 'relu')
x = Dropout(0.5)(x)
outputs = GCN_block(x, 1, 'softmax')
# Define the model and compile it
model = Model(inputs=inputs, outputs=outputs)
optimizer = Adam(lr=0.01)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
# Train the model
hist=model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32)
#train and validation loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train','Validation'],loc='upper left')
plt.savefig('results/GNN Loss.png') 
plt.pause(5)
plt.show(block=False)
plt.close()

#train and validation accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train','Validation'],loc='upper left')
plt.savefig('results/GNN Accuracy.png') 
plt.pause(5)
plt.show(block=False)
plt.close()