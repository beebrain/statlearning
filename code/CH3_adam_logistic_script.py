import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-5, 5, 20).reshape(-1, 1)
# Add intercept
X_aug = np.hstack([np.ones((X.shape[0], 1)), X])
true_beta = np.array([-1, 2])
prob = 1 / (1 + np.exp(-X_aug @ true_beta))
y = (np.random.rand(20) < prob).astype(float)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_loss(y, p):
    return -np.mean(y * np.log(p + 1e-15) + (1 - y) * np.log(1 - p + 1e-15))

def adam_logistic(X, y, lr=0.1, iterations=200):
    n_samples, n_features = X.shape
    beta = np.zeros(n_features)
    m = np.zeros(n_features)
    v = np.zeros(n_features)
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    loss_history = []
    
    for t in range(1, iterations + 1):
        p = sigmoid(X @ beta)
        loss = compute_loss(y, p)
        loss_history.append(loss)
        
        # Gradient of Negative Log-Likelihood
        g = X.T @ (p - y) / n_samples
        
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        beta = beta - lr * m_hat / (np.sqrt(v_hat) + eps)
        
    return beta, loss_history

# Run optimization
beta_opt, losses = adam_logistic(X_aug, y)

# Visualization
plt.figure(figsize=(12, 5))

# Plot 1: Sigmoid Fit
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='red', label='Data Points')
X_test = np.linspace(-6, 6, 100).reshape(-1, 1)
X_test_aug = np.hstack([np.ones((100, 1)), X_test])
plt.plot(X_test, sigmoid(X_test_aug @ beta_opt), 'b-', label='Adam Sigmoid Fit')
plt.title('Logistic Regression with Adam')
plt.xlabel('x')
plt.ylabel('P(y=1)')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Loss Curve
plt.subplot(1, 2, 2)
plt.plot(losses, 'g-')
plt.title('Loss Curve (Negative Log-Likelihood)')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('CH3_adam_logistic_generated.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Estimated Coefficients: {beta_opt}")
