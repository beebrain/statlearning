import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification

# Set style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

def create_case_study_plot(filename, title, reg_config, class_config):
    # reg_config: (xlabel, ylabel, x_range, slope, intercept, noise)
    # class_config: (xlabel, ylabel, class_labels, feature_1_range, feature_2_range)
    
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1], hspace=0.3)

    # --- Regression Panel ---
    ax1 = fig.add_subplot(gs[0, 0])
    np.random.seed(42)
    
    # Generate realistic regression data
    x_min, x_max = reg_config[2]
    x = np.linspace(x_min, x_max, 10)
    slope, intercept, noise_scale = reg_config[3], reg_config[4], reg_config[5]
    y = slope * x + intercept + np.random.normal(0, noise_scale, 10)
    
    ax1.scatter(x, y, color='#1f77b4', alpha=0.7, label='Data', s=80)
    ax1.plot(x, slope * x + intercept, color='#d62728', linewidth=2.5, label='Model')
    ax1.set_title(f'{title}: Regression', fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel(reg_config[0], fontsize=12)
    ax1.set_ylabel(reg_config[1], fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.tick_params(axis='both', which='major', labelsize=10)

    # Regression Table
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.axis('off')
    # Format: commas for large numbers, 1 decimal for small
    def smart_format(val):
        if abs(val) >= 1000:
            return f'{val:,.0f}'
        elif abs(val) >= 10:
            return f'{val:.0f}'
        else:
            return f'{val:.1f}'
    
    reg_data = [[smart_format(val), smart_format(op)] for val, op in zip(x[:6], y[:6])]
    table1 = ax3.table(cellText=reg_data, colLabels=[reg_config[0], reg_config[1]], loc='center', cellLoc='center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(12)
    table1.scale(1, 2.0)
    ax3.set_title(f'Example Data ({reg_config[0]} vs {reg_config[1]})', fontsize=14, pad=5)

    # --- Classification Panel ---
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Generate realistic classification data manually to control ranges
    f1_min, f1_max = class_config[3] # Feature 1 Range
    f2_min, f2_max = class_config[4] # Feature 2 Range
    
    # Create 2 clusters
    n_per_class = 6
    # Class 0: Low F1, Low F2
    c0_f1 = np.random.uniform(f1_min, (f1_min+f1_max)*0.45, n_per_class)
    c0_f2 = np.random.uniform(f2_min, (f2_min+f2_max)*0.45, n_per_class)
    
    # Class 1: High F1, High F2
    c1_f1 = np.random.uniform((f1_min+f1_max)*0.55, f1_max, n_per_class)
    c1_f2 = np.random.uniform((f2_min+f2_max)*0.55, f2_max, n_per_class)
    
    dataset = []
    for i in range(n_per_class):
        dataset.append([c0_f1[i], c0_f2[i], 0])
        dataset.append([c1_f1[i], c1_f2[i], 1])
    dataset = np.array(dataset)
    # Shuffle for table randomness
    np.random.shuffle(dataset)
    
    # Plotting needs sorted by class for consistent colors
    class_0 = dataset[dataset[:, 2] == 0]
    class_1 = dataset[dataset[:, 2] == 1]
    
    ax2.scatter(class_0[:, 0], class_0[:, 1], color='#1f77b4', marker='o', label=class_config[2][0], s=80)
    ax2.scatter(class_1[:, 0], class_1[:, 1], color='#ff7f0e', marker='^', label=class_config[2][1], s=80)
    
    # Simple separator
    xx = np.linspace(f1_min, f1_max, 100)
    # Line passing through middle
    mid_f1 = (f1_min + f1_max) / 2
    mid_f2 = (f2_min + f2_max) / 2
    # Determine slope based on ranges to look nice (approx -1 in normalized space, but scaled)
    # y - y1 = m(x - x1) -> passing through (mid_f1, mid_f2) with negative slope
    slope_vis = -1.0 * (f2_max - f2_min) / (f1_max - f1_min) 
    yy = slope_vis * (xx - mid_f1) + mid_f2
    
    ax2.plot(xx, yy, color='green', linestyle='--', label='Boundary', linewidth=2)
    ax2.set_xlim(f1_min, f1_max)
    ax2.set_ylim(f2_min, f2_max)
    
    ax2.set_title(f'{title}: Classification', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel(class_config[0], fontsize=12)
    ax2.set_ylabel(class_config[1], fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.tick_params(axis='both', which='major', labelsize=10)

    # Classification Table
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    
    # Pick first 6
    table_rows = []
    for i in range(6):
        row = dataset[i]
        label_text = class_config[2][int(row[2])]
        table_rows.append([smart_format(row[0]), smart_format(row[1]), label_text])
    
    table2 = ax4.table(cellText=table_rows, colLabels=[class_config[0], class_config[1], 'Class'], loc='center', cellLoc='center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(12) # Balance size
    table2.scale(1, 2.0)
    ax4.set_title(f'Example Data (Class Labels)', fontsize=14, pad=5)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")

# 1. Medical Case
# Reg: Age (20-80) -> Recovery (10-60 days)
# Class: BMI (18-35) & Glucose (80-200) -> Diabetic
create_case_study_plot(
    'd:/OnedrivePM/OneDrive - Uttaradit Rajabhat University/URU/1_Books/6_Stat Learning/case_medical.png',
    'Medical Case',
    ('Age', 'Recovery Days', (20, 80), 0.5, 5, 3), 
    ('BMI', 'Glucose Level', ['Non-Diabetic', 'Diabetic'], (18, 35), (80, 200))
)

# 2. Marketing Case
# Reg: Ad Spend (10k-100k) -> Sales (100k-1M)
# Class: Age (25-60) & Annual Income (20k-100k) -> Will Buy
create_case_study_plot(
    'd:/OnedrivePM/OneDrive - Uttaradit Rajabhat University/URU/1_Books/6_Stat Learning/case_marketing.png',
    'Marketing Case',
    ('Ad Spend', 'Total Sales', (10000, 100000), 10, 50000, 15000), 
    ('Age', 'Annual Income', ['Will Not Buy', 'Will Buy'], (25, 60), (20000, 100000))
)

# 3. Finance Case
# Reg: Market Index (1000-1800) -> Stock Price (50-250)
# Class: Debt Ratio (0.1-0.9) & Income (20k-100k) -> Default
create_case_study_plot(
    'd:/OnedrivePM/OneDrive - Uttaradit Rajabhat University/URU/1_Books/6_Stat Learning/case_finance.png',
    'Finance Case',
    ('Market Index', 'Stock Price', (1000, 1800), 0.2, -100, 10), 
    ('Debt Ratio', 'Income Level', ['Non-Default', 'Default'], (0.1, 0.9), (20000, 100000))
)
