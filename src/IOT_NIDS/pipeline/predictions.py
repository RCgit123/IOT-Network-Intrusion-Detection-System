import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

def predict_labels(model, x_test):
    # Make predictions using the model
    model=load_model(os.path.join("artifacts","gru_model","gru_model.h5"))
    min_max_scaler = MinMaxScaler()
    x_test = min_max_scaler.fit_transform(x_test)
    predictions = model.predict(x_test)

    # Get the index of the maximum probability for each prediction
    predicted_labels_index = np.argmax(predictions, axis=1)

    # Define your label mapping
    labels=['Normal', 'MITM', 'Uploading', 'Ransomware', 'SQL_injection',
            'DDoS_HTTP', 'DDoS_TCP', 'Password', 'Port_Scanning',
            'Vulnerability_scanner', 'Backdoor', 'XSS', 'Fingerprinting',
            'DDoS_UDP', 'DDoS_ICMP']

    # Map the predicted indices to actual labels
    predicted_labels = [labels[i] for i in predicted_labels_index]

    return predicted_labels

