import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    # Load synthetic dataset
    df = pd.read_csv('dummy_telemetry.csv')

    X = df[['cpu_load', 'ram_usage']]
    y = df[['power_draw', 'temperature']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save trained model
    joblib.dump(model, 'greencloud_model.pkl')
    print("✅ Machine Learning model trained and saved as greencloud_model.pkl")

def predict_metrics(cpu_load, ram_usage):
    try:
        model = joblib.load('greencloud_model.pkl')
    except FileNotFoundError:
        train_model()
        model = joblib.load('greencloud_model.pkl')

    prediction = model.predict([[cpu_load, ram_usage]])
    predicted_power, predicted_temp = prediction[0]

    return {
        'predicted_power_watts': round(predicted_power, 2),
        'predicted_temp_c': round(predicted_temp, 2)
    }

if __name__ == '__main__':
    train_model()