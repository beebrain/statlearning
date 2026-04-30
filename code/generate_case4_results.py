import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager

# Load Thai Font
font_path = r"d:\OnedrivePM\OneDrive - Uttaradit Rajabhat University\URU\1_Books\6_Stat Learning\TH Sarabun New.TTF"
thai_font = font_manager.FontProperties(fname=font_path)

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

def adam_logistic_regression(X, y, alpha=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, iterations=2000):
    n_samples, n_features = X.shape
    X_bias = np.c_[np.ones(n_samples), X]
    n_params = n_features + 1
    theta = np.zeros(n_params)
    m_t = np.zeros(n_params)
    v_t = np.zeros(n_params)
    loss_history = []
    
    for t in range(1, iterations + 1):
        z = np.dot(X_bias, theta)
        h = sigmoid(z)
        gradient = np.dot(X_bias.T, (h - y)) / n_samples
        m_t = beta1 * m_t + (1 - beta1) * gradient
        v_t = beta2 * v_t + (1 - beta2) * (gradient**2)
        m_cap = m_t / (1 - (beta1**t))
        v_cap = v_t / (1 - (beta2**t))
        theta = theta - (alpha * m_cap) / (np.sqrt(v_cap) + epsilon)
        loss = -np.mean(y * np.log(h + 1e-15) + (1 - y) * np.log(1 - h + 1e-15))
        loss_history.append(loss)
    return theta, loss_history

def create_case4_infographic(case_title, code_text, theta, loss_history, output_path):
    fig = plt.figure(figsize=(10, 14), facecolor='white')
    
    # 1. Header (Gray bar)
    header_ax = fig.add_axes([0.05, 0.94, 0.9, 0.03], facecolor='#555555')
    header_ax.text(0.02, 0.5, case_title, color='white', fontsize=16, weight='bold',
                   va='center', ha='left', fontproperties=thai_font)
    header_ax.set_xticks([])
    header_ax.set_yticks([])
    for spine in header_ax.spines.values(): spine.set_visible(False)
    
    # 2. Code Block (Light yellow background)
    code_ax = fig.add_axes([0.05, 0.56, 0.9, 0.37], facecolor='#FFFBE6')
    code_ax.text(0.02, 0.97, code_text, transform=code_ax.transAxes,
                fontsize=10.5, fontfamily='monospace', va='top', ha='left', color='#333333')
    code_ax.text(0.98, 0.02, "# Python Source Code", transform=code_ax.transAxes,
                fontsize=9, color='#999999', ha='right', va='bottom', style='italic')
    code_ax.set_xticks([])
    code_ax.set_yticks([])
    for spine in code_ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#CCCCCC')

    # 3. Results Area (Light blue background)
    res_ax = fig.add_axes([0.05, 0.38, 0.9, 0.16], facecolor='#F0F8FF')
    res_text = "Final Model Parameters (Weights):\n" + "-"*35 + "\n"
    res_text += f"Beta 0 (Intercept)    : {theta[0]:.6f}\n"
    res_text += f"Beta 1 (Score)        : {theta[1]:.6f}\n"
    res_text += f"Beta 2 (Income k$)    : {theta[2]:.6f}\n"
    res_text += f"Beta 3 (DTI %)        : {theta[3]:.6f}\n"
    res_text += f"Beta 4 (Emp Yrs)      : {theta[4]:.6f}\n"
    res_text += f"Beta 5 (Loan k$)      : {theta[5]:.6f}\n"
    res_text += f"Final Cross-Entropy Loss: {loss_history[-1]:.8f}"
    res_ax.text(0.02, 0.92, res_text, transform=res_ax.transAxes, fontsize=10.5, family='monospace', va='top', linespacing=1.4)
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

# Credit Scoring Data (Case 4)
# Features: Score, Income(k$), DTI(%), Emp_Yrs, Loan(k$)
# Label: Default (1 = default, 0 = no default)
X4 = np.array([
    [720, 55, 15, 8, 20],
    [680, 40, 22, 5, 25],
    [600, 30, 35, 2, 30],
    [750, 80, 10, 15, 40],
    [620, 35, 40, 1, 35],
    [700, 60, 18, 10, 28],
    [580, 25, 45, 1, 40],
    [660, 45, 25, 6, 22],
    [740, 70, 12, 12, 18],
    [610, 28, 38, 2, 32]
])
y4 = np.array([0, 0, 1, 0, 1, 0, 1, 0, 0, 1])

theta4, loss4 = adam_logistic_regression(X4, y4, alpha=0.001, iterations=3000)
print("Case 4 Final Betas:", theta4)

code4 = """import numpy as np

# Credit Scoring Data (Case 4)
X = np.array([
    [720, 55, 15, 8, 20],   # Score, Income, DTI%, EmpYrs, Loan
    [680, 40, 22, 5, 25],
    [600, 30, 35, 2, 30],
    [750, 80, 10, 15, 40],
    [620, 35, 40, 1, 35],
    [700, 60, 18, 10, 28],
    [580, 25, 45, 1, 40],
    [660, 45, 25, 6, 22],
    [740, 70, 12, 12, 18],
    [610, 28, 38, 2, 32]
])
y = np.array([0, 0, 1, 0, 1, 0, 1, 0, 0, 1])  # Default

def sigmoid(z): return 1/(1+np.exp(-z))

# Adam Optimizer (lr=0.001, b1=0.9, b2=0.999, 3000 epochs)
theta = np.zeros(6)           # theta[0]=intercept
m, v = np.zeros(6), np.zeros(6)
for t in range(1, 3001):
    h = sigmoid(X_bias @ theta)
    g = X_bias.T @ (h - y) / n
    m = 0.9*m + 0.1*g;  v = 0.999*v + 0.001*g**2
    theta -= 0.001 * (m/(1-0.9**t)) / (np.sqrt(v/(1-0.999**t))+1e-8)
"""

create_case4_infographic("case_study_4_credit_scoring.py", code4, theta4, loss4, "CH3_case4_adam_results.png")
print("Case 4 infographic generated.")
