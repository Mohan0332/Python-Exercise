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

class Loss:
    def calculate(self,output,y):
        sample_losses = self.forward(output,y)
        mean_loss = np.mean(sample_losses)
        return mean_loss

class Loss_CategoricalCrossEntropy(Loss):
    def forward(self,y_pred,y_true):
        n_samples = len(y_pred)

        # If y_true is not one-hot encoded
        if len(y_true.shape) == 1: 
            correct_confidences = y_pred[range(n_samples),y_true]

        # If y_true is one-hot encoded
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred * y_true,axis=1)
        
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods



    


