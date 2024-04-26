import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Charger les données
def load_data():
    data = pd.read_csv('Base_OP_2023_Nationale.csv')
    features = data[['surface_moyenne', 'nombre_pieces_homogene', 'agglomeration']].values
    target = data['loyer_moyen'].values
    return features, target

# Préparation des données
def prepare_data(features, target):
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    return train_test_split(features_scaled, target, test_size=0.2, random_state=0)

# Construction du modèle
def build_model(input_dim):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=input_dim))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='linear'))
    return model

# Compilation et entraînement du modèle
def compile_and_train(model, X_train, y_train):
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)

# Exécution principale
def main():
    features, target = load_data()
    X_train, X_test, y_train, y_test = prepare_data(features, target)
    model = build_model(X_train.shape[1])
    compile_and_train(model, X_train, y_train)
    # Évaluation simple (peut être étendue pour inclure des métriques plus complexes)
    test_loss = model.evaluate(X_test, y_test)
    print('Test loss:', test_loss)

if __name__ == "__main__":
    main()
