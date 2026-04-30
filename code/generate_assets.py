import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. The Analysis Code Content
code_part_1 = """def descriptive_statistics(df):
    # Calculate basic descriptive statistics
    stats = df.describe()
    return stats"""

code_part_2 = """# Define the dataset
data = {
    'Area_sqm': [50, 80, 120, 45, 60, 200, 35, 90, 150, 75],
    'Bedrooms': [1, 2, 3, 1, 2, 4, 1, 3, 3, 2],
    'Dist_BTS_km': [0.5, 1.2, 2.5, 0.2, 5.0, 3.0, 0.1, 1.5, 4.0, 0.8],
    'Age_Years': [5, 8, 10, 2, 15, 5, 1, 20, 12, 6],
    'Price_MB': [3.5, 5.2, 6.8, 4.0, 2.8, 12.5, 3.8, 4.5, 7.5, 4.9]
}

# Create DataFrame and Analyze
df = pd.DataFrame(data)
print(descriptive_statistics(df))"""

# 2. Perform the actual analysis for the output
data = {
    'Area_sqm': [50, 80, 120, 45, 60, 200, 35, 90, 150, 75],
    'Bedrooms': [1, 2, 3, 1, 2, 4, 1, 3, 3, 2],
    'Dist_BTS_km': [0.5, 1.2, 2.5, 0.2, 5.0, 3.0, 0.1, 1.5, 4.0, 0.8],
    'Age_Years': [5, 8, 10, 2, 15, 5, 1, 20, 12, 6],
    'Price_MB': [3.5, 5.2, 6.8, 4.0, 2.8, 12.5, 3.8, 4.5, 7.5, 4.9]
}
df = pd.DataFrame(data)
# 3. Helper function to render text in a "Mac-style" editor window
def render_code_window(text, filename, title="Python Code", is_code=True, bg_color=None, text_color=None):
    # Keeping old function for compatibility if needed, but we will focus on new one
    pass # Implementation skipped for brevity in this replace block as we are adding new logic below

def render_combined_window(code_text, output_text, filename, title="analysis.py"):
    code_lines = code_text.split('\n')
    output_lines = output_text.split('\n')
    
    # Fonts and sizing
    fontsize_title = 12
    fontsize_content = 10
    line_height = 0.3
    padding = 0.5
    
    # Calculate dimensions
    max_len_code = max(len(line) for line in code_lines) if code_lines else 0
    max_len_out = max(len(line) for line in output_lines) if output_lines else 0
    max_len = max(max_len_code, max_len_out)
    
    code_height = len(code_lines) * line_height + padding
    output_height = len(output_lines) * line_height + padding
    title_height = 0.5
    
    total_height = title_height + code_height + output_height
    fig_width = max(8, max_len * 0.14)
    
    fig, ax = plt.subplots(figsize=(fig_width, total_height))
    ax.set_xlim(0, fig_width)
    ax.set_ylim(0, total_height)
    ax.axis('off')
    
    # 1. Title Bar (Dark Grey)
    rect_title = patches.Rectangle((0, total_height - title_height), fig_width, title_height, 
                                   facecolor='#666666', edgecolor='none')
    ax.add_patch(rect_title)
    ax.text(padding, total_height - title_height/2, title, 
            color='white', fontsize=fontsize_title, va='center', fontweight='bold', family='monospace')
    
    # 2. Code Section (Light Yellow)
    rect_code = patches.Rectangle((0, output_height), fig_width, code_height, 
                                  facecolor='#FFFFE0', edgecolor='#333333', linewidth=1)
    ax.add_patch(rect_code)
    
    # Draw simple syntax highlighting for code
    y_pos = total_height - title_height - padding/2
    keywords = ['import', 'from', 'def', 'return', 'print', 'if', 'else', 'for', 'in']
    
    for line in code_lines:
        words = line.split(' ')
        x_pos = padding/2
        # Very basic manual rendering for colored text
        # Note: robust syntax highlighting in matplotlib is complex, using simplified approach
        # Alternatively we can just print the whole line in black/dark blue for reliability
        ax.text(x_pos, y_pos, line, ha='left', va='top', 
                fontsize=fontsize_content, family='monospace', color='#000000')
        y_pos -= line_height

    # 3. Output Section (Light Grey)
    rect_out = patches.Rectangle((0, 0), fig_width, output_height, 
                                 facecolor='#F0F0F0', edgecolor='#333333', linewidth=1)
    ax.add_patch(rect_out)
    
    y_pos = output_height - padding/2
    for line in output_lines:
        ax.text(padding/2, y_pos, line, ha='left', va='top', 
                fontsize=fontsize_content, family='monospace', color='#333333')
        y_pos -= line_height
        
    # Border around everything
    rect_border = patches.Rectangle((0, 0), fig_width, total_height, 
                                    fill=False, edgecolor='#333333', linewidth=1)
    ax.add_patch(rect_border)

    plt.savefig(filename, bbox_inches='tight', dpi=150)
    plt.close()

