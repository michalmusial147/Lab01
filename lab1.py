import numpy as np
file = open('./dataset/dataset.npz', 'rb')
data = np.load(file)
train, test = data['train'], data['test']
print(type(train), type(test))
print(train.size, test.size)
print(train.shape, test.shape)
