# Car Price Prediction

This project is a car price prediction tool built with Python and Streamlit. The model leverages machine learning techniques to predict the price of a car based on various input features like model year, mileage, engine type, and more.

![Project Owner](https://github.com/user-attachments/assets/5703ab83-1686-45f8-a91b-a282a83e9ab8)

## Project Owner

This project is a car price prediction tool built with Python and Streamlit. The model leverages machine learning techniques to predict the price of a car based on various input features like model year, mileage, engine type, and more.

## Link to Streamlit App

[Open in Streamlit](https://pricekh2024-zvfsxgwga9unazxe8f4qyg.streamlit.app/)

## Features

- Predicts car prices based on user-provided details
- Interactive UI built with Streamlit for easy usability
- Data preprocessing, transformation, and model loading handled in the backend

## Project Structure

```
project-folder/
│
├── main.py                  # Main Streamlit application
├── car_price_model.joblib   # Trained machine learning model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
```

### Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run the Streamlit app:

```bash
streamlit run main.py
```

Open the app in your browser by going to [http://localhost:8501](http://localhost:8501/).

## Usage

1. Enter details like car model, year, mileage, transmission type, and other relevant information.
2. Click the "Predict Price" button to get an estimated price.

## Model Training

The model was trained using various features, including:

- Model year
- Mileage
- Transmission type
- Fuel type
- Engine capacity and more...

The model was saved using joblib and can be reloaded for predictions.

## Dependencies

This project uses the following libraries:

- **Streamlit** - For building the interactive web application
- **Scikit-learn** - For machine learning model training and pipeline management
- **XGBoost** - For the prediction model
- **Pandas** - For data manipulation and preprocessing

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Notes

- Replace **username** in `git clone` with your GitHub username.

- If you don't have the `requirements.txt` file, you can create it by running the following command:

  ```bash
  pip freeze > requirements.txt
  ```

## Code Explanation

### Importing Libraries

```python
import streamlit as st
import pandas as pd
import joblib
```

- **`streamlit`**: For creating an interactive UI.
- **`pandas`**: For data manipulation.
- **`joblib`**: For loading the saved model.

### Setting up Streamlit UI

```python
st.markdown("""
    <h1 style='text-align: right;'>مدل پیش‌بینی قیمت خودرو</h1>
    """, unsafe_allow_html=True)
```

- Displays the app title in Persian.

```python
st.markdown("""
    <style>
    .css-1dq8tca {
        text-align: right;
        direction: rtl;
    }
    .stSelectbox, .stNumberInput, .stButton > button {
        text-align: right;
        direction: rtl;
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)
```

- Sets up right-aligned UI elements for better Persian language support.

### Loading Model and Data

```python
train_data = pd.read_csv('train.csv')
model = joblib.load('car_price_model.joblib.gz')
preprocessor = joblib.load("car_price_model_preprocessor.joblib")
```

- **`train_data`**: Loads the dataset used for training.
- **`model`**: Loads the pre-trained model.
- **`preprocessor`**: Loads the preprocessor used to transform input data.

### Encoding Categorical Features

```python
column_dictionaries = {}
for col in train_data.select_dtypes(include='object').columns:
    unique_values = train_data[col].unique()
    value_to_number = {value: idx for idx, value in enumerate(unique_values)}
    column_dictionaries[col] = value_to_number
```

- Creates mappings for categorical values to convert text into numerical values.

### Getting User Input

```python
title = st.selectbox("نام خودرو", list(column_dictionaries['title'].keys()))
year = st.number_input("سال ساخت", min_value=1350, max_value=1403, value=1390)
mileage = st.number_input("کارکرد (به کیلومتر)", min_value=0.0, value=110000.0, step=1000.0)
```

- Collects user input for the car details, including title, year, and mileage.

### Preparing Input Data

```python
input_data = pd.DataFrame({
    "title": [column_dictionaries['title'][title]],
    "year": [year],
    "mileage": [mileage],
    "transmission": [column_dictionaries['transmission'][transmission]],
    "fuel": [column_dictionaries['fuel'][fuel]],
    "body_color": [column_dictionaries['body_color'][body_color]],
    "inside_color": [column_dictionaries['inside_color'][inside_color]],
    "body_status": [column_dictionaries['body_status'][body_status]],
    "body_type": [column_dictionaries['body_type'][body_type]],
    "volume": [volume],
    "engine": [column_dictionaries['engine'][engine]],
    "acceleration": [acceleration]
})
```

- Converts user inputs into a structured DataFrame, replacing categorical values with numerical representations.

### Making Predictions

```python
if st.button("پیش‌بینی قیمت"):
    predicted_price = model.predict(input_data)
    st.markdown(f"""
        <div style='text-align: right;'>
            <span style='font-weight: bold; font-size: 18px;'>قیمت پیش‌بینی شده: </span>
            <span style='color: purple; font-size: 24px; font-weight: bold;'>{predicted_price[0]:,.0f}</span>
            <span style='font-weight: bold; font-size: 18px;'>تومان</span>  
        </div>
    """, unsafe_allow_html=True)
```

- When the "Predict Price" button is clicked, the model predicts the price and displays it in Persian format.

------

## Project link on my kaggle page

[Project link]([https://pricekh2024-zvfsxgwga9unazxe8f4qyg.streamlit.app/](https://www.kaggle.com/code/peimandaii/predict-price-iranian-car))