# Combined code text
full_code = """import pandas as pd

# Define the dataset
data = {
    'Area_sqm': [50, 80, 120, 45, 60, 200, 35, 90, 150, 75],
    'Bedrooms': [1, 2, 3, 1, 2, 4, 1, 3, 3, 2],
    'Dist_BTS_km': [0.5, 1.2, 2.5, 0.2, 5.0, 3.0, 0.1, 1.5, 4.0, 0.8],
    'Age_Years': [5, 8, 10, 2, 15, 5, 1, 20, 12, 6],
    'Price_MB': [3.5, 5.2, 6.8, 4.0, 2.8, 12.5, 3.8, 4.5, 7.5, 4.9]
}

def descriptive_statistics(df):
    return df.describe()

df = pd.DataFrame(data)
print(descriptive_statistics(df))"""

# Generate Output text for the combined window
# We need to recreate the DF and output because I removed the previous global scope block in the previous edit (or it was seemingly disconnected)
# Actually, let's just make sure it's defined right here.
data_dict = {
    'Area_sqm': [50, 80, 120, 45, 60, 200, 35, 90, 150, 75],
    'Bedrooms': [1, 2, 3, 1, 2, 4, 1, 3, 3, 2],
    'Dist_BTS_km': [0.5, 1.2, 2.5, 0.2, 5.0, 3.0, 0.1, 1.5, 4.0, 0.8],
    'Age_Years': [5, 8, 10, 2, 15, 5, 1, 20, 12, 6],
    'Price_MB': [3.5, 5.2, 6.8, 4.0, 2.8, 12.5, 3.8, 4.5, 7.5, 4.9]
}
df = pd.DataFrame(data_dict)
output_text = str(df.describe())

# Generate Combined Image
print("Generating CH1_python_combined.png...")
render_combined_window(full_code, output_text, "CH1_python_combined.png", title="house_price_analysis.py")

# 5. Generate Scatter Plot Code Image
scatter_code_text = """import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 7))
plt.style.use('bmh')
plt.scatter(df['Area_sqm'], df['Price_MB'], color='#007acc', 
            alpha=0.9, s=100, edgecolors='white', linewidth=1.5)
plt.title('Relationship between House Area and Price', fontsize=14)
plt.xlabel('Area (sq.m.)', fontsize=12)
plt.ylabel('Price (Million Baht)', fontsize=12)

# Add trend line
z = np.polyfit(df['Area_sqm'], df['Price_MB'], 1)
p = np.poly1d(z)
plt.plot(df['Area_sqm'], p(df['Area_sqm']), "r--", alpha=0.6, 
         label='Trend Line')
plt.legend()

plt.tight_layout()
plt.show()"""

# We don't need the separate code image anymore if we combine them, but good to keep basic logic if needed.
# print("Generating CH1_python_scatter_code.png...")
# render_code_window(scatter_code_text, "CH1_python_scatter_code.png", title="plot_scatter.py", is_code=True, bg_color='#FFFFE0')

# 6. Generate Actual Scatter Plot (enhanced)
print("Generating CH1_ex_home_scatter.png...")
plt.figure(figsize=(10, 7))
plt.style.use('bmh') # Use a clean style
plt.scatter(df['Area_sqm'], df['Price_MB'], color='#007acc', alpha=0.9, s=100, edgecolors='white', linewidth=1.5, zorder=3)
plt.title('Relationship between House Area and Price', fontsize=14, pad=20)
plt.xlabel('Area (sq.m.)', fontsize=12)
plt.ylabel('Price (Million Baht)', fontsize=12)

# Add trend line
import numpy as np
z = np.polyfit(df['Area_sqm'], df['Price_MB'], 1)
p = np.poly1d(z)
plt.plot(df['Area_sqm'], p(df['Area_sqm']), "r--", alpha=0.6, label='Trend Line', zorder=2)
plt.legend()

for i, row in df.iterrows():
    plt.annotate(f"{row['Price_MB']}M", (row['Area_sqm'], row['Price_MB']), 
                 xytext=(8, -8), textcoords='offset points', fontsize=9, color='#444444')

plt.tight_layout()
plt.savefig("CH1_ex_home_scatter.png", dpi=150)
plt.close()

