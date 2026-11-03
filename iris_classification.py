# Import the Iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import joblib
# Load the dataset
iris = load_iris()

# Separate input features and target
X = iris.data
y = iris.target

# Display the dataset information
print("First five flower measurements:")
print(X[:5])

print("\nFirst five flower categories:")
print(y[:5])

print("\nDataset size:")
print(X.shape)

print("\nFlower measurements:")
print(iris.feature_names)

print("\nFlower species:")
print(iris.target_names)

# Split the dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Display the training and testing sizes

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
# Create the Logistic Regression model
model = LogisticRegression(max_iter=200)

# Train the model using the training data
model.fit(X_train, y_train)

print("Model training completed successfully!")
# Save the trained model
joblib.dump(model, "iris_model.pkl")

print("Trained model saved successfully!")
# Make predictions using the testing data
y_pred = model.predict(X_test)

# Display the predicted flower categories
print("\nPredicted flower categories:")
print(y_pred)
# Compare predictions with actual categories
accuracy = accuracy_score(y_test, y_pred)

# Display the model accuracy
print("\nModel Accuracy:")
print(accuracy * 100, "%")
# Generate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display the confusion matrix
print("\nConfusion Matrix:")
print(cm)
# Display the confusion matrix visually
plt.figure(figsize=(6, 5))

plt.imshow(cm, cmap="Blues")

plt.title("Iris Classification Confusion Matrix")
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")

plt.xticks([0, 1, 2], iris.target_names)
plt.yticks([0, 1, 2], iris.target_names)

# Display numbers inside the boxes
for i in range(3):
    for j in range(3):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.colorbar()
plt.tight_layout()
# Save the confusion matrix as an image
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")

# Display the confusion matrix
plt.show()
# Generate classification report
report = classification_report(y_test, y_pred, target_names=iris.target_names)

# Display the classification report
print("\nClassification Report:")
print(report)
# Compare actual and predicted flower categories

print("\nActual vs Predicted Results:")
print("--------------------------------")

for actual, predicted in zip(y_test, y_pred):
    print(
        "Actual:", iris.target_names[actual],
        "| Predicted:", iris.target_names[predicted]
    )