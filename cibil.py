import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib


def train_model(data_file, model_file):
    # Read data
    df = pd.read_csv(data_file)

    # Encoding categorical variables
    le = LabelEncoder()
    df['Crop_type'] = le.fit_transform(df['Crop_type'])

    # Splitting data into input (X) and target (y)
    X = df.drop(columns=['CIBIL_score'])
    y = df['CIBIL_score']

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, model_file)

    print("Model trained and saved successfully!")


def generate_npk_value(n, p, k):
    # Assuming weights for N, P, and K respectively
    n_weight = 0.4
    p_weight = 0.3
    k_weight = 0.3

    # Calculate weighted sum for NPK value
    npk_value = (n * n_weight) + (p * p_weight) + (k * k_weight)
    return npk_value


def predict_with_trained_model(model_file, crop_value, other_features):
    # Load the trained model
    model = joblib.load(model_file)
    npk = generate_npk_value(other_features[0], other_features[1], other_features[2])
    other_features2 = [npk, other_features[3], other_features[4]]

    # Example input
    crop_encoding = {'Wheat': 0, 'Rice': 1, 'Maize': 2, 'Barley': 3}
    example_input = np.array([other_features2 + [crop_encoding[crop_value]]])

    # Predict using the loaded model
    predicted_cibil = model.predict(example_input)

    print(f'Predicted CIBIL Score: {predicted_cibil[0]}')


# Example usage
train_model('sample_data.csv', 'trained_model.pkl')
predict_with_trained_model('trained_model.pkl', 'Wheat', [55, 20, 30, 110, 5500])