# 7. Generate Combined Scatter Code + Plot
def render_combined_code_and_plot(code_text, plot_filename, output_filename, title="plot.py"):
    code_lines = code_text.split('\n')
    
    # Measurements
    fontsize_title = 12
    fontsize_content = 10
    line_height = 0.3
    padding = 0.5
    
    code_height = len(code_lines) * line_height + padding
    title_height = 0.5
    
    # Load the plot image to determine size
    img = plt.imread(plot_filename)
    img_h, img_w, _ = img.shape
    aspect_ratio = img_h / img_w
    
    # Scale image to fit within width (approx)
    # Fig width determined by code
    max_len_code = max(len(line) for line in code_lines) if code_lines else 0
    fig_width = max(8, max_len_code * 0.14)
    
    # Calculate desired image height in figure coordinates
    # Matplotlib figures are in inches. 
    # Let's say we want image width to match fig width minus padding
    display_img_width = fig_width
    display_img_height = display_img_width * aspect_ratio
    
    total_height = title_height + code_height + display_img_height
    
    fig, ax = plt.subplots(figsize=(fig_width, total_height))
    ax.set_xlim(0, fig_width)
    ax.set_ylim(0, total_height)
    ax.axis('off')
    
    # 1. Title Bar
    rect_title = patches.Rectangle((0, total_height - title_height), fig_width, title_height, 
                                   facecolor='#666666', edgecolor='none')
    ax.add_patch(rect_title)
    ax.text(padding, total_height - title_height/2, title, 
            color='white', fontsize=fontsize_title, va='center', fontweight='bold', family='monospace')
            
    # 2. Code Section
    rect_code = patches.Rectangle((0, display_img_height), fig_width, code_height, 
                                  facecolor='#FFFFE0', edgecolor='#333333', linewidth=1)
    ax.add_patch(rect_code)
    
    y_pos = total_height - title_height - padding/2
    for line in code_lines:
        ax.text(padding/2, y_pos, line, ha='left', va='top', 
                fontsize=fontsize_content, family='monospace', color='#000000')
        y_pos -= line_height

    # 3. Image Section
    # Display the image in the bottom area using imshow with extent
    # zorder=1 to ensure it is below the border
    ax.imshow(img, extent=[0, fig_width, 0, display_img_height], aspect='auto', zorder=1)
    
    # Add a border frame for the plot area on top
    # zorder=2 to ensure it is above the image
    rect_plot = patches.Rectangle((0, 0), fig_width, display_img_height, 
                                  fill=False, edgecolor='#333333', linewidth=2, zorder=2)
    ax.add_patch(rect_plot)
    
    # Border
    rect_border = patches.Rectangle((0, 0), fig_width, total_height, 
                                    fill=False, edgecolor='#333333', linewidth=1)
    ax.add_patch(rect_border)
    
    plt.savefig(output_filename, bbox_inches='tight', dpi=150)
    plt.close()

print("Generating CH1_scatter_combined.png...")
render_combined_code_and_plot(scatter_code_text, "CH1_ex_home_scatter.png", "CH1_scatter_combined.png", title="plot_scatter.py")

# ==========================================
# NEW: Chapter 3 Newton-Raphson Case Studies
# ==========================================

# Case Study 1: Root Finding
# ---------------------------
root_code_text = """def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            return None
        x = x - fx / dfx
    return x

# Define function f(x) = x^3 - 2x - 2
f = lambda x: x**3 - 2*x - 2
df = lambda x: 3*x**2 - 2

root = newton_raphson(f, df, x0=2.0)
print(f"Root found at x = {root:.6f}")"""

print("Generating CH3_newton_root plot...")
# Generate the plot for Root Finding
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
x = np.linspace(0, 3, 100)
y = x**3 - 2*x - 2
plt.plot(x, y, label='$f(x) = x^3 - 2x - 2$', color='#d55e00', linewidth=2)
plt.axhline(0, color='gray', linestyle='--', alpha=0.7)
# Root location
root_val = 1.769292
plt.plot(root_val, 0, 'go', markersize=10, label=f'Root $\\approx {root_val:.4f}$', zorder=5)
# Tangent line at x0=2
x0 = 2
y0 = x0**3 - 2*x0 - 2
slope = 3*x0**2 - 2
# y - y0 = m(x - x0) => y = m(x-x0) + y0
def tangent_line(x_val): return slope * (x_val - x0) + y0
plt.plot(x, tangent_line(x), '--', color='#0072b2', alpha=0.5, label='Tangent at $x_0=2$')

