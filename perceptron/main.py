import tensorflow.contrib.tensorrt as trt
import tflearn
from tflearn import DNN
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

"""
    Steps
    1. preparacion de datos de entrada
    2. definicion de la estructura para aprender los datos
    3. entrenamiento de la estructura definida
    4. Comprobacion de que la estructura ha aprendido correctamente
"""

# entradas de la red neuronal
# XOR logical function
X = [[0,0], [0,1],[1,0], [1,1]] # entradas
Y = [[0],   [1],  [1],   [0]]           # salidas esperadas
"""
AND 
Y = [[0], [0], [0], [1]] salidas esperadas

OR
Y = [[0], [1], [1], [1]] salidas esperadas
"""

# definir la estructura de la red neuronal


input_layer = input_data(shape=[None, 2])
"""
shape=[None, 2] siginifica que la red con el None se podra entrenar
con cualquier numero de ejemplos y el menciona que los
parametros de entrada van a ser 2
"""
hidden_layer = fully_connected( input_layer, 2, activation='tanh') # tanh es tangente hipervolica 
output_layer = fully_connected(hidden_layer, 1, activation='tanh') # tanh es tangente hipervolica

# se define el tipo de algoritmo para llevar el aprendizaje
regression = regression(output_layer, optimizer='sgd', loss='binary_crossentropy', learning_rate=5)

model = DNN(regression)
# entrenamiento del sistema 
model.fit( X, Y, n_epoch=5000, show_metric=True )
"""
model.filt ( entradas, salidas, iteration, mostrar metricas )
accuracy la precicion de la red neuronal
si el accuracy no cambia o esta arriba del 0.9
!la red no esta aprendiendo! 
"""
print("salida aprendida:", [i[0] > 0 for i in Y])
print("salida recordada:", [i[0] > 0 for i in model.predict(X)])