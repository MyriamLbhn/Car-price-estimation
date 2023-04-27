import streamlit as st
import joblib
import pandas as pd

# Chargement du modèle pré-entraîné
model = joblib.load('../models/trained_pipe_ridge_poly.joblib')

# Création d'une fonction pour afficher le formulaire et faire des prédictions
def predict_price(wheelbase, carlength, carwidth, curbweight, enginesize, boreratio, horsepower, fueleconomy,
                  symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, enginetype, cylindernumber,
                  fuelsystem, car_company):

    # Convertir les entrées utilisateur en un dataframe pandas
    input_df = pd.DataFrame({'wheelbase': [wheelbase],
                             'carlength': [carlength],
                             'carwidth': [carwidth],
                             'curbweight': [curbweight],
                             'enginesize': [enginesize],
                             'boreratio': [boreratio],
                             'horsepower': [horsepower],
                             'fueleconomy': [fueleconomy],
                             'symboling': [symboling],
                             'fueltype': [fueltype],
                             'aspiration': [aspiration],
                             'doornumber': [doornumber],
                             'carbody': [carbody],
                             'drivewheel': [drivewheel],
                             'enginelocation': [enginelocation],
                             'enginetype': [enginetype],
                             'cylindernumber': [cylindernumber],
                             'fuelsystem': [fuelsystem],
                             'car_company': [car_company]})

    # Faire la prédiction avec le modèle pré-entraîné
    prediction = model.predict(input_df)

    # Afficher la prédiction à l'utilisateur
    return prediction[0]

st.set_page_config(page_title="Car price prediction", page_icon=":car:", layout="wide")
st.title("Car price prediction")
col1, col2, col3 = st.columns(3)


# Définir les valeurs par défaut
default_values = {
    "wheelbase": 102.4,
    "carlength": 175.6,
    "carwidth": 66.5,
    "curbweight": 2414,
    "enginesize": 122,
    "boreratio": 3.33,
    "horsepower": 97,
    "fueleconomy": 29,
    "symboling": "-1",
    "fueltype": "gas",
    "aspiration": "std",
    "doornumber": "four",
    "carbody": "sedan",
    "drivewheel": "fwd",
    "enginelocation": "front",
    "enginetype": "ohc",
    "cylindernumber": "four",
    "fuelsystem": "mpfi",
    "car_company": "toyota"
}

with col1:
    wheelbase = st.number_input("Wheelbase", min_value=50.0, max_value=200.0, step=0.1, value=default_values["wheelbase"])
    carlength = st.number_input("Car lenght", min_value=100.0, max_value=300.0, step=0.1, value=default_values["carlength"])
    carwidth = st.number_input("Car width", min_value=30.0, max_value=100.0, step=0.1, value=default_values["carwidth"])
    curbweight = st.number_input("Curb weight", min_value=1000, max_value=6000, step=1, value=default_values["curbweight"])
    enginesize = st.number_input("Engine size", min_value=20, max_value=800, step=1, value=default_values["enginesize"])
    boreratio = st.number_input("Bore ratio", min_value=0.0, max_value=10.0, step=0.01, value=default_values["boreratio"])
    horsepower = st.number_input("Horsepower", min_value=20, max_value=500, step=1, value=default_values["horsepower"])
    fueleconomy = st.number_input("Fuel economy", min_value=0, max_value=100, step=1, value=default_values["fueleconomy"])


with col2:
    symboling = st.selectbox("Symboling", options=["-3", "-2", "-1", "0", "1", "2", "3"], index=int(default_values["symboling"]) + 3)
    fueltype = st.selectbox("Fuel type", options=["gas", "diesel"], index=1 if default_values["fueltype"] == "diesel" else 0)
    aspiration = st.selectbox("Aspiration", options=["std", "turbo"], index=1 if default_values["aspiration"] == "turbo" else 0)
    doornumber = st.selectbox("Number of doors", options=["two", "four"], index=1 if default_values["doornumber"] == "four" else 0)
    carbody = st.selectbox("Car body", options=["sedan", "hatchback", "wagon", "hardtop", "convertible"], index=["sedan", "hatchback", "wagon", "hardtop", "convertible"].index(default_values["carbody"]))
    drivewheel = st.selectbox("Drivewheel", options=["fwd", "rwd", "4wd"])
    enginelocation = st.selectbox("Engine location", options=["front", "rear"])
    enginetype = st.selectbox("Engine type", options=["ohc", "ohcf", "ohcv", "dohc", "l", "rotor", "dohcv"])
    cylindernumber = st.selectbox("Number of cylinders", options=["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"], index=2 if default_values["cylindernumber"]=="four" else 0)
    fuelsystem = st.selectbox("Fuel system", options=["mpfi", "2bbl", "idi", "1bbl", "spdi", "4bbl", "mfi", "spfi"], index=0 if default_values["fuelsystem"]=="mpfi" else 0)
    car_company = st.selectbox("Car brand", options=["toyota", "nissan", "mazda", "mitsubishi", "honda", "volkswagen", "subaru", "peugeot", "volvo", "dodge", "buick", "bmw", "audi", "plymouth", "saab", "porsche", "isuzu", "jaguar", "chevrolet", "alpha-romeo", "renault", "mercury"], 
                               index=0 if default_values["car_company"]=="toyota" else 0)

with col3:
    st.image("DALL·E 2023-04-26 16.25.42.png")
        # Fonction pour afficher la prédiction lorsque l'utilisateur clique sur le bouton
    if st.button("Predict the car price", key='predict'):
        result = predict_price(wheelbase, carlength, carwidth, curbweight, enginesize, boreratio, horsepower, fueleconomy,
                    symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, enginetype, cylindernumber,
                    fuelsystem, car_company)
        result= round(result)
        st.write("<h1>The car price is estimated at :</h1>", f"<h1 style='color: green; font-weight: bold; font-size: 48px;'>${result}</h1>", unsafe_allow_html=True)