plt.title('Newton-Raphson Root Finding', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ex_root_plot.png", dpi=150)
plt.close()

print("Generating CH3_newton_root.png combined...")
render_combined_code_and_plot(root_code_text, "CH3_ex_root_plot.png", "CH3_newton_root.png", title="newton_root.py")


# Case Study 2: Logistic Regression Optimization
# ----------------------------------------------
logistic_code_text = """import numpy as np

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Newton-Raphson for Logistic Regression
def logistic_newton(X, y, beta, iterations=10):
    for i in range(iterations):
        z = np.dot(X, beta)
        p = sigmoid(z)
        W = np.diag(p * (1 - p))
        
        # Gradient (Score)
        gradient = np.dot(X.T, (y - p))
        # Hessian
        hessian = -np.dot(np.dot(X.T, W), X)
        
        # Update beta
        beta -= np.linalg.inv(hessian).dot(gradient)
    return beta"""

print("Generating CH3_logistic_plot.png...")
# Generate the plot for Logistic Regression
# Synthetic data
np.random.seed(42)
n_points = 20
X_val = np.sort(np.random.uniform(-5, 5, n_points))
# True parameters: beta0=0, beta1=1
true_p = 1 / (1 + np.exp(-(0 + 1 * X_val)))
y_val = np.random.binomial(1, true_p)

plt.figure(figsize=(8, 6))
plt.style.use('bmh')
plt.scatter(X_val, y_val, color='black', s=50, label='Data (0/1)', zorder=3)

# Plot the fitted curve (using true params for clean illustration or estimate?)
# Let's estimate quickly for the plot using the logic
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(C=1e5)
clf.fit(X_val.reshape(-1, 1), y_val)
b0, b1 = clf.intercept_[0], clf.coef_[0][0]

x_plot = np.linspace(-6, 6, 200)
p_plot = 1 / (1 + np.exp(-(b0 + b1 * x_plot)))

plt.plot(x_plot, p_plot, color='#009e73', linewidth=3, label='Fitted Sigmoid Model')
plt.title('Logistic Regression Optimization Result', fontsize=14)
plt.xlabel('Feature (x)', fontsize=12)
plt.ylabel('Probability P(Y=1)', fontsize=12)
plt.axhline(0.5, color='gray', linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ex_logistic_plot.png", dpi=150)
plt.close()

print("Generating CH3_newton_logistic.png combined...")
render_combined_code_and_plot(logistic_code_text, "CH3_ex_logistic_plot.png", "CH3_newton_logistic.png", title="logistic_opt.py")


# ==========================================
# NEW: Chapter 3 Predictions Case Studies
# ==========================================

# Example 1: Predicting Admission (Single Variable)
# -------------------------------------------------
ex1_code_text = """import numpy as np
from sklearn.linear_model import LogisticRegression

# Data: Hours Studied (X) vs Pass(1)/Fail(0)
X = np.array([1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 5.5, 6.0]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1])

# Create and fit model
model = LogisticRegression(C=10.0, random_state=42)
model.fit(X, y)

# Coefficients
b0 = model.intercept_[0]
b1 = model.coef_[0][0]
print(f"Intercept (b0): {b0:.4f}")
print(f"Coefficient (b1): {b1:.4f}")

# Predict for student studying 3.8 hours
hours_new = np.array([[3.8]])
prob = model.predict_proba(hours_new)[0][1]
prediction = model.predict(hours_new)[0]

print(f"Prediction for 3.8 hours:")
print(f"Log-odds: {b0 + b1*3.8:.4f}")
print(f"Probability: {prob:.4f}")
print(f"Result: {'Pass' if prediction==1 else 'Fail'}")"""

# Run simulation for output
from sklearn.linear_model import LogisticRegression
X_ex1 = np.array([1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 5.5, 6.0]).reshape(-1, 1)
y_ex1 = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1])
model_ex1 = LogisticRegression(C=10.0, random_state=42)
model_ex1.fit(X_ex1, y_ex1)
b0_ex1 = model_ex1.intercept_[0]
b1_ex1 = model_ex1.coef_[0][0]
hours_new = 3.8
prob_ex1 = model_ex1.predict_proba([[hours_new]])[0][1]
log_odds_ex1 = b0_ex1 + b1_ex1 * hours_new

ex1_output_text = f"Intercept (b0): {b0_ex1:.4f}\\nCoefficient (b1): {b1_ex1:.4f}\\nPrediction for 3.8 hours:\\nLog-odds: {log_odds_ex1:.4f}\\nProbability: {prob_ex1:.4f}\\nResult: {'Pass' if prob_ex1 > 0.5 else 'Fail'}"

print("Generating CH3_ex1_prediction plot...")
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
plt.scatter(X_ex1, y_ex1, color='black', s=80, label='Data', zorder=3)
x_range = np.linspace(0, 7, 100)
p_range = 1 / (1 + np.exp(-(b0_ex1 + b1_ex1 * x_range)))
plt.plot(x_range, p_range, color='#0072b2', linewidth=3, label='Logistic Model')

