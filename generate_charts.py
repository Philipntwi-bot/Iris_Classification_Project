import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Set dark theme style
plt.style.use('dark_background')

# 1. Confusion Matrix Plot
fig, ax = plt.subplots(figsize=(7, 6), facecolor='#0b0f19')
ax.set_facecolor('#0f172a')

cax = ax.imshow(cm, interpolation='nearest', cmap='Blues')
cbar = fig.colorbar(cax, fraction=0.046, pad=0.04)
cbar.ax.tick_params(colors='#94a3b8')

ax.set_title("Iris Classification Confusion Matrix (30 Test Samples)\nPhilip Antwi | PUIT24120002", 
             fontsize=13, fontweight='bold', color='#38bdf8', pad=15)
ax.set_xlabel("Predicted Species", fontsize=11, fontweight='semibold', color='#f1f5f9', labelpad=10)
ax.set_ylabel("Actual Ground Truth Species", fontsize=11, fontweight='semibold', color='#f1f5f9', labelpad=10)

tick_marks = np.arange(len(iris.target_names))
species_labels = ['I. setosa', 'I. versicolor', 'I. virginica']
ax.set_xticks(tick_marks)
ax.set_xticklabels(species_labels, fontsize=10, color='#cbd5e1')
ax.set_yticks(tick_marks)
ax.set_yticklabels(species_labels, fontsize=10, color='#cbd5e1')

# Add values inside cells
for i in range(3):
    for j in range(3):
        val = cm[i, j]
        color = '#ffffff' if val > 5 else '#94a3b8'
        tag = ""
        if i == j:
            tag = " (TP)"
        elif val > 0:
            tag = " (Err)"
        ax.text(j, i, f"{val}{tag}", ha="center", va="center", 
                fontsize=13, fontweight='bold', color=color)

plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300, facecolor='#0b0f19', bbox_inches='tight')
plt.close()
print("confusion_matrix.png generated successfully!")

# 2. Feature Scatter / Clustering Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor='#0b0f19')

# Subplot 1: Sepal Length vs Sepal Width
ax1.set_facecolor('#0f172a')
colors = ['#06b6d4', '#a855f7', '#ec4899']
markers = ['o', 's', '^']

for i, (name, col, mark) in enumerate(zip(iris.target_names, colors, markers)):
    subset = X[y == i]
    ax1.scatter(subset[:, 0], subset[:, 1], c=col, marker=mark, s=65, alpha=0.85, 
                edgecolors='white', linewidths=0.5, label=f"Iris {name}")

ax1.set_title("Sepal Dimensions: Length vs Width", fontsize=12, fontweight='bold', color='#38bdf8')
ax1.set_xlabel("Sepal Length (cm)", color='#cbd5e1', fontsize=10)
ax1.set_ylabel("Sepal Width (cm)", color='#cbd5e1', fontsize=10)
ax1.tick_params(colors='#94a3b8')
ax1.grid(True, color='#334155', linestyle='--', alpha=0.4)
ax1.legend(loc='upper right', facecolor='#1e293b', edgecolor='#334155', labelcolor='#f1f5f9')

# Subplot 2: Petal Length vs Petal Width
ax2.set_facecolor('#0f172a')
for i, (name, col, mark) in enumerate(zip(iris.target_names, colors, markers)):
    subset = X[y == i]
    ax2.scatter(subset[:, 2], subset[:, 3], c=col, marker=mark, s=65, alpha=0.85, 
                edgecolors='white', linewidths=0.5, label=f"Iris {name}")

ax2.set_title("Petal Dimensions: Length vs Width (Linear Separation)", fontsize=12, fontweight='bold', color='#22c55e')
ax2.set_xlabel("Petal Length (cm)", color='#cbd5e1', fontsize=10)
ax2.set_ylabel("Petal Width (cm)", color='#cbd5e1', fontsize=10)
ax2.tick_params(colors='#94a3b8')
ax2.grid(True, color='#334155', linestyle='--', alpha=0.4)
ax2.legend(loc='upper left', facecolor='#1e293b', edgecolor='#334155', labelcolor='#f1f5f9')

fig.suptitle("Morphological Feature Space & Species Clustering\nPhilip Antwi // PUIT24120002 // Pentecost University", 
             fontsize=14, fontweight='bold', color='#f8fafc', y=1.02)

plt.tight_layout()
plt.savefig("feature_clustering.png", dpi=300, facecolor='#0b0f19', bbox_inches='tight')
plt.close()
print("feature_clustering.png generated successfully!")
