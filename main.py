import streamlit as st
import pandas as pd
import joblib

st.markdown("""
    <h1 style='text-align: right;'>مدل پیش‌بینی قیمت خودرو</h1>
    """, unsafe_allow_html=True)

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

train_data = pd.read_csv('train.csv')
model = joblib.load('car_price_model.joblib.gz')
preprocessor = joblib.load("car_price_model_preprocessor.joblib")

column_dictionaries = {}
for col in train_data.select_dtypes(include='object').columns:
    unique_values = train_data[col].unique()

    value_to_number = {value: idx for idx, value in enumerate(unique_values)}
    column_dictionaries[col] = value_to_number

title = st.selectbox("نام خودرو", list(column_dictionaries['title'].keys()))
year = st.number_input("سال ساخت", min_value=1350, max_value=1403, value=1390)
mileage = st.number_input("کارکرد (به کیلومتر)", min_value=0.0, value=110000.0, step=1000.0)
transmission = st.selectbox("نوع گیربکس", list(column_dictionaries['transmission'].keys()))
fuel = st.selectbox("نوع سوخت", list(column_dictionaries['fuel'].keys()))
body_color = st.selectbox("رنگ بدنه", list(column_dictionaries['body_color'].keys()))
inside_color = st.selectbox("رنگ داخل", list(column_dictionaries['inside_color'].keys()))
body_status = st.selectbox("وضعیت بدنه", list(column_dictionaries['body_status'].keys()))
body_type = st.selectbox("نوع بدنه", list(column_dictionaries['body_type'].keys()))
volume = st.number_input("حجم موتور (به سی‌سی)", min_value=0.0, value=1.3)
engine = st.selectbox("نوع موتور", list(column_dictionaries['engine'].keys()))
acceleration = st.number_input("شتاب (0 تا 100)", min_value=0.0, value=13.0, step=0.1)


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

if st.button("پیش‌بینی قیمت"):
    predicted_price = model.predict(input_data)
    st.markdown(f"""
        <div style='text-align: right;'>
            <span style='font-weight: bold; font-size: 18px;'>قیمت پیش‌بینی شده: </span>
            <span style='color: purple; font-size: 24px; font-weight: bold;'>{predicted_price[0]:,.0f}</span>
            <span style='font-weight: bold; font-size: 18px;'>تومان</span>  
        </div>
    """, unsafe_allow_html=True)