# Highlight prediction
plt.axvline(hours_new, color='red', linestyle='--', alpha=0.5)
plt.plot(hours_new, prob_ex1, 'r*', markersize=15, label=f'Predict (3.8h) = {prob_ex1:.2f}', zorder=5)

plt.title('Study Hours vs Probability of Passing', fontsize=14)
plt.xlabel('Hours Studied', fontsize=12)
plt.ylabel('Probability (Pass)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ex1_plot.png", dpi=150)
plt.close()

print("Generating CH3_ex1_combined.png...")
render_combined_window(ex1_code_text, ex1_output_text, "CH3_ex1_combined.png", title="predict_pass.py")


# Example 2: Heart Disease (Multi-variable)
# ------------------------------------------
ex2_code_text = """import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data: Age, Cholesterol, Disease (1=Yes, 0=No)
data = {
    'Age': [25, 30, 45, 50, 60, 35, 40, 55, 65, 58],
    'Chol': [180, 190, 220, 240, 260, 200, 210, 250, 280, 230],
    'Disease': [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)

# Fit model
X = df[['Age', 'Chol']]
y = df['Disease']
model = LogisticRegression(C=1e5, random_state=42)
model.fit(X, y)

print(f"Intercept: {model.intercept_[0]:.4f}")
print(f"Coefficients: {model.coef_[0]}")

# Predict for Age 52, Chol 235
new_case = [[52, 235]]
prob = model.predict_proba(new_case)[0][1]
print(f"Patient (Age 52, Chol 235):")
print(f"Disease Probability: {prob:.4f}")"""

# Run simulation for output
df_ex2 = pd.DataFrame({
    'Age': [25, 30, 45, 50, 60, 35, 40, 55, 65, 58],
    'Chol': [180, 190, 220, 240, 260, 200, 210, 250, 280, 230],
    'Disease': [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
})
X_ex2 = df_ex2[['Age', 'Chol']]
y_ex2 = df_ex2['Disease']
model_ex2 = LogisticRegression(C=1e5, random_state=42)
model_ex2.fit(X_ex2, y_ex2)
b0_ex2 = model_ex2.intercept_[0]
b1_ex2, b2_ex2 = model_ex2.coef_[0]

new_age = 52
new_chol = 235
# sklearn predict_proba expects array-like, make sure to add dataframe labels if using columns
# or just numpy array. The code text uses list of list which becomes array.
# Let's match the code text exactly in simulation logic.
prob_ex2 = model_ex2.predict_proba([[new_age, new_chol]])[0][1]

ex2_output_text = f"Intercept: {b0_ex2:.4f}\\nCoefficients: [{b1_ex2:.4f} {b2_ex2:.4f}]\\nPatient (Age 52, Chol 235):\\nDisease Probability: {prob_ex2:.4f}"

print("Generating CH3_ex2_prediction plot...")
# For 2D features, let's plot decision boundary
plt.figure(figsize=(8, 6))
plt.style.use('bmh')

# Scatter existing data
plt.scatter(df_ex2[df_ex2.Disease==0]['Age'], df_ex2[df_ex2.Disease==0]['Chol'], 
            color='blue', label='No Disease', s=80, edgecolors='k')
plt.scatter(df_ex2[df_ex2.Disease==1]['Age'], df_ex2[df_ex2.Disease==1]['Chol'], 
            color='red', label='Disease', s=80, edgecolors='k')

# Plot prediction point
plt.scatter(new_age, new_chol, color='green', marker='X', s=200, label='New Patient', zorder=5, edgecolors='white')

# Decision Boundary
# 0 = b0 + b1*x1 + b2*x2  =>  x2 = -(b0 + b1*x1)/b2
x1_vals = np.array([20, 70])
x2_vals = -(b0_ex2 + b1_ex2 * x1_vals) / b2_ex2
plt.plot(x1_vals, x2_vals, '--', color='gray', label='Decision Boundary (P=0.5)')

# Gradient background
x_min, x_max = 20, 70
y_min, y_max = 150, 300
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
# Ensure we predict with correct feature names or structure
Z = model_ex2.predict(pd.DataFrame(np.c_[xx.ravel(), yy.ravel()], columns=['Age', 'Chol']))
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.1, cmap=plt.cm.coolwarm)

plt.title('Heart Disease Prediction Analysis', fontsize=14)
plt.xlabel('Age (Years)', fontsize=12)
plt.ylabel('Cholesterol (mg/dL)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ex2_plot.png", dpi=150)
plt.close()

print("Generating CH3_ex2_combined.png...")
render_combined_window(ex2_code_text, ex2_output_text, "CH3_ex2_combined.png", title="health_predict.py")


# ==========================================
# Chapter 3 Assignments
# ==========================================

# Assignment 1: Promotion Prediction (Exp vs Promoted)
# ----------------------------------------------------
ass1_code_text = """import numpy as np
from sklearn.linear_model import LogisticRegression

# Data: Years Experience vs Promoted(1)/Not(0)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1])

model = LogisticRegression(C=10.0, random_state=42)
model.fit(X, y)

b0 = model.intercept_[0]
b1 = model.coef_[0][0]
print(f"Intercept (b0): {b0:.4f}")
print(f"Coefficient (b1): {b1:.4f}")

# Predict for 5.5 years
new_x = np.array([[5.5]])
prob = model.predict_proba(new_x)[0][1]
print(f"Prob(Promoted | 5.5yrs): {prob:.4f}")"""

# Run Ass1
X_a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y_a1 = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1])
m_a1 = LogisticRegression(C=10.0, random_state=42).fit(X_a1, y_a1)
b0_a1 = m_a1.intercept_[0]
b1_a1 = m_a1.coef_[0][0]
prob_a1 = m_a1.predict_proba([[5.5]])[0][1]
ass1_out = f"Intercept (b0): {b0_a1:.4f}\\nCoefficient (b1): {b1_a1:.4f}\\nProb(Promoted | 5.5yrs): {prob_a1:.4f}"

