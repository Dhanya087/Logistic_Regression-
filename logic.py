import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st

# Load the dataset
dataset = pd.read_csv('rain.csv')

# Convert 'Rain (Yes/No)' to binary
dataset['Rain (Yes/No)'] = dataset['Rain (Yes/No)'].map({'Yes': 1, 'No': 0})

# Split dataset into features and target
X = dataset.drop(columns=['Rain (Yes/No)'])
y = dataset['Rain (Yes/No)']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title('Rain Prediction')

st.write('Enter weather conditions to predict whether it will rain or not.')

# Create text input fields for temperature, pressure, and humidity
temperature = st.text_input('Temperature (Celsius)')
pressure = st.text_input('Pressure')
humidity = st.text_input('Humidity (%)')

# Create a predict button
if st.button('Predict'):
    # Check if inputs are provided
    if temperature and pressure and humidity:
        # Convert inputs to float
        temperature = float(temperature)
        pressure = float(pressure)
        humidity = float(humidity)

        # Make prediction
        prediction = model.predict([[pressure, temperature, humidity]])

        # Display prediction result
        st.write('Prediction:')
        if prediction[0] == 1:
            st.write('It will rain.')
        else:
            st.write('It will not rain.')


