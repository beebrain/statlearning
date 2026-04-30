import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification, make_regression

# Set style for academic look
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- Panel 1: Regression ---
np.random.seed(42)
X_reg = np.linspace(0, 10, 30)
y_reg = 0.5 * X_reg**2 - 2 * X_reg + 5 + np.random.normal(0, 2, 30)
# Fit a polynomial for the curve
p = np.poly1d(np.polyfit(X_reg, y_reg, 2))
x_line = np.linspace(0, 10, 100)

ax1.scatter(X_reg, y_reg, color='#1f77b4', alpha=0.7, label='Data Points', s=60)
ax1.plot(x_line, p(x_line), color='#d62728', linewidth=2.5, label='Regression Model\n(Continuous Prediction)')

ax1.set_title('Regression Problem', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Input Feature (x)', fontsize=12)
ax1.set_ylabel('Continuous Output (y)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.legend(loc='upper left', frameon=True, framealpha=0.9)

# Annotation for Regression
ax1.text(5, 50, 'Output is a Quantity\n(e.g., Price, Temp)', 
         ha='center', fontsize=11, style='italic',
         bbox=dict(facecolor='#e6f2ff', edgecolor='#1f77b4', boxstyle='round,pad=0.5', alpha=0.8))


# --- Panel 2: Classification ---
X_class, y_class = make_classification(n_samples=40, n_features=2, n_redundant=0, 
                                       n_informative=2, random_state=1, n_clusters_per_class=1)
# Simply shift data for better visualization if needed
X_class += 2 

# Plot classes
class_0 = X_class[y_class == 0]
class_1 = X_class[y_class == 1]

ax2.scatter(class_0[:, 0], class_0[:, 1], color='#1f77b4', marker='o', s=60, label='Class A (e.g., Healthy)')
ax2.scatter(class_1[:, 0], class_1[:, 1], color='#ff7f0e', marker='^', s=60, label='Class B (e.g., Sick)')

# Decision Boundary (approximate for visualization)
xx = np.linspace(min(X_class[:,0])-1, max(X_class[:,0])+1, 100)
yy = -1.2 * xx + 4.5 # Manually tuned simple boundary
ax2.plot(xx, yy, color='green', linewidth=2.5, linestyle='--', label='Decision Boundary')

ax2.set_title('Classification Problem', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Feature 1 (x1)', fontsize=12)
ax2.set_ylabel('Feature 2 (x2)', fontsize=12)
ax2.set_xlim(min(X_class[:,0])-1, max(X_class[:,0])+1)
ax2.set_ylim(min(X_class[:,1])-1, max(X_class[:,1])+1)
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.legend(loc='lower right', frameon=True, framealpha=0.9)

# Annotation for Classification
ax2.text(1, 3.5, 'Output is a Category\n(e.g., Yes/No)', 
         ha='center', fontsize=11, style='italic',
         bbox=dict(facecolor='#fff2e6', edgecolor='#ff7f0e', boxstyle='round,pad=0.5', alpha=0.8))

plt.tight_layout()
plt.savefig('d:/OnedrivePM/OneDrive - Uttaradit Rajabhat University/URU/1_Books/6_Stat Learning/reg_vs_class_diagram.png', dpi=300, bbox_inches='tight')
print("Image saved successfully.")
