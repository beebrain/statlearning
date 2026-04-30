import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set style for academic look
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- Panel 1: Simple Linear Regression ---
np.random.seed(42)
x = np.linspace(0, 10, 20)
y = 2 * x + 5 + np.random.normal(0, 2, 20)

ax1.scatter(x, y, color='#1f77b4', alpha=0.7, label='Data Points')
ax1.plot(x, 2 * x + 5, color='#d62728', linewidth=2, label='Regression Line')
ax1.set_title('Simple Linear Regression\n(Single Independent Variable)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Independent Variable (x)\n(e.g., Reading Hours)', fontsize=11)
ax1.set_ylabel('Dependent Variable (y)\n(e.g., Exam Score)', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.legend()
ax1.text(1, 22, r'$y = \beta_0 + \beta_1x + \epsilon$', fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# --- Panel 2: Multiple Linear Regression (Conceptual Diagram) ---
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Multiple Linear Regression\n(Multiple Independent Variables)', fontsize=14, fontweight='bold', pad=15)

# Nodes
def draw_circle(ax, center, radius, text, color='#aec7e8'):
    circle = patches.Circle(center, radius, facecolor=color, edgecolor='#1f77b4', linewidth=1.5)
    ax.add_patch(circle)
    ax.text(center[0], center[1], text, ha='center', va='center', fontsize=10, fontweight='bold')

# Inputs
draw_circle(ax2, (2, 8), 0.8, 'Location\n(x1)')
draw_circle(ax2, (2, 5), 0.8, 'Size\n(x2)')
draw_circle(ax2, (2, 2), 0.8, 'Rooms\n(x3)')

# Output
draw_circle(ax2, (8, 5), 0.8, 'House Price\n(y)', color='#ffbb78')

# Arrows
arrow_props = dict(facecolor='gray', edgecolor='gray', alpha=0.6, width=0.1, headwidth=0.4)
ax2.annotate('', xy=(7.2, 5.2), xytext=(2.8, 8), arrowprops=arrow_props)
ax2.annotate('', xy=(7.2, 5), xytext=(2.8, 5), arrowprops=arrow_props)
ax2.annotate('', xy=(7.2, 4.8), xytext=(2.8, 2), arrowprops=arrow_props)

# Equation
ax2.text(5, 0.5, r'$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \epsilon$', ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='#ccc'))

plt.tight_layout()
plt.savefig('d:/OnedrivePM/OneDrive - Uttaradit Rajabhat University/URU/1_Books/6_Stat Learning/regression_types_diagram.png', dpi=300, bbox_inches='tight')
print("Image saved successfully.")