print("Generating CH3_ass1_plot.png...")
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
plt.scatter(X_a1, y_a1, color='blue', s=80, label='Data', zorder=3)
xr_a1 = np.linspace(0, 11, 100)
pr_a1 = 1 / (1 + np.exp(-(b0_a1 + b1_a1 * xr_a1)))
plt.plot(xr_a1, pr_a1, color='orange', linewidth=3, label='Logistic Model')
plt.axvline(5.5, color='gray', linestyle='--')
plt.plot(5.5, prob_a1, 'r*', markersize=15, label=f'Predict(5.5)={prob_a1:.2f}', zorder=5)
plt.title('Exp vs Promotion', fontsize=14)
plt.xlabel('Years Experience')
plt.ylabel('Probability')
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ass1_plot.png", dpi=150)
plt.close()

render_combined_window(ass1_code_text, ass1_out, "CH3_ass1_combined.png", title="ass1_promo.py")


# Assignment 2: Machine Failure (Temp vs Failure)
# -----------------------------------------------
ass2_code_text = """import numpy as np
from sklearn.linear_model import LogisticRegression

# Data: Temperature (C) vs Failure(1)/OK(0)
X = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1, 1])

model = LogisticRegression(C=10.0, random_state=42)
model.fit(X, y)

print(f"Intercept: {model.intercept_[0]:.4f}")
print(f"Coef (Temp): {model.coef_[0][0]:.4f}")

# Predict for Temp 72C
prob = model.predict_proba([[72]])[0][1]
print(f"Prob(Fail | 72C): {prob:.4f}")"""

# Run Ass2
X_a2 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95]).reshape(-1, 1)
y_a2 = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1, 1])
m_a2 = LogisticRegression(C=10.0, random_state=42).fit(X_a2, y_a2)
b0_a2 = m_a2.intercept_[0]
b1_a2 = m_a2.coef_[0][0]
prob_a2 = m_a2.predict_proba([[72]])[0][1]
ass2_out = f"Intercept: {b0_a2:.4f}\\nCoef (Temp): {b1_a2:.4f}\\nProb(Fail | 72C): {prob_a2:.4f}"

print("Generating CH3_ass2_plot.png...")
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
plt.scatter(X_a2, y_a2, color='green', s=80, label='Data', zorder=3)
xr_a2 = np.linspace(45, 100, 100)
pr_a2 = 1 / (1 + np.exp(-(b0_a2 + b1_a2 * xr_a2)))
plt.plot(xr_a2, pr_a2, color='red', linewidth=3, label='Logistic Model')
plt.axvline(72, color='gray', linestyle='--')
plt.plot(72, prob_a2, 'k*', markersize=15, label=f'Predict(72)={prob_a2:.2f}', zorder=5)
plt.title('Temp vs Machine Failure', fontsize=14)
plt.xlabel('Temperature (C)')
plt.ylabel('Probability')
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ass2_plot.png", dpi=150)
plt.close()

render_combined_window(ass2_code_text, ass2_out, "CH3_ass2_combined.png", title="ass2_machine.py")


