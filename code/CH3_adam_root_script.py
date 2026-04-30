import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x - 2)**2

def grad(x):
    return 2 * (x - 2)

def adam_optimizer(x_start, lr=0.1, beta1=0.9, beta2=0.999, eps=1e-8, iterations=50):
    x = x_start
    m = 0
    v = 0
    history = [x]
    
    for t in range(1, iterations + 1):
        g = grad(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        history.append(x)
        
    return np.array(history)

# Run optimization
history = adam_optimizer(x_start=0.0)

# Visualization
x_vals = np.linspace(-1, 5, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), 'b-', label='$f(x) = (x-2)^2$')
plt.plot(history, f(history), 'ro-', markersize=4, alpha=0.6, label='Adam Path')
plt.scatter(history[-1], f(history[-1]), color='gold', marker='*', s=200, label='Minimum (2.0)', zorder=5)

plt.title('Adam Optimization: Minimizing $f(x) = (x-2)^2$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('CH3_adam_root_generated.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Final x: {history[-1]:.4f}")
print(f"Minimum value: {f(history[-1]):.4f}")
