import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Weights initialization with bias terms
        self.weights1 = np.random.randn(2, 4) * np.sqrt(1.0 / 2)
        self.bias1 = np.zeros((1, 4))
        self.weights2 = np.random.randn(4, 1) * np.sqrt(1.0 / 4)
        self.bias2 = np.zeros((1, 1))
        self.learning_rate = 0.1
        self.momentum = 0.9
        
        # Previous weight changes for momentum
        self.prev_weight1_change = np.zeros_like(self.weights1)
        self.prev_weight2_change = np.zeros_like(self.weights2)
        self.prev_bias1_change = np.zeros_like(self.bias1)
        self.prev_bias2_change = np.zeros_like(self.bias2)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        self.hidden = self.sigmoid(np.dot(X, self.weights1) + self.bias1)
        self.output = self.sigmoid(np.dot(self.hidden, self.weights2) + self.bias2)
        return self.output

    def backward(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = np.dot(output_delta, self.weights2.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden)

        # Calculate weight changes with momentum
        weight2_change = (self.learning_rate * np.dot(self.hidden.T, output_delta) + 
                         self.momentum * self.prev_weight2_change)
        bias2_change = (self.learning_rate * np.sum(output_delta, axis=0, keepdims=True) + 
                       self.momentum * self.prev_bias2_change)
        
        weight1_change = (self.learning_rate * np.dot(X.T, hidden_delta) + 
                         self.momentum * self.prev_weight1_change)
        bias1_change = (self.learning_rate * np.sum(hidden_delta, axis=0, keepdims=True) + 
                       self.momentum * self.prev_bias1_change)

        # Update weights and biases
        self.weights2 += weight2_change
        self.bias2 += bias2_change
        self.weights1 += weight1_change
        self.bias1 += bias1_change

        # Store changes for next iteration
        self.prev_weight2_change = weight2_change
        self.prev_bias2_change = bias2_change
        self.prev_weight1_change = weight1_change
        self.prev_bias1_change = bias1_change

    def train(self, X, y, epochs):
        for _ in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)

# Training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Train network
nn = NeuralNetwork()
nn.train(X, y, epochs=10000)

# Test
print("\nTest Results:")
for pattern, target in zip(X, y):
    pred = nn.forward(pattern.reshape(1, -1))
    print(f"Pattern: {pattern}, Target: {target[0]}, Prediction: {pred[0][0]:.3f}")