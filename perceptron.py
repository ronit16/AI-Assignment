import numpy as np

class Percepton:
    def __init__(self, learning_rate=0.01, n_iters=10):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)

# Example usage
if __name__ == "__main__":
    # perform AND and Or operation using perceptron
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])

    p = Percepton(learning_rate=0.01, n_iters=5)
    p.fit(X, y)
    print(p.predict(X))
    print(p.weights, p.bias)

    # perform OR operation
    y = np.array([0, 1, 1, 1])
    p = Percepton(learning_rate=0.01, n_iters=3)
    p.fit(X, y)
    print(p.predict(X))
    print(p.weights, p.bias)
