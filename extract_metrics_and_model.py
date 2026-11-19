import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import json
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save pkl
joblib.dump(model, "iris_model.pkl")

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred).tolist()
rep = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)

coef = model.coef_.tolist()
intercept = model.intercept_.tolist()

# Also calculate stats per species for the UI
species_stats = {}
for i, name in enumerate(iris.target_names):
    subset = X[y == i]
    species_stats[name] = {
        "sepal_length": {"mean": round(float(np.mean(subset[:, 0])), 2), "std": round(float(np.std(subset[:, 0])), 2), "min": round(float(np.min(subset[:, 0])), 2), "max": round(float(np.max(subset[:, 0])), 2)},
        "sepal_width": {"mean": round(float(np.mean(subset[:, 1])), 2), "std": round(float(np.std(subset[:, 1])), 2), "min": round(float(np.min(subset[:, 1])), 2), "max": round(float(np.max(subset[:, 1])), 2)},
        "petal_length": {"mean": round(float(np.mean(subset[:, 2])), 2), "std": round(float(np.std(subset[:, 2])), 2), "min": round(float(np.min(subset[:, 2])), 2), "max": round(float(np.max(subset[:, 2])), 2)},
        "petal_width": {"mean": round(float(np.mean(subset[:, 3])), 2), "std": round(float(np.std(subset[:, 3])), 2), "min": round(float(np.min(subset[:, 3])), 2), "max": round(float(np.max(subset[:, 3])), 2)}
    }

# All 150 points for scatter plot
samples = []
for i in range(len(y)):
    samples.append({
        "sl": float(round(X[i][0], 2)),
        "sw": float(round(X[i][1], 2)),
        "pl": float(round(X[i][2], 2)),
        "pw": float(round(X[i][3], 2)),
        "species": int(y[i]),
        "name": str(iris.target_names[y[i]])
    })

data_export = {
    "accuracy": round(acc * 100, 2),
    "confusion_matrix": cm,
    "classification_report": rep,
    "coef": coef,
    "intercept": intercept,
    "feature_names": iris.feature_names,
    "target_names": iris.target_names.tolist(),
    "species_stats": species_stats,
    "samples": samples
}

with open("model_data.json", "w") as f:
    json.dump(data_export, f, indent=2)

print("Saved model_data.json successfully!")
print("Accuracy:", acc)
print("CM:", cm)
