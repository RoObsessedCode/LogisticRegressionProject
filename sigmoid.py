import numpy as np
from exam import calculated_log_odds

def sigmoid(z):
  denominator = 1 + np.exp(-z)
  return 1 / denominator 


probabilities = sigmoid(calculated_log_odds)
print(probabilities)
