import os
from detect_anomalies import detect_anomalies
from alerting import send_alert

def main():
    # Detect anomalies
    detect_anomalies()
    
    # Check if anomalies were detected and alert if necessary
    if os.path.exists("../logs/detected_anomalies.log"):
        with open("../logs/detected_anomalies.log", "r") as f:
            anomalies = f.read()
            if anomalies:
                send_alert(f"Anomalies detected:\n\n{anomalies}")

if __name__ == "__main__":
    main()
