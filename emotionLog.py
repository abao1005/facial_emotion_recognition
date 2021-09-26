from matplotlib import pyplot as plt
import pandas as pd
import sys

path = 'models2/emotion_training.log'
data = pd.read_csv(path)
acc = data['accuracy'].tolist()
loss = data['loss'].tolist()
val_acc = data['val_accuracy'].tolist()
val_loss = data['val_loss'].tolist()


fig = plt.figure()
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(acc, label = 'training acc')
plt.plot(val_acc, label = 'validation acc')
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.subplot(1,2,2)
plt.plot(loss,label = 'training loss')
plt.plot(val_loss,label = 'validation loss')
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()
fig.savefig('xception_epoch150-2.png')