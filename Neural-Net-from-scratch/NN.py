#This file aims to create a basic Neural Network from scratch.
import numpy as np

class LayerDense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros(1,n_neurons)
    
    def forward_propagation(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_Relu:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs) #using maximum to compare elementwise

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs-np.max(inputs,axis=1,keepdims=True))
        normalised_values = exp_values/np.sum(exp_values,axis=1)
        self.output = normalised_values



    


