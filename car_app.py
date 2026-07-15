import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")
feature_names = joblib.load("feature_names.pkl")
city_list = joblib.load("city_list.pkl")

registered_year = st.sidebar.slider(
    "Registered Year",
    2002,
    2023,
    2018
)

engine_capacity = st.sidebar.number_input(
    "Engine Capacity (CC)",
    500,
    6000,
    1200
)

kms_driven = st.sidebar.number_input(
    "Kilometers Driven",
    0,
    500000,
    50000
)

max_power = st.sidebar.number_input(
    "Max Power (bhp)",
    20.0,
    600.0,
    90.0
)

seats = st.sidebar.selectbox(
    "Seats",
    [2,4,5,6,7,8,9,10,11,12,13,14]
)

mileage = st.sidebar.number_input(
    "Mileage",
    5.0,
    40.0,
    18.0
)

city = st.sidebar.selectbox(
    "City",
    city_list
)

insurance = st.sidebar.selectbox(
    "Insurance",
    ["Yes","No"]
)

owner_type = st.sidebar.selectbox(
    "Owner Type",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth Owner"
    ]
)

transmission_type = st.sidebar.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

fuel_type = st.sidebar.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "CNG",
        "LPG",
        "Electric"
    ]
)

body_type = st.sidebar.selectbox(
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

full_name = st.sidebar.text_input(
    "Car Name",
    "Maruti Swift"
)


input_df = pd.DataFrame({

    "registered_year":[registered_year],
    "engine_capacity":[engine_capacity],
    "kms_driven":[kms_driven],
    "max_power":[max_power],
    "seats":[seats],
    "mileage":[mileage],
    "insurance":[insurance],
    "owner_type":[owner_type],
    "transmission_type":[transmission_type],
    "fuel_type":[fuel_type],
    "body_type":[body_type],
    "city":[city],
    "full_name":[full_name]

})


input_df = pd.get_dummies(
    input_df,
    drop_first=True
)


input_df = input_df.reindex(
    columns=feature_names,
    fill_value=0
)


if st.button("Predict Price"):

    prediction = model.predict(input_df)

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="Estimated Resale Price",
        value=f"{prediction[0]:.2f} Lakhs"
    )


    st.write("### Car Details")

    details = pd.DataFrame({
        "Feature": [
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
            "City",
            "Car Name"
        ],
        "Value": [
            registered_year,
            f"{engine_capacity} CC",
            f"{kms_driven:,} Kms",
            f"{max_power} bhp",
            seats,
            f"{mileage} kmpl",
            insurance,
            owner_type,
            transmission_type,
            fuel_type,
            body_type,
            city,
            full_name
        ]
    })

    st.table(details)
