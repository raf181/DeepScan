import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from log_preprocess import fetch_logs

# Load model
autoencoder = tf.keras.models.load_model('../models/autoencoder_model.h5')
scaler = StandardScaler()

def detect_anomalies():
    log_data = fetch_logs()
    features = log_data.select_dtypes(include=[np.number])
    scaled_data = scaler.fit_transform(features)

    # Predict and calculate reconstruction error
    reconstructions = autoencoder.predict(scaled_data)
    reconstruction_errors = np.mean(np.square(scaled_data - reconstructions), axis=1)
    threshold = np.mean(reconstruction_errors) + np.std(reconstruction_errors)
    
    anomalies = log_data[reconstruction_errors > threshold]
    if not anomalies.empty:
        anomalies.to_csv('../logs/detected_anomalies.log', mode='a', header=False)
        print("Anomalies detected and logged.")

if __name__ == "__main__":
    detect_anomalies()
