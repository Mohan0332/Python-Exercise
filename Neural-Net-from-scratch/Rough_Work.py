import numpy as np
#Rough work below

#Case 1: Normalizing without subtracting the max element
op = np.array([[1,2,3],[4,5,6],[7,8,9]])
op_exp1 = np.exp(op)
op_norm1 = op_exp1 / np.sum(op_exp1,axis=1,keepdims=True)

#Case 2: Normalizing after subtracting the highest element, thus the exponent is capped between (0,1) 

# Case 1 and Case 2 values after normalization are the same 
op_exp2 = np.exp(op - np.max(op,axis=1,keepdims=True))
op_norm2 = op_exp2/np.sum(op_exp2,axis=1,keepdims=True)
print(op_norm2)