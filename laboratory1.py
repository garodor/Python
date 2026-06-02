import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense

#массив с 1000 строками заполненные 3 рандоомными числами
X_train = np.random.uniform(-100, 100, (1000, 3))
y_train = X_train[:, 0] + X_train[:, 1] + X_train[:, 2] 

model = keras.Sequential()
model.add(Dense(units=1, input_shape=(3,),activation='linear'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

log = model.fit(X_train, y_train, epochs=1500, verbose=0)

plt.plot(log.history['loss'])   
plt.grid(True)
plt.show()

test_data = np.array([[5, 3, 2], [10, 20, 30], [1.5, 2.5, 3.0], [-5, 5, 0]])
predictions = model.predict(test_data, verbose=0)

for i in range(len(test_data)):
    a, b, c = test_data[i]
    true_sum = a + b + c
    pred_sum = predictions[i][0]
    print(f"{a} + {b} + {c} = {true_sum} (предсказание: {pred_sum})")


weights, bias = model.get_weights()
print(f"Найденные веса: {weights.flatten()}")
print(f"Найденное смещение (bias): {bias[0]}")