# Assignment 3: Customer Purchase (Age, Salary)
# ---------------------------------------------
ass3_code_text = """import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data: Age, Salary(k), Purchased(1)
data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 22, 48],
    'Salary': [20000, 25000, 30000, 80000, 35000, 90000, 40000, 95000, 22000, 85000],
    'Purchased': [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['Age', 'Salary']]
y = df['Purchased']
model = LogisticRegression(C=1e5, solver='liblinear', random_state=42)
model.fit(X, y)

print(f"Int: {model.intercept_[0]:.4f}")
print(f"Coefs: {model.coef_[0]}")

# Predict: Age 42, Salary 75000
new_cust = [[42, 75000]]
prob = model.predict_proba(new_cust)[0][1]
print(f"Prob(Purchase): {prob:.4f}")"""

# Run Ass3
df_a3 = pd.DataFrame({
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 22, 48],
    'Salary': [20000, 25000, 30000, 80000, 35000, 90000, 40000, 95000, 22000, 85000],
    'Purchased': [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
})
X_a3 = df_a3[['Age', 'Salary']]
y_a3 = df_a3['Purchased']
m_a3 = LogisticRegression(C=1e5, solver='liblinear', random_state=42).fit(X_a3, y_a3)
b0_a3 = m_a3.intercept_[0]
b1_a3, b2_a3 = m_a3.coef_[0]
prob_a3 = m_a3.predict_proba([[42, 75000]])[0][1]
ass3_out = f"Int: {b0_a3:.4f}\\nCoefs: [{b1_a3:.4f} {b2_a3:.4f}]\\nProb(Purchase): {prob_a3:.4f}"

print("Generating CH3_ass3_plot.png...")
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
groups = df_a3.groupby('Purchased')
for name, group in groups:
    plt.plot(group.Age, group.Salary, marker='o', linestyle='', ms=12, label=f'Buy={name}')
# Decision Boundary: b0 + b1*x1 + b2*x2 = 0 => x2 = -(b0 + b1*x1)/b2
xx = np.linspace(15, 60, 100)
yy = -(b0_a3 + b1_a3 * xx) / b2_a3
plt.plot(xx, yy, 'k--', label='Boundary')
plt.plot(42, 75000, 'rX', ms=15, label='New Customer')
plt.title('Purchase Prediction', fontsize=14)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ass3_plot.png", dpi=150)
plt.close()

render_combined_window(ass3_code_text, ass3_out, "CH3_ass3_combined.png", title="ass3_market.py")


# Assignment 4: Loan Default (5 Variables)
# ----------------------------------------
ass4_code_text = """import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data: Score, Income(k), DTI(%), Emp(Yrs), Loan(k), Default(1)
data = {
    'Score': [800, 780, 750, 700, 650, 600, 550, 500, 450, 400],
    'Income': [80, 75, 70, 60, 55, 45, 40, 35, 30, 40],
    'DTI':    [5,  8,  10, 12, 15, 20, 25, 30, 35, 40],
    'Emp':    [10, 9,  8,  6,  5,  3,  2,  1,  0,  2],
    'Loan':   [10, 15, 20, 12, 18, 25, 30, 40, 45, 50],
    'Default':[0,  0,  0,  0,  0,  1,  1,  1,  1,  1]
}
df = pd.DataFrame(data)

X = df[['Score', 'Income', 'DTI', 'Emp', 'Loan']]
y = df['Default']
model = LogisticRegression(C=10.0, solver='liblinear', random_state=42)
model.fit(X, y)

print("Coefficients:")
for col, coef in zip(X.columns, model.coef_[0]):
    print(f" {col}: {coef:.4f}")
print(f" Intercept: {model.intercept_[0]:.4f}")

# Predict: Score=620, Inc=50, DTI=18, Emp=4, Loan=22
new_case = [[620, 50, 18, 4, 22]]
prob = model.predict_proba(new_case)[0][1]
print(f"Prob(Default): {prob:.4f}")"""

# Run Ass4 (5 vars)
df_a4 = pd.DataFrame({
    'Score': [800, 780, 750, 700, 650, 600, 550, 500, 450, 400],
    'Income': [80, 75, 70, 60, 55, 45, 40, 35, 30, 40],
    'DTI':    [5,  8,  10, 12, 15, 20, 25, 30, 35, 40],
    'Emp':    [10, 9,  8,  6,  5,  3,  2,  1,  0,  2],
    'Loan':   [10, 15, 20, 12, 18, 25, 30, 40, 45, 50],
    'Default':[0,  0,  0,  0,  0,  1,  1,  1,  1,  1]
})
X_a4 = df_a4[['Score', 'Income', 'DTI', 'Emp', 'Loan']]
y_a4 = df_a4['Default']
m_a4 = LogisticRegression(C=10.0, solver='liblinear', random_state=42).fit(X_a4, y_a4)

coefs_str = ""
for col, coef in zip(X_a4.columns, m_a4.coef_[0]):
    coefs_str += f"{col}: {coef:.4f}\\n"
