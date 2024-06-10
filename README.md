# Rain Prediction using Logistic Regression

This project predicts whether it will rain based on weather conditions such as temperature, pressure, and humidity. It utilizes Logistic Regression for binary classification and includes an interactive web application powered by Streamlit.

## Project Overview
The goal of this project is to predict whether it will rain based on weather attributes. The dataset includes features like temperature, pressure, and humidity. We use Logistic Regression to classify whether it will rain or not. The project includes:

- Data loading and preprocessing
- Training the Logistic Regression model
- Interactive Streamlit app for prediction

## Usage
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/rain-prediction.git
    cd rain-prediction
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App:**
    ```sh
    streamlit run app.py
    ```

4. **Use the Streamlit App:**
    - Input weather conditions (temperature, pressure, humidity).
    - Click on the "Predict" button.
    - View the prediction whether it will rain or not.

## File Structure
- `app.py`: Contains the Streamlit web application code.
- `rain.csv`: Dataset containing weather attributes.
- `README.md`: This file.

## Dependencies
- pandas
- scikit-learn
- streamlit
