import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set font for Thai support (if available, otherwise fallback)
plt.rcParams['font.family'] = 'sans-serif'

def draw_adam_workflow(output_path):
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Styles
    box_style = dict(boxstyle='round,pad=0.5', facecolor='#e6f3ff', edgecolor='#004d99', linewidth=2)
    arrow_style = dict(arrowstyle='-|>', color='#004d99', lw=2)
    font_header = {'fontsize': 14, 'fontweight': 'bold', 'color': '#003366'}
    font_math = {'fontsize': 12, 'color': '#003366'}

    # 1. Start / Input
    ax.text(5, 11, 'Start: Initialization', ha='center', va='center', bbox=box_style, fontdict=font_header)
    ax.text(5, 10.3, r'Set: $\beta_t = 0, m_0 = 0, v_0 = 0, t = 0$', ha='center', fontdict=font_math)

    # Arrow 1
    ax.annotate('', xy=(5, 9.5), xytext=(5, 10.8), arrowprops=arrow_style)

    # 2. Compute Gradient
    ax.text(5, 9, 'Step 1: Compute Gradient', ha='center', va='center', bbox=box_style, fontdict=font_header)
    ax.text(5, 8.3, r'$\mathbf{g}_t = \mathbf{X}^T(\mathbf{p}_t - \mathbf{y})$', ha='center', fontdict=font_math)

    # Arrow 2
    ax.annotate('', xy=(5, 7.5), xytext=(5, 8.8), arrowprops=arrow_style)

    # 3. Update Moments
    ax.text(5, 7, 'Step 2: Update Moments', ha='center', va='center', bbox=box_style, fontdict=font_header)
    ax.text(5, 6.3, r'$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$' + '\n' + r'$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$', ha='center', fontdict=font_math)

    # Arrow 3
    ax.annotate('', xy=(5, 5.3), xytext=(5, 6.8), arrowprops=arrow_style)

    # 4. Bias Correction
    ax.text(5, 4.8, 'Step 3: Bias Correction', ha='center', va='center', bbox=box_style, fontdict=font_header)
    ax.text(5, 4.1, r'$\hat{m}_t = m_t / (1 - \beta_1^t)$' + '\n' + r'$\hat{v}_t = v_t / (1 - \beta_2^t)$', ha='center', fontdict=font_math)

    # Arrow 4
    ax.annotate('', xy=(5, 3.1), xytext=(5, 4.6), arrowprops=arrow_style)

    # 5. Update Parameters
    ax.text(5, 2.6, 'Step 4: Update Parameters', ha='center', va='center', bbox=box_style, fontdict=font_header)
    ax.text(5, 1.9, r'$\beta_{t+1} = \beta_t - \alpha \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$', ha='center', fontdict=font_math)

    # Arrow 5
    ax.annotate('', xy=(5, 0.7), xytext=(5, 2.4), arrowprops=arrow_style)

    # 6. End / Iteration
    ax.text(5, 0.4, 'Repeat until Convergence', ha='center', va='center', bbox=box_style, fontdict=font_header)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_adam_workflow("CH3_adam_workflow.png")