ass4_out = f"Coefficients:\\n{coefs_str}Intercept: {m_a4.intercept_[0]:.4f}\\n\\nProb(Default): {m_a4.predict_proba([[620, 50, 18, 4, 22]])[0][1]:.4f}"

print("Generating CH3_ass4_plot.png (5 vars code view)...")
# Since 5D data is hard to plot, we visualize 2 main vars (Score vs DTI) for the scatter
# but emphasize it is a Code View mostly
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
groups = df_a4.groupby('Default')
for name, group in groups:
    plt.plot(group.Score, group.DTI, marker='o', linestyle='', ms=12, label=f'Default={name}')
# Simple boundary line for visualization (just approximation)
plt.plot([620], [18], 'rX', ms=15, label='Applicant')
plt.title('Credit Analysis (Score vs DTI)', fontsize=14)
plt.xlabel('Credit Score')
plt.ylabel('Debt-to-Income Ratio (%)')
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ass4_plot.png", dpi=150)
plt.close()

render_combined_window(ass4_code_text, ass4_out, "CH3_ass4_combined.png", title="ass4_loan_complex.py")


# Assignment 5: Ad Click (5 Variables)
# ------------------------------------
ass5_code_text = """import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data: Usage(min), Age, Income(k), SectionTime(min), Male(1)/Fem(0), Click(1)
data = {
    'Usage':   [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Age':     [50, 45, 40, 35, 30, 25, 28, 22, 20, 18],
    'Income':  [30, 35, 40, 45, 55, 60, 65, 70, 80, 85],
    'Time':    [10, 15, 20, 15, 30, 35, 40, 45, 50, 55],
    'Male':    [1,  0,  1,  0,  1,  0,  1,  0,  1,  0],
    'Click':   [1,  1,  1,  1,  0,  0,  0,  0,  0,  0]
}
df = pd.DataFrame(data)

X = df[['Usage', 'Age', 'Income', 'Time', 'Male']]
y = df['Click']
model = LogisticRegression(C=10.0, solver='liblinear', random_state=42)
model.fit(X, y)

print("Coefficients:")
for col, coef in zip(X.columns, model.coef_[0]):
    print(f" {col}: {coef:.4f}")
print(f" Intercept: {model.intercept_[0]:.4f}")

# Predict: Usage=55, Age=38, Inc=50, Time=25, Male=1
new_case = [[55, 38, 50, 25, 1]]
prob = model.predict_proba(new_case)[0][1]
print(f"Prob(Click): {prob:.4f}")"""

# Run Ass5 (5 vars)
df_a5 = pd.DataFrame({
    'Usage':   [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Age':     [50, 45, 40, 35, 30, 25, 28, 22, 20, 18],
    'Income':  [30, 35, 40, 45, 55, 60, 65, 70, 80, 85],
    'Time':    [10, 15, 20, 15, 30, 35, 40, 45, 50, 55],
    'Male':    [1,  0,  1,  0,  1,  0,  1,  0,  1,  0],
    'Click':   [1,  1,  1,  1,  0,  0,  0,  0,  0,  0]
})
X_a5 = df_a5[['Usage', 'Age', 'Income', 'Time', 'Male']]
y_a5 = df_a5['Click']
m_a5 = LogisticRegression(C=10.0, solver='liblinear', random_state=42).fit(X_a5, y_a5)

coefs_str = ""
for col, coef in zip(X_a5.columns, m_a5.coef_[0]):
    coefs_str += f"{col}: {coef:.4f}\\n"
ass5_out = f"Coefficients:\\n{coefs_str}Intercept: {m_a5.intercept_[0]:.4f}\\n\\nProb(Click): {m_a5.predict_proba([[55, 38, 50, 25, 1]])[0][1]:.4f}"

print("Generating CH3_ass5_plot.png (5 vars code view)...")
plt.figure(figsize=(8, 6))
plt.style.use('bmh')
# Visualize Usage vs Age but colored by Click
groups = df_a5.groupby('Click')
for name, group in groups:
    plt.plot(group.Usage, group['Age'], marker='o', linestyle='', ms=12, label=f'Click={name}')
# Simple point for prediction
plt.plot(55, 38, 'mX', ms=15, label='User', zorder=5)
plt.title('Ad Click Analysis (Usage vs Age)', fontsize=14)
plt.xlabel('Daily Usage (Min)')
plt.ylabel('Age (Years)')
plt.legend()
plt.tight_layout()
plt.savefig("CH3_ass5_plot.png", dpi=150)
plt.close()

render_combined_window(ass5_code_text, ass5_out, "CH3_ass5_combined.png", title="ass5_ad_complex.py")
