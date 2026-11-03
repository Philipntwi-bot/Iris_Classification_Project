import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Iris AI Classification",
    page_icon="🌸",
    layout="wide"
)

# --------------------------------
# 2. LOAD MACHINE LEARNING MODEL
# --------------------------------

model = joblib.load("iris_model.pkl")

iris = load_iris()
flower_names = iris.target_names

# --------------------------------
# 3. CUSTOM DASHBOARD DESIGN
# --------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F4F7FB;
}

.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #17365D;
}

.subtitle {
    font-size: 17px;
    color: #64748B;
}

.info-card {
    background-color: white;
    padding: 22px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.info-card h3 {
    color: #17365D;
}

.info-card p {
    color: #64748B;
}

.result-card {
    background-color: #E0F2FE;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #BAE6FD;
}

.result-card h2 {
    color: #075985;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# 4. DASHBOARD HEADER
# --------------------------------

st.markdown(
    '<div class="main-title">🌸 Iris Flower AI Classification</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A Machine Learning System for Predicting Iris Flower Species</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------
# 5. INFORMATION CARDS
# --------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🌱 Setosa</h3>
        <p>Iris flower species</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🌼 Versicolor</h3>
        <p>Iris flower species</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🌺 Virginica</h3>
        <p>Iris flower species</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# --------------------------------
# 6. INPUT SECTION
# --------------------------------

st.subheader("🔍 Enter Flower Measurements")

st.write(
    "Provide the measurements below to allow the machine learning "
    "model to identify the flower species."
)

input_col1, input_col2 = st.columns(2)

with input_col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with input_col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

st.write("")

# --------------------------------
# 7. PREDICTION
# --------------------------------

if st.button("🔮 Predict Flower Species", use_container_width=True):

    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(input_data)

    probabilities = model.predict_proba(input_data)[0]

    predicted_species = flower_names[prediction[0]]

    confidence = probabilities[prediction[0]] * 100

    st.divider()

    # Prediction result

    st.subheader("📊 Classification Result")

    st.markdown(f"""
    <div class="result-card">
        <h2>Predicted Species</h2>
        <h1>{predicted_species.upper()}</h1>
        <p>Prediction Confidence: {confidence:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Probability chart

    st.subheader("Prediction Probability")

    probability_data = pd.DataFrame({
        "Flower Species": flower_names,
        "Probability (%)": probabilities * 100
    })

    st.bar_chart(
        probability_data.set_index("Flower Species")
    )

    st.success("Flower classification completed successfully!")

# --------------------------------
# 8. ABOUT THE SYSTEM
# --------------------------------

st.divider()

with st.expander("ℹ️ About This Machine Learning System"):

    st.write("""
    This application uses Logistic Regression, a supervised
    machine learning classification algorithm.

    The model was trained using the Iris dataset from
    Scikit-learn.

    It uses four measurements:

    - Sepal Length
    - Sepal Width
    - Petal Length
    - Petal Width

    The system predicts one of three flower species:

    - Setosa
    - Versicolor
    - Virginica
    """)

st.caption("Iris Flower Classification Project | Machine Learning")