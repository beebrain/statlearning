import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import os

# Load Thai Font (Absolute Path)
font_path = r"d:\OnedrivePM\OneDrive - Uttaradit Rajabhat University\URU\1_Books\6_Stat Learning\TH Sarabun New.TTF"
if not os.path.exists(font_path):
    # Fallback for flexibility
    font_path = "TH Sarabun New.TTF"
thai_font = font_manager.FontProperties(fname=font_path)

def generate_premium_newton_workflow(output_path):
    # Set up the figure with a "Safe for eyes" palette
    fig = plt.figure(figsize=(11, 14), facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    # Define Colors (Muted, Professional)
    colors = {
        'bg': '#FFFFFF',
        'border': '#D1D9E6',
        'text_dark': '#2E3440',
        'text_light': '#4C566A',
        'accent_1': '#5E81AC',  # Muted Blue
        'accent_2': '#81A1C1',  # Lighter Blue
        'accent_3': '#A3BE8C',  # Sage Green 
        'accent_4': '#EBCB8B',  # Muted Amber
        'line': '#88C0D0'       # Soft Cyan
    }

    # Helper to draw a shadow-like card
    def draw_card(ax, x, y, width, height, color, title, content, step_num):
        # Background card
        rect = patches.FancyBboxPatch((x, y), width, height, 
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     linewidth=1, edgecolor=colors['border'], facecolor='white',
                                     zorder=1)
        ax.add_patch(rect)
        
        # Step Number Circle
        circle = plt.Circle((x + 0.05, y + height - 0.03), 0.025, color=color, zorder=2)
        ax.add_patch(circle)
        ax.text(x + 0.05, y + height - 0.03, str(step_num), color='white', weight='bold',
                ha='center', va='center', fontsize=14, zorder=3)

        # Title
        ax.text(x + 0.09, y + height - 0.03, title, va='center', ha='left',
                color=colors['text_dark'], weight='bold', fontsize=18, fontproperties=thai_font, zorder=3)
        
        # Content
        ax.text(x + 0.05, y + height - 0.08, content, va='top', ha='left',
                color=colors['text_light'], fontsize=16, fontproperties=thai_font, zorder=3, linespacing=1.4)

    # Coordinates and Content
    steps = [
        {"title": "กำหนดค่าเริ่มต้น (Initialization)", 
         "color": colors['accent_2'],
         "text": r"กำหนดค่าพารามิเตอร์เริ่มต้น $\beta^{(0)}$ (เวกเตอร์ศูนย์)" + "\n" + r"และกำหนดระดับความคลาดเคลื่อน $\epsilon$ (เช่น $10^{-6}$)"},
        {"title": "คำนวณความน่าจะเป็น (Probability)", 
         "color": colors['accent_1'],
         "text": r"คำนยณความน่าจะเป็นทำนายสำหรับข้อมูลแต่ละหน่วย:" + "\n" + r"$p_i = \sigma(x_i^T \beta^{(t)}) = \frac{1}{1 + e^{-x_i^T \beta^{(t)}}}$"},
        {"title": "คำนวณ Score Function (First Derivative)", 
         "color": colors['accent_1'],
         "text": r"หาเวกเตอร์เกรเดียนต์ของฟังก์ชัน Log-Likelihood:" + "\n" + r"$S(\beta^{(t)}) = X^T(y - p)$"},
        {"title": "คำนวณเมทริกซ์ Hessian (Second Derivative)", 
         "color": colors['accent_1'],
         "text": r"หาค่าความโค้งผ่านเมทริกซ์อนุพันธ์อันดับสอง:" + "\n" + r"$H(\beta^{(t)}) = -X^T W X$ โดยที่ $W = \text{diag}(p_i(1-p_i))$"},
        {"title": "อัปเดตพารามิเตอร์ (Newton Update)", 
         "color": colors['accent_4'],
         "text": r"ปรับแก้ค่าพารามิเตอร์ด้วยแนวคิดนิวตัน-ราฟสัน:" + "\n" + r"$\beta^{(t+1)} = \beta^{(t)} - H(\beta^{(t)})^{-1} S(\beta^{(t)})$"},
        {"title": "ตรวจสอบการลู่เข้า (Convergence Check)", 
         "color": colors['accent_3'],
         "text": r"ตรวจสอบเงื่อนไข $||\beta^{(t+1)} - \beta^{(t)}|| < \epsilon$" + "\n" + r"หากลู่เข้าแล้วให้หยุดการทำงาน หากไม่ให้เริ่มรอบใหม่ ($t = t+1$)"}
    ]

    # Draw Cards
    current_y = 0.82
    spacing = 0.14
    card_width = 0.9
    card_height = 0.11
    x_start = 0.05

    for i, step in enumerate(steps):
        draw_card(ax, x_start, current_y, card_width, card_height, 
                  step['color'], step['title'], step['text'], i + 1)
        
        # Connection Arrow
        if i < len(steps) - 1:
            ax.annotate("", xy=(x_start + 0.5, current_y - 0.015), 
                        xytext=(x_start + 0.5, current_y + 0.01),
                        arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.6', 
                                      color=colors['border'], linewidth=2),
                        zorder=0)
        current_y -= spacing

    # Result Box (Special Card)
    last_y = current_y + 0.02
    res_rect = patches.FancyBboxPatch((x_start, last_y), card_width, 0.06, 
                                     boxstyle="round,pad=0.02,rounding_size=0.03",
                                     linewidth=2, edgecolor=colors['accent_3'], facecolor='#F6FFF8',
                                     zorder=1)
    ax.add_patch(res_rect)
    ax.text(x_start + 0.5, last_y + 0.03, r"ผลลัพธ์: ได้ค่าประมาณ $\hat{\beta}$ ที่ให้ความน่าจะเป็นสูงสุด (MLE)", 
            ha='center', va='center', color=colors['text_dark'], weight='bold', 
            fontsize=18, fontproperties=thai_font, zorder=3)

    # Title Section
    title_rect = patches.Rectangle((0, 0.93), 1, 0.07, facecolor='#ECEFF4', alpha=0.5, zorder=0)
    ax.add_patch(title_rect)
    plt.text(0.5, 0.965, "ขั้นตอนการทำงานของอัลกอริทึม Newton-Raphson", 
             ha='center', va='center', fontsize=26, fontproperties=thai_font, weight='bold', color='#2E3440')
    plt.text(0.5, 0.94, "(Newton-Raphson Workflow for Logistic Regression)", 
             ha='center', va='center', fontsize=14, color='#4C566A', style='italic')

    # Footer
    plt.text(0.95, 0.02, "Stat Learning Book - CH3 Regression Infographic", 
             ha='right', va='bottom', fontsize=10, color='#D8DEE9')

    # Save
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_premium_newton_workflow("CH3_NewtonRaphson_Workflow.png")
    print("Premium Newton-Raphson workflow image generated at CH3_NewtonRaphson_Workflow.png")
