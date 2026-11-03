 Iris Flower Classification Using Machine Learning

1. Project Overview

This project focuses on developing a Machine Learning classification system that predicts the species of an Iris flower based on four physical measurements.

The system uses Logistic Regression, a supervised machine learning algorithm, to classify flowers into three species: Setosa, Versicolor, and Virginica.

A Streamlit web application was also developed to allow users to enter flower measurements and obtain predictions.

2. Project Objectives

* To develop a machine learning model for classifying Iris flower species.
* To train and evaluate the model using the Iris dataset.
* To develop an interactive web application for making predictions.
* To demonstrate how machine learning can solve classification problems.

3. Dataset Description

The project uses the Iris dataset provided by Scikit-learn.

The dataset contains 150 flower observations divided into three species.

The four input features are:

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

The target classes are:

* Setosa
* Versicolor
* Virginica

4. Machine Learning Algorithm

The project uses Logistic Regression, a supervised classification algorithm.

The model learns patterns from the training data and uses those patterns to predict the species of previously unseen flower measurements.

 5. Model Performance

The model achieved an accuracy of approximately 96.67% on the test dataset.

A confusion matrix and classification report were also generated to evaluate its performance.

6. Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Streamlit
* GitHub

7. Project Files

| File                     | Description                    |
| ------------------------ | ------------------------------ |
| `iris_classification.py` | Model training and evaluation  |
| `app.py`                 | Streamlit web application      |
| `iris_model.pkl`         | Saved trained model            |
| `confusion_matrix.png`   | Confusion matrix visualisation |
| `README.md`              | Project documentation          |

 8. How to Run the Project

Step 1: Clone the repository

```bash
git https://github.com/Philipntwi-bot/Iris_Classification_Project
```

 Step 2: Open the project folder

```bash
cd Iris_Classification_Project
```
Step 3: Install the required libraries

```bash
pip install streamlit pandas numpy scikit-learn matplotlib joblib
```

Step 4: Run the application

```bash
python -m streamlit run app.py
```

9. Conclusion

The project demonstrates the application of supervised machine learning in solving a multiclass classification problem. The developed web application provides an interactive way for users to predict Iris flower species using their physical measurements.
