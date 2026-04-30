import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def adam_logistic_regression(X, y, alpha=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, iterations=2000):
    m, n = X.shape
    X_bias = np.c_[np.ones(m), X]
    theta = np.zeros(n + 1)
    m_t = np.zeros(n + 1)
    v_t = np.zeros(n + 1)
    loss_history = []
    
    for t in range(1, iterations + 1):
        z = np.dot(X_bias, theta)
        h = sigmoid(z)
        gradient = np.dot(X_bias.T, (h - y)) / m
        m_t = beta1 * m_t + (1 - beta1) * gradient
        v_t = beta2 * v_t + (1 - beta2) * (gradient**2)
        m_cap = m_t / (1 - (beta1**t))
        v_cap = v_t / (1 - (beta2**t))
        theta = theta - (alpha * m_cap) / (np.sqrt(v_cap) + epsilon)
        loss = -np.mean(y * np.log(h + 1e-15) + (1 - y) * np.log(1 - h + 1e-15))
        loss_history.append(loss)
    return theta, loss_history

def create_composite_infographic(case_title, code_text, theta, loss_history, output_path):
    # Set up the figure (Matching Gen 1 style: 10x14)
    fig = plt.figure(figsize=(10, 14), facecolor='white')
    
    # 1. Header (Gray bar)
    header_ax = fig.add_axes([0.05, 0.94, 0.9, 0.03], facecolor='#666666')
    header_ax.text(0.02, 0.5, case_title, color='white', fontsize=14, weight='bold', va='center', ha='left')
    header_ax.set_xticks([])
    header_ax.set_yticks([])
    for spine in header_ax.spines.values(): spine.set_visible(False)
    
    # 2. Code Block (Light yellow background)
    code_ax = fig.add_axes([0.05, 0.56, 0.9, 0.37], facecolor='#FFFBE6')
    code_ax.text(0.02, 0.97, code_text, transform=code_ax.transAxes, 
                fontsize=11, fontfamily='monospace', va='top', ha='left', color='#333333')
    code_ax.text(0.98, 0.02, "# Python Source Code", transform=code_ax.transAxes, 
                fontsize=9, color='#999999', ha='right', va='bottom', style='italic')
    code_ax.set_xticks([])
    code_ax.set_yticks([])
    for spine in code_ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#CCCCCC')

    # 3. Results Area (Light blue background) - NOW ABOVE PLOT
    res_ax = fig.add_axes([0.05, 0.38, 0.9, 0.16], facecolor='#F0F8FF')
    res_text = "Final Model Parameters (Weights):\n" + "-"*35 + "\n"
    res_text += f"Beta 0 (Intercept)    : {theta[0]:.6f}\n"
    res_text += f"Beta 1 (Feature 1)    : {theta[1]:.6f}\n"
    res_text += f"Beta 2 (Feature 2)    : {theta[2]:.6f}\n"
    res_text += f"Final Cross-Entropy Loss: {loss_history[-1]:.8f}"
    res_ax.text(0.02, 0.85, res_text, transform=res_ax.transAxes, fontsize=12, family='monospace', va='top', linespacing=1.5)
    res_ax.set_xticks([])
    res_ax.set_yticks([])
    for spine in res_ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#CCCCCC')
    
    # 4. Loss plot (Bottom)
    plot_ax = fig.add_axes([0.1, 0.06, 0.8, 0.28])
    plot_ax.plot(loss_history, color='#00a08a', linewidth=2.5)
    plot_ax.set_title('Optimization Convergence (Loss History)', fontsize=12, weight='bold', color='#333333')
    plot_ax.set_xlabel('Iterations (Epochs)', fontsize=10)
    plot_ax.set_ylabel('Log-Loss', fontsize=10)
    plot_ax.grid(True, linestyle=':', alpha=0.6)
    plot_ax.spines['top'].set_visible(False)
    plot_ax.spines['right'].set_visible(False)
    
    # Outer Border
    rect = patches.Rectangle((0.01, 0.01), 0.98, 0.98, linewidth=1, edgecolor='#999999', facecolor='none', transform=fig.transFigure)
    fig.patches.append(rect)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

# Case 2 Content
code2 = """
# Logistic Regression with Adam (Case 2)
import numpy as np

# Initializing Data
X = np.array([[20, 20k], [25, 25k], ..., [42, 75k]])
y = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0, 1])

def sigmoid(z): return 1 / (1 + np.exp(-z))

# Training Loop
for t in range(1, 2000):
    p = sigmoid(X_bias @ theta)
    grad = X_bias.T @ (p - y) / m
    
    # Adam velocity and momentum
    m_t = b1*m_t + (1-b1)*grad
    v_t = b2*v_t + (1-b2)*grad**2
    
    # Param update with bias correction
    theta -= alpha * m_hat / (sqrt(v_hat) + eps)
"""

X2 = np.array([[20, 20000], [25, 25000], [30, 30000], [35, 80000], [40, 85000], [45, 90000], [50, 40000], [55, 95000], [22, 22000], [42, 75000]])
y2 = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0, 1])
theta2, loss2 = adam_logistic_regression(X2, y2)
create_composite_infographic("case_study_2_customer.py", code2, theta2, loss2, "CH3_case2_adam_results.png")

# Case 3 Content
code3 = """
# Logistic Regression with Adam (Case 3)
import numpy as np

# Heart Disease Data
X = np.array([[25, 180], [30, 190], ..., [58, 230]])
y = np.array([0, 0, 1, 1, 1, 0, 0, 1, 1, 1])

# Adam Optimizer
def train(X, y, lr=0.01):
    m, v = 0, 0
    theta = np.zeros(3)
    for t in range(1, 2000):
        # Forward and Gradient
        p = 1 / (1 + np.exp(-X@theta))
        g = X.T @ (p - y) / n
        
        # Adaptive updates
        update = apply_adam(g, t)
        theta -= lr * update
    return theta
"""

X3 = np.array([[25, 180], [30, 190], [45, 220], [50, 240], [60, 260], [35, 200], [40, 210], [55, 250], [65, 280], [58, 230]])
y3 = np.array([0, 0, 1, 1, 1, 0, 0, 1, 1, 1])
theta3, loss3 = adam_logistic_regression(X3, y3)
create_composite_infographic("case_study_3_heart.py", code3, theta3, loss3, "CH3_case3_adam_results.png")

print("Updated infographics generated.")
