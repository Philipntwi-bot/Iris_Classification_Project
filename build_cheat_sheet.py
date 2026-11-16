import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def create_cheat_sheet():
    doc = Document()

    # Set Margins to 0.75 in for compact professional feel
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Helper styling functions
    def set_cell_background(cell, fill_hex):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'''
            <w:tcMar {nsdecls("w")}>
                <w:top w:w="{top}" w:type="dxa"/>
                <w:bottom w:w="{bottom}" w:type="dxa"/>
                <w:left w:w="{left}" w:type="dxa"/>
                <w:right w:w="{right}" w:type="dxa"/>
            </w:tcMar>
        ''')
        tcPr.append(tcMar)

    # ------------------ HEADER TITLE ------------------
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_table.cell(0, 0)
    set_cell_background(cell, "0B132B") # Deep Navy
    set_cell_margins(cell, top=200, bottom=200, left=250, right=250)

    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p.add_run("PENTECOST UNIVERSITY • FACULTY OF SCIENCE & COMPUTING\n")
    r0.font.name = "Calibri"
    r0.font.size = Pt(11)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(212, 175, 55) # Gold

    r1 = p.add_run("ORAL DEFENSE & VIVA VOCE CHEAT SHEET\n")
    r1.font.name = "Arial Black"
    r1.font.size = Pt(17)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(255, 255, 255)

    r2 = p.add_run("IRIS FLOWER MACHINE LEARNING CLASSIFICATION ENGINE\n")
    r2.font.name = "Calibri"
    r2.font.size = Pt(12)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(56, 189, 248) # Sky blue

    r3 = p.add_run("Candidate: Philip Antwi  |  ID: PUIT24120002  |  BSc Information Technology Level 400")
    r3.font.name = "Calibri"
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = RGBColor(203, 213, 225) # Slate

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ QUICK LINKS CALLOUT ------------------
    links_table = doc.add_table(rows=1, cols=1)
    links_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    lcell = links_table.cell(0, 0)
    set_cell_background(lcell, "F1F5F9")
    set_cell_margins(lcell, top=100, bottom=100, left=150, right=150)
    lp = lcell.paragraphs[0]
    lp.paragraph_format.space_after = Pt(0)
    lr1 = lp.add_run("🔗 PRODUCTION PROJECT REPOSITORIES & URLS:\n")
    lr1.font.bold = True
    lr1.font.size = Pt(10)
    lr1.font.color.rgb = RGBColor(15, 23, 42)
    lr2 = lp.add_run("• Live Web Application: https://iris-classification-project-rk73.vercel.app/\n")
    lr2.font.size = Pt(9.5)
    lr3 = lp.add_run("• Alternative Production: https://iris-classification-project-eight.vercel.app/\n")
    lr3.font.size = Pt(9.5)
    lr4 = lp.add_run("• GitHub Source Code: https://github.com/Philipntwi-bot/Iris_Classification_Project")
    lr4.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ SECTION 1: ELEVATOR PITCH ------------------
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(8)
    h1.paragraph_format.space_after = Pt(2)
    hr1 = h1.add_run("1. THE 30-SECOND 'ELEVATOR PITCH' (HOW TO OPEN YOUR DEFENSE)")
    hr1.font.name = "Arial"
    hr1.font.size = Pt(12)
    hr1.font.bold = True
    hr1.font.color.rgb = RGBColor(15, 23, 42)

    box1 = doc.add_table(rows=1, cols=1)
    box1.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1 = box1.cell(0, 0)
    set_cell_background(c1, "E0F2FE") # Soft light blue
    set_cell_margins(c1, top=120, bottom=120, left=160, right=160)
    bp1 = c1.paragraphs[0]
    bp1.paragraph_format.space_after = Pt(0)
    br1 = bp1.add_run("🗣️ WHAT TO SAY VERBATIM IF ASKED 'TELL US ABOUT YOUR PROJECT':\n")
    br1.font.bold = True
    br1.font.size = Pt(10)
    br1.font.color.rgb = RGBColor(3, 105, 161)
    br2 = bp1.add_run(
        '"Good day, respected examiners. My project is an end-to-end Machine Learning botanical classification system '
        'built on Fisher’s canonical Iris benchmark. Using Scikit-Learn in Python, I trained a Multinomial Logistic Regression '
        'model with Softmax activation and L-BFGS optimization. The model is deployed as a serverless microservice on Vercel '
        'with a real-time responsive web interface. It achieves 96.67% test accuracy and a Macro F1-Score of 0.97. '
        'To enable deep morphometric analysis, the application features a live 2D scatter plot in Sepal Space and Petal Space '
        'with real-time target tracking and an inference latency under 15 milliseconds."'
    )
    br2.font.italic = True
    br2.font.size = Pt(10)
    br2.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ SECTION 2: TOP 5 LECTURER DEFENSE QUESTIONS ------------------
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)
    hr2 = h2.add_run("2. TOP 5 TOUGH QUESTIONS LECTURERS LOVE TO ASK & YOUR WINNING ANSWERS")
    hr2.font.name = "Arial"
    hr2.font.size = Pt(12)
    hr2.font.bold = True
    hr2.font.color.rgb = RGBColor(15, 23, 42)

    qa_list = [
        (
            "QUESTION 1: What does 'Inference' mean, and how does it happen in your project?",
            "WHAT TO EXPLAIN:",
            "• Distinction: 'Training' is offline where the model computes gradients and learns weights from 120 training flowers.\n"
            "• 'Inference' is the live operational phase where the frozen model processes unseen user inputs.\n"
            "• The 4 input values (Sepal Length, Sepal Width, Petal Length, Petal Width) form a 4-dimensional tensor X = [x1, x2, x3, x4].\n"
            "• The model computes the linear logits zk = w_k • X + bk for all 3 classes, then applies the Softmax function: P(yk|X) = exp(zk) / Σ exp(zj).\n"
            "• Telemetry: Our Vercel serverless function executes this full inference cycle in approximately 12 to 14 milliseconds."
        ),
        (
            "QUESTION 2: Why did you plot Sepal Length against Sepal Width?",
            "WHAT TO EXPLAIN:",
            "• Biological Context: Sepals form the outer protective calyx of the flower, while petals form the inner corolla.\n"
            "• Linear Separability: In 2D Sepal space, Iris Setosa is completely isolated and linearly separable (high sepal width > 3.0 cm, shorter length).\n"
            "• Morphological Overlap: However, Iris Versicolor and Iris Virginica overlap significantly in Sepal dimensions alone.\n"
            "• Mathematical Justification: This plot visually proves to botanists why a simple 2D sepal rule is insufficient and why a 4D feature model incorporating Petal Length and Petal Width is mathematically required to reach 96.67% accuracy."
        ),
        (
            "QUESTION 3: What is the F1-Score and why did you use it instead of just Accuracy?",
            "WHAT TO EXPLAIN:",
            "• Flaw of Accuracy: Simple accuracy only counts total correct predictions. If a dataset is imbalanced or a model generates false alarms, accuracy conceals the failure.\n"
            "• Precision: Measures exactness: Out of all flowers predicted as Virginica, how many were truly Virginica? (Minimizes False Positives).\n"
            "• Recall: Measures completeness: Out of all actual Virginicas, how many did the model detect? (Minimizes False Negatives).\n"
            "• Harmonic Mean: F1 = 2 × (Precision × Recall) / (Precision + Recall). The harmonic mean severely penalizes extreme divergence between precision and recall.\n"
            "• Our Exact Scores: Macro F1 is 0.97 (Setosa = 1.00, Versicolor = 0.95, Virginica = 0.95), demonstrating high-confidence, balanced performance."
        ),
        (
            "QUESTION 4: Why did you choose Multinomial Logistic Regression over a Deep Neural Network or SVM?",
            "WHAT TO EXPLAIN:",
            "• Principle of Parsimony (Occam’s Razor): The Iris dataset has 150 rows and 4 numerical features. Deep neural networks have thousands of parameters and will overfit or require massive compute overhead.\n"
            "• Convex Optimization: Logistic Regression with L-BFGS is mathematically convex, guaranteeing convergence to the global optimum without getting trapped in local minima.\n"
            "• Calibrated Probabilities: Softmax outputs true probabilistic confidence scores that sum to 1.0 (100%), allowing clear risk assessment in botanical categorization."
        ),
        (
            "QUESTION 5: What happens if a user submits negative values or extreme outliers?",
            "WHAT TO EXPLAIN:",
            "• Input Boundary Clamping: The web app UI enforces min and max constraints on sliders (e.g., Sepal Length clamped between 4.3 and 7.9 cm).\n"
            "• Server-Side Validation: In api/predict.py, incoming JSON payloads are typed and validated before reaching the Scikit-Learn pipeline to prevent runtime injection or NaN tensor exceptions.\n"
            "• Botanical Realism: This ensures the system operates strictly within physically viable morphometric distributions."
        )
    ]

    for q, label, ans in qa_list:
        q_tbl = doc.add_table(rows=2, cols=1)
        q_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Header Row
        qc_top = q_tbl.cell(0, 0)
        set_cell_background(qc_top, "1E293B") # Dark slate
        set_cell_margins(qc_top, top=80, bottom=80, left=140, right=140)
        qp_top = qc_top.paragraphs[0]
        qp_top.paragraph_format.space_after = Pt(0)
        qr_top = qp_top.add_run(q)
        qr_top.font.bold = True
        qr_top.font.size = Pt(10)
        qr_top.font.color.rgb = RGBColor(255, 255, 255)

        # Answer Row
        qc_bot = q_tbl.cell(1, 0)
        set_cell_background(qc_bot, "F8FAFC") # Crisp off-white
        set_cell_margins(qc_bot, top=100, bottom=100, left=140, right=140)
        qp_bot = qc_bot.paragraphs[0]
        qp_bot.paragraph_format.space_after = Pt(0)
        
        ar_lbl = qp_bot.add_run(label + "\n")
        ar_lbl.font.bold = True
        ar_lbl.font.size = Pt(9.5)
        ar_lbl.font.color.rgb = RGBColor(37, 99, 235) # Blue

        ar_txt = qp_bot.add_run(ans)
        ar_txt.font.size = Pt(9.5)
        ar_txt.font.color.rgb = RGBColor(30, 41, 59)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ SECTION 3: NUMERICAL PERFORMANCE CHEAT TABLE ------------------
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(8)
    h3.paragraph_format.space_after = Pt(4)
    hr3 = h3.add_run("3. EXACT NUMERICAL PERFORMANCE MATRIX (MEMORIZE THESE 6 NUMBERS)")
    hr3.font.name = "Arial"
    hr3.font.size = Pt(12)
    hr3.font.bold = True
    hr3.font.color.rgb = RGBColor(15, 23, 42)

    # 5 rows x 5 cols table
    tbl = doc.add_table(rows=5, cols=5)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    headers = ["Class / Category", "Precision", "Recall", "F1-Score", "Test Samples (Support)"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        set_cell_background(cell, "0F172A")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ["Iris Setosa", "1.00 (100%)", "1.00 (100%)", "1.00 (100%)", "10 / 10 correct"],
        ["Iris Versicolor", "1.00 (100%)", "0.90 (90%)", "0.95 (95%)", "9 / 10 (1 border error)"],
        ["Iris Virginica", "0.91 (91%)", "1.00 (100%)", "0.95 (95%)", "10 / 10 detected"],
        ["OVERALL / MACRO AVG", "0.97 (97%)", "0.97 (97%)", "0.97 (97%)", "29 / 30 = 96.67% Acc."]
    ]

    for row_idx, row_data in enumerate(data, start=1):
        bg = "F1F5F9" if row_idx % 2 == 1 else "FFFFFF"
        if row_idx == 4:
            bg = "FEF08A" # Highlight total row
        for col_idx, val in enumerate(row_data):
            cell = tbl.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            if col_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(9)
            if row_idx == 4 or col_idx == 0:
                r.font.bold = True
            r.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ SECTION 4: ARCHITECTURE & DEPLOYMENT TELEMETRY ------------------
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(8)
    h4.paragraph_format.space_after = Pt(4)
    hr4 = h4.add_run("4. SYSTEM ARCHITECTURE & PRODUCTION DEPLOYMENT SUMMARY")
    hr4.font.name = "Arial"
    hr4.font.size = Pt(12)
    hr4.font.bold = True
    hr4.font.color.rgb = RGBColor(15, 23, 42)

    arch_p = doc.add_paragraph()
    arch_p.paragraph_format.line_spacing = 1.15
    arch_p.paragraph_format.space_after = Pt(4)
    
    arch_points = [
        ("• Machine Learning Pipeline: ", "Scikit-Learn 1.4+, Multinomial Logistic Regression with L-BFGS solver, max_iter=200, trained on 80/20 stratified split."),
        ("• Serialization & Artifacts: ", "Pretrained model weights serialized via Python pickle (iris_model.pkl), stored within the serverless microservice root."),
        ("• Serverless Cloud Architecture: ", "Vercel Serverless Functions running Python 3.10 runtime (api/predict.py) with automated horizontal scaling and zero cold-start latency (<15 ms)."),
        ("• Interactive Frontend Visualization: ", "Single-Page Application (SPA) built with vanilla HTML5, Canvas API (dynamic 150-specimen point rendering), and Glassmorphism CSS."),
        ("• Continuous Integration & Deployment (CI/CD): ", "Automated deployment pipeline synced with GitHub (Philipntwi-bot/Iris_Classification_Project) directly targeting Vercel Production.")
    ]

    for title, desc in arch_points:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r_t = p.add_run(title)
        r_t.font.bold = True
        r_t.font.size = Pt(9.5)
        r_t.font.color.rgb = RGBColor(15, 23, 42)
        r_d = p.add_run(desc)
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = RGBColor(51, 65, 85)

    # ------------------ FOOTER SIGNATURE ------------------
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    footer_p = doc.add_paragraph()
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer_p.add_run("Prepared for Philip Antwi (PUIT24120002) • Pentecost University • Faculty of Science & Computing\nStrictly Confidential Student Defense Guide • Keep for Personal Presentation Use")
    fr.font.size = Pt(8.5)
    fr.font.italic = True
    fr.font.color.rgb = RGBColor(100, 116, 139)

    out_path = r"C:\Users\User\OneDrive\Desktop\MY IA FOR ARTIFICIAL INTELLIGENCE\Iris_Classification_Project\ORAL_DEFENSE_CHEAT_SHEET.docx"
    doc.save(out_path)
    print("Saved docx to:", out_path)

if __name__ == "__main__":
    create_cheat_sheet()
