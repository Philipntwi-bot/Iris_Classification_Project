# 🌺 NEURAL-IRIS AI // Botanical Machine Learning Classifier

**Student:** Philip Antwi  
**Student ID:** PUIT24120002  
**Level:** 400  
**Programme:** BSc Information Technology  
**Institution:** Pentecost University, Accra, Ghana  
**Live Production Web App:** [https://iris-classification-project.vercel.app](https://iris-classification-project.vercel.app)  
**☁️ Vercel Console:** [https://vercel.com/philipntwi-bot/iris-classification-project](https://vercel.com/philipntwi-bot/iris-classification-project)  
**🐙 GitHub Repository:** [https://github.com/Philipntwi-bot/Iris_Classification_Project](https://github.com/Philipntwi-bot/Iris_Classification_Project)  
**⚡ VS Code in Browser:** [https://github.dev/Philipntwi-bot/Iris_Classification_Project](https://github.dev/Philipntwi-bot/Iris_Classification_Project)  

---

## 📌 Executive Summary

**NEURAL-IRIS AI** is a state-of-the-art interactive botanical classification system and machine learning research platform. Built upon Ronald Fisher's benchmark 1936 Iris dataset, the application trains a **Multinomial Logistic Regression** model with L-BFGS optimization to classify Iris specimens into three distinct species based on four physical morphometric dimensions:

1. **Iris setosa** (*Arctic Iris* / *Beachhead Iris*) — Class 0
2. **Iris versicolor** (*Blue Flag* / *Harlequin Blueflag*) — Class 1
3. **Iris virginica** (*Southern Blue Flag* / *Virginia Iris*) — Class 2

The production application features a bioluminescent glassmorphism interface with dual-mode inference (client-side zero-latency softmax math + Vercel serverless Python API), authentic high-resolution botanical photography, interactive 2D scatter plots with real-time cursor tracking, an interactive 3×3 confusion matrix with step-by-step harmonic mean derivations, and a comprehensive oral defense guide for academic review.

---

## 🔬 Dataset & Morphological Dimensions

The system uses Fisher's canonical Iris dataset (`sklearn.datasets.load_iris`):

| Property | Details |
|---|---|
| **Total Samples** | 150 specimens (50 per species, perfectly balanced) |
| **Input Features** | 4 continuous measurements in centimeters (cm) |
| **1. Sepal Length** | 4.3 cm to 7.9 cm (Mean: 5.84 cm) |
| **2. Sepal Width** | 2.0 cm to 4.4 cm (Mean: 3.06 cm) |
| **3. Petal Length** | 1.0 cm to 6.9 cm (Mean: 3.76 cm) |
| **4. Petal Width** | 0.1 cm to 2.5 cm (Mean: 1.20 cm) |
| **Target Classes** | 3 species: Setosa (0), Versicolor (1), Virginica (2) |

---

## 📊 Model Evaluation & Statistical Metrics

The model was split with stratified 80/20 train-test partitioning (120 training samples, 30 unseen test samples):

### 1. Classification Performance Table

| Class / Specimen | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| **Iris setosa** | **1.00 (100%)** | **1.00 (100%)** | **1.00 (100%)** | 10 |
| **Iris versicolor** | **1.00 (100%)** | **0.90 (90%)** | **0.95 (95%)** | 10 |
| **Iris virginica** | **0.91 (91%)** | **1.00 (100%)** | **0.95 (95%)** | 10 |
| **Overall Accuracy** | — | — | **96.67% (29/30)** | 30 |
| **Macro Average** | **0.97** | **0.97** | **0.967** | 30 |
| **Weighted Average** | **0.97** | **0.97** | **0.967** | 30 |

### 2. Multi-Class Confusion Matrix (N = 30)

| Actual \ Predicted | Predicted Setosa | Predicted Versicolor | Predicted Virginica |
|---|---|---|---|
| **Actual Setosa** | **10 (TP)** | 0 | 0 |
| **Actual Versicolor** | 0 | **9 (TP)** | 1 (Misclassified) |
| **Actual Virginica** | 0 | 0 | **10 (TP)** |

* **Analysis:** 29 out of 30 flowers were predicted with flawless accuracy. Only 1 *Versicolor* specimen situated directly on the decision boundary was classified as *Virginica* due to overlapping petal length (> 4.8 cm).

### 3. Mathematical Formula Formulations

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

$$\text{Softmax Probability: } P(y = k \mid \mathbf{x}) = \frac{e^{\mathbf{w}_k^\top \mathbf{x} + b_k}}{\sum_{j=1}^3 e^{\mathbf{w}_j^\top \mathbf{x} + b_j}}$$

---

## 🌟 Interactive Key Features

1. **Authentic Botanical Flower Species Showcase**:
   - Curated high-resolution photography for all three species (*Setosa*, *Versicolor*, *Virginica*) plus full morphological anatomy comparison.
   - 1-click preset loader to test standard morphological dimensions.

2. **Morphometric Sensor Sliders**:
   - 4 calibrated sliders with live number input synchronisation, range meters, and instant edge calculation.
   - Quick presets: *Typical Setosa*, *Typical Versicolor*, *Typical Virginica*, *Borderline Margin*, and *Random Real Sample*.

3. **Dynamic 2D Feature Scatter Plot with Live Target Cursor**:
   - Plots all 150 Iris specimens across switchable coordinate projections (Sepal L vs W, Petal L vs W, Petal L vs Sepal L).
   - Real-time animated pulsing crosshair target (`🎯`) that moves across species clusters as sliders are adjusted!

4. **Interactive 3×3 Confusion Matrix & Metric Inspector**:
   - Cell-by-cell interactive hover inspection explaining True Positives, False Positives, and False Negatives.
   - Live numeric substitution into Precision, Recall, and F1-score formulas.

5. **Lecturer Oral Defense & Academic Theory Suite**:
   - In-depth answers covering linear separability of Setosa, Sepal vs Petal anatomical distinction, Softmax derivation, and L-BFGS optimization.

---

## 🛠️ Technology Stack & Architecture

- **Machine Learning Core:** Python 3.13, Scikit-Learn 1.9.1, NumPy, Joblib, Matplotlib
- **Web Frontend:** HTML5, CSS3 Glassmorphism, Vanilla JavaScript (ES6+), Canvas API, Canvas Confetti
- **Serverless API:** Python `BaseHTTPRequestHandler` deployed on Vercel Serverless Functions (`/api/predict`)
- **Cloud Hosting:** Vercel Global Edge Network with CI/CD GitHub synchronization
- **Version Control:** Git & GitHub

---

## 🚀 Running the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Philipntwi-bot/Iris_Classification_Project.git
cd Iris_Classification_Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
You can open `index.html` directly in any web browser, or start a local Python server:
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000`.

---

## 📜 Verification & Academic Attribution

- **Author:** Philip Antwi
- **Student ID:** PUIT24120002
- **Level:** 400 BSc Information Technology
- **Institution:** Pentecost University, Sowutuom, Accra, Ghana
- **Course:** Artificial Intelligence & Machine Learning
