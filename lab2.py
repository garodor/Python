import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

(x_train_full, y_train_full), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_full = x_train_full.astype('float32') / 255
x_test = x_test.astype('float32') / 255

y_train_full_cat = to_categorical(y_train_full, 10)
y_test_cat = to_categorical(y_test, 10)

indices_20k = np.random.choice(60000, 20000, replace=False)
x_train_20k = x_train_full[indices_20k]
y_train_20k_cat = y_train_full_cat[indices_20k]

print(f"Сокращённая обучающая выборка: {x_train_20k.shape[0]} изображений")

def create_model():
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28)))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return model

model_full = create_model()
history_full = model_full.fit(x_train_full, y_train_full_cat, validation_split=0.1, epochs=20, batch_size=128, verbose=1)
test_loss_full, test_acc_full = model_full.evaluate(x_test, y_test_cat, verbose=0)

model_20k = create_model()
history_20k = model_20k.fit(x_train_20k, y_train_20k_cat, validation_split=0.1, epochs=20, batch_size=128,verbose=1)
test_loss_20k, test_acc_20k = model_20k.evaluate(x_test, y_test_cat, verbose=0)

#График потерь
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(history_full.history['loss'], 'b-', label='Полная (обучение)', linewidth=2)
plt.plot(history_full.history['val_loss'], 'b--', label='Полная (валидация)', linewidth=2)
plt.plot(history_20k.history['loss'], 'r-', label='20k (обучение)', linewidth=2)
plt.plot(history_20k.history['val_loss'], 'r--', label='20k (валидация)', linewidth=2)
plt.xlabel('Эпоха')
plt.ylabel('Потери')
plt.title('Сравнение функции потерь')
plt.legend()
plt.grid(True, alpha=0.3)

#График точности
plt.subplot(1, 3, 2)
plt.plot(history_full.history['accuracy'], 'b-', label='Полная (обучение)', linewidth=2)
plt.plot(history_full.history['val_accuracy'], 'b--', label='Полная (валидация)', linewidth=2)
plt.plot(history_20k.history['accuracy'], 'r-', label='20k (обучение)', linewidth=2)
plt.plot(history_20k.history['val_accuracy'], 'r--', label='20k (валидация)', linewidth=2)
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.title('Сравнение точности')
plt.legend()
plt.grid(True, alpha=0.3)

#Диаграмма сравнения
plt.subplot(1, 3, 3)
accuracies = [test_acc_full*100, test_acc_20k*100]
colors = ['blue', 'red']
bars = plt.bar(['Полная (60000)', 'Сокращённая (20000)'], accuracies, color=colors)
plt.ylabel('Точность %')
plt.title('Сравнение точности на тестовой выборке')
plt.ylim(90, 100)


plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print(f"Точность на полной выборке (60000): {test_acc_full*100:.2f}%")
print(f"Точность на сокращённой выборке (20000): {test_acc_20k*100:.2f}%")
print(f"Разница в точности:{(test_acc_full - test_acc_20k)*100:.2f}%")

