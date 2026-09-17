import streamlit as st
import pandas as pd
import joblib

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CUSTOM CSS

st.markdown("""
<style>

    /* Main page */
    .stApp {
        background-color: #f7f8fc;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #202124;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 650;
        color: #252a34;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Cards */
    .input-card {
        background-color: white;
        padding: 24px 26px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }

    /* Prediction card */
    .prediction-card {
        background-color: white;
        border-radius: 16px;
        padding: 30px;
        margin-top: 30px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
        text-align: center;
    }

    .prediction-label {
        font-size: 16px;
        color: #6b7280;
        margin-bottom: 5px;
    }

    .prediction-value {
        font-size: 42px;
        font-weight: 750;
        color: #4f46e5;
    }

    .prediction-note {
        font-size: 14px;
        color: #9ca3af;
        margin-top: 5px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        border: none;
        background-color: #4f46e5;
        color: white;
        font-size: 17px;
        font-weight: 600;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #4338ca;
        border: none;
        color: white;
    }

    /* Input labels */
    label {
        font-weight: 500 !important;
        color: #374151 !important;
    }

    /* Dataframe */
    .details-title {
        font-size: 22px;
        font-weight: 650;
        color: #252a34;
        margin-top: 35px;
        margin-bottom: 15px;
    }

    /* Divider */
    .divider {
        height: 1px;
        background-color: #e5e7eb;
        margin: 30px 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        margin-top: 45px;
    }

</style>
""", unsafe_allow_html=True)


# LOAD MODEL

model = joblib.load("car_price_model.pkl")
feature_names = joblib.load("feature_names.pkl")
city_list = joblib.load("city_list.pkl")


# HEADER

st.markdown(
    '<div class="main-title">Car Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Estimate the resale value of a used car using machine learning.'
    '</div>',
    unsafe_allow_html=True
)


# BASIC DETAILS

st.markdown(
    '<div class="section-title">Basic Vehicle Details</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    full_name = st.text_input(
        "Car Name",
        "Maruti Swift"
    )

with col2:
    registered_year = st.slider(
        "Registered Year",
        2002,
        2023,
        2018
    )

with col3:
    city = st.selectbox(
        "City",
        city_list
    )

st.markdown('</div>', unsafe_allow_html=True)


# PERFORMANCE DETAILS

st.markdown(
    '<div class="section-title">Performance & Usage</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    engine_capacity = st.number_input(
        "Engine Capacity (CC)",
        min_value=500,
        max_value=6000,
        value=1200,
        step=100
    )

with col2:
    max_power = st.number_input(
        "Max Power (bhp)",
        min_value=20.0,
        max_value=600.0,
        value=90.0,
        step=5.0
    )

with col3:
    mileage = st.number_input(
        "Mileage (kmpl)",
        min_value=5.0,
        max_value=40.0,
        value=18.0,
        step=0.5
    )

col1, col2, col3 = st.columns(3)

with col1:
    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        max_value=500000,
        value=50000,
        step=1000
    )

with col2:
    seats = st.selectbox(
        "Seats",
        [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        index=2
    )

with col3:
    owner_type = st.selectbox(
        "Owner Type",
        [
            "First Owner",
            "Second Owner",
            "Third Owner",
            "Fourth Owner"
        ]
    )

st.markdown('</div>', unsafe_allow_html=True)


# VEHICLE INFORMATION

st.markdown(
    '<div class="section-title">Vehicle Information</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    fuel_type = st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG",
            "Electric"
        ]
    )

with col2:
    transmission_type = st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )

with col3:
    body_type = st.selectbox(
        "Body Type",
        [
            "Hatchback",
            "Sedan",
            "SUV",
            "MUV",
            "Coupe",
            "Convertible",
            "Minivan",
            "Pickup Truck"
        ]
    )

col1, col2, col3 = st.columns(3)

with col1:
    insurance = st.selectbox(
        "Insurance",
        [
            "Yes",
            "No"
        ]
    )

st.markdown('</div>', unsafe_allow_html=True)


# PREDICTION BUTTON


st.markdown("<br>", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:

    predict_button = st.button(
        "Predict Car Price"
    )



# CREATE INPUT DATA

input_df = pd.DataFrame({

    "registered_year": [registered_year],
    "engine_capacity": [engine_capacity],
    "kms_driven": [kms_driven],
    "max_power": [max_power],
    "seats": [seats],
    "mileage": [mileage],
    "insurance": [insurance],
    "owner_type": [owner_type],
    "transmission_type": [transmission_type],
    "fuel_type": [fuel_type],
    "body_type": [body_type],
    "city": [city],
    "full_name": [full_name]

})


# PREPROCESSING

input_df = pd.get_dummies(
    input_df,
    drop_first=True
)

input_df = input_df.reindex(
    columns=feature_names,
    fill_value=0
)


# PREDICTION

if predict_button:

    prediction = model.predict(input_df)

    predicted_price = prediction[0]

    # Prediction Card
    st.html(
        f"""
        <div class="prediction-card">
            <div class="prediction-label">Estimated Resale Price</div>
            <div class="prediction-value">₹ {predicted_price:.2f} Lakhs</div>
            <div class="prediction-note">
                Estimated value based on the vehicle information provided
            </div>
        </div>
        """
    )


    # CAR DETAILS


    st.markdown(
        '<div class="details-title">Vehicle Summary</div>',
        unsafe_allow_html=True
    )

    details = pd.DataFrame({

        "Feature": [
            "Car Name",
            "Registered Year",
            "Engine Capacity",
            "Kilometers Driven",
            "Max Power",
            "Seats",
            "Mileage",
            "Insurance",
            "Owner Type",
            "Transmission",
            "Fuel Type",
            "Body Type",
            "City"
        ],

        "Value": [
            full_name,
            registered_year,
            f"{engine_capacity} CC",
            f"{kms_driven:,} km",
            f"{max_power} bhp",
            seats,
            f"{mileage} kmpl",
            insurance,
            owner_type,
            transmission_type,
            fuel_type,
            body_type,
            city
        ]

    })

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True
    )


# FOOTER

st.markdown(
    """
    <div class="footer">
        Car Price Prediction System · Machine Learning Application
    </div>
    """,
    unsafe_allow_html=True
)
