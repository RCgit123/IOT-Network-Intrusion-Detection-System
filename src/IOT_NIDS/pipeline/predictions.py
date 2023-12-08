import numpy as np
from pathlib import Path 
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import ipaddress


class Pred:
        def __init__(self):
              self.model=load_model(Path('model/gru_model.h5'))
        import ipaddress

        def convert_to_int(ip_str):
            try:
                return int(ipaddress.IPv4Address(self, ip_str))
            except ipaddress.AddressValueError:
                return None  # or handle the error in a way that makes sense for your case
        
        def predictionPipeline(self, data):
            # Make predictions using the model
            min_max_scaler = MinMaxScaler()
            test=pd.read_csv(data)
            #transforming the columns
            test['ip.src_host'] = test['ip.src_host'].apply(self.convert_to_int)
            test['tcp.srcport'] = test['tcp.srcport'].astype(np.float64)
            test = min_max_scaler.fit_transform(test.head(100))
            predictions = self.model.predict(test)

            # Get the index of the maximum probability for each prediction
            predicted_labels_index = np.argmax(predictions, axis=1)

            # Define your label mapping
            labels=['Normal', 'MITM', 'Uploading', 'Ransomware', 'SQL_injection',
                    'DDoS_HTTP', 'DDoS_TCP', 'Password', 'Port_Scanning',
                    'Vulnerability_scanner', 'Backdoor', 'XSS', 'Fingerprinting',
                    'DDoS_UDP', 'DDoS_ICMP']

            # Map the predicted indices to actual labels
            predicted_labels = [labels[i] for i in predicted_labels_index]
            predicted_labels=set(predicted_labels)
            
            return list(predicted_labels)

