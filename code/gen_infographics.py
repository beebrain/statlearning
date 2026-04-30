import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_composite_infographic(filename, code_text, plot_func, output_path):
    # Set up the figure
    fig = plt.figure(figsize=(10, 14), facecolor='white')
    
    # 1. Header (Gray bar)
    header_height = 0.05
    header_ax = fig.add_axes([0.05, 0.9, 0.9, header_height], facecolor='#666666')
    header_ax.text(0.05, 0.5, filename, color='white', fontsize=14, weight='bold', va='center', ha='left')
    header_ax.set_xticks([])
    header_ax.set_yticks([])
    for spine in header_ax.spines.values():
        spine.set_visible(False)
    
    # 2. Code Block (Yellow background)
    code_height = 0.45
    code_ax = fig.add_axes([0.05, 0.45, 0.9, code_height], facecolor='#FFFBE6') # Light yellow
    code_ax.text(0.02, 0.95, code_text, transform=code_ax.transAxes, 
                fontsize=11, fontfamily='monospace', va='top', ha='left', color='#333333')
    code_ax.set_xticks([])
    code_ax.set_yticks([])
    for spine in code_ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#CCCCCC')
    
    # 3. Plot Area
    plot_ax = fig.add_axes([0.1, 0.05, 0.8, 0.35])
    plot_func(plot_ax)
    
    # Outer Border
    rect = patches.Rectangle((0.01, 0.01), 0.98, 0.98, linewidth=1, edgecolor='#999999', facecolor='none', transform=fig.transFigure)
    fig.patches.append(rect)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

# --- Adam Root Finding content ---
def plot_adam_root(ax):
    def f(x): return (x - 2)**2
    def grad(x): return 2 * (x - 2)
    
    x = 0.0
    m, v = 0, 0
    lr, b1, b2, eps = 0.2, 0.9, 0.999, 1e-8
    history = [x]
    for t in range(1, 41):
        g = grad(x)
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * (g**2)
        m_h = m / (1 - b1**t)
        v_h = v / (1 - b2**t)
        x = x - lr * m_h / (np.sqrt(v_h) + eps)
        history.append(x)
    
    x_vals = np.linspace(-0.5, 4.5, 400)
    ax.plot(x_vals, f(x_vals), color='#00a08a', linewidth=2, label='$f(x) = (x-2)^2$')
    hist_x = np.array(history)
    ax.plot(hist_x, f(hist_x), 'ro-', markersize=4, alpha=0.5, label='Adam Optimization Path')
    ax.scatter(hist_x[-1], f(hist_x[-1]), color='orange', marker='*', s=150, zorder=5, label='Minimum at x=2.0')
    ax.set_title('Adam Optimization Result (Minimization)', fontsize=12, weight='bold')
    ax.set_xlabel('Parameter x')
    ax.set_ylabel('Objective Value f(x)')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=9)

adam_root_code = """
import numpy as np

# Objective function and its gradient
def f(x): return (x - 2)**2
def grad(x): return 2 * (x - 2)

# Adam Optimizer
def adam_minimize(f, grad, x_start, lr=0.1):
    x = x_start
    m, v = 0, 0
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    
    for t in range(1, 101):
        g = grad(x)
        
        # Update biased first moment
        m = beta1 * m + (1 - beta1) * g
        # Update biased second raw moment
        v = beta2 * v + (1 - beta2) * (g**2)
        
        # Compute bias-corrected moments
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        # Update parameter
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        
    return x

# Execute
min_x = adam_minimize(f, grad, x_start=0.0)
print(f"Optimal x: {min_x}")
"""

# --- Adam Logistic content ---
def plot_adam_logistic(ax):
    np.random.seed(42)
    X = np.linspace(-5, 5, 20).reshape(-1, 1)
    X_aug = np.hstack([np.ones((X.shape[0], 1)), X])
    y = (np.random.rand(20) < (1 / (1 + np.exp(-(X.flatten()*1.5 - 1))))).astype(float)
    
    def sigmoid(z): return 1 / (1 + np.exp(-z))
    
    beta = np.zeros(2)
    m, v = np.zeros(2), np.zeros(2)
    lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
    for t in range(1, 201):
        p = sigmoid(X_aug @ beta)
        g = X_aug.T @ (p - y) / 20
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * (g**2)
        m_h = m / (1 - b1**t)
        v_h = v / (1 - b2**t)
        beta = beta - lr * m_h / (np.sqrt(v_h) + eps)
    
    ax.scatter(X, y, color='black', s=20, label='Observations (0/1)')
    X_line = np.linspace(-6, 6, 100).reshape(-1, 1)
    p_line = sigmoid(np.hstack([np.ones((100, 1)), X_line]) @ beta)
    ax.plot(X_line, p_line, color='#00a08a', linewidth=2.5, label='Fitted Sigmoid (Adam)')
    ax.axhline(0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.set_title('Logistic Regression Optimization Result', fontsize=12, weight='bold')
    ax.set_xlabel('Feature (x)')
    ax.set_ylabel('Probability P(Y=1)')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=9)

adam_logistic_code = """
import numpy as np

# Generate data
X = np.linspace(-5, 5, 20).reshape(-1, 1)
X_aug = np.hstack([np.ones((20, 1)), X])
y = (np.random.rand(20) < 1/(1+np.exp(-(X.flatten()*1.5-1)))).astype(float)

def sigmoid(z): return 1 / (1 + np.exp(-z))

# Adam for Logistic Regression
def logistic_adam(X, y, iterations=100, lr=0.1):
    n_samples, n_features = X.shape
    beta = np.zeros(n_features)
    m, v = np.zeros(n_features), np.zeros(n_features)
    b1, b2, eps = 0.9, 0.999, 1e-8
    
    for t in range(1, iterations + 1):
        p = sigmoid(np.dot(X, beta))
        grad = np.dot(X.T, (p - y)) / n_samples
        
        m = b1 * m + (1 - b1) * grad
        v = b2 * v + (1 - b2) * (grad**2)
        
        m_hat = m / (1 - b1**t)
        v_hat = v / (1 - b2**t)
        
        beta -= lr * m_hat / (np.sqrt(v_hat) + eps)
    return beta

# Fit model
beta_hat = logistic_adam(X_aug, y)
"""

# Generate images
create_composite_infographic('adam_root.py', adam_root_code, plot_adam_root, 'CH3_adam_root.png')
create_composite_infographic('adam_logistic.py', adam_logistic_code, plot_adam_logistic, 'CH3_adam_logistic.png')

print("Infographics generated successfully.")
