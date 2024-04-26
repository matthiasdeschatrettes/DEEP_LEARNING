import streamlit as st
import pandas as pd
from data_processing import prepare_data
from keras.models import load_model
import numpy as np

# Charger et préparer les données
data = prepare_data('Base_OP_2023_Nationale.csv')
model = load_model('loyer_model.h5')  # Assurez-vous que le modèle est bien entraîné et sauvegardé.

# Création de l'interface utilisateur
st.title('Dashboard des Loyers en France avec Prédiction de Loyer')

# Visualisation des données
st.header('Histogramme des Loyers')
st.bar_chart(data['loyer'])

st.header('Prédiction de Loyer')
surface = st.number_input('Entrez la surface du bien (en m²):', min_value=0)

if st.button('Prédire le loyer'):
    predicted_loyer = model.predict(np.array([[surface]]))[0][0]
    st.write(f'Le loyer prédit est de {predicted_loyer:.2f} euros.')
