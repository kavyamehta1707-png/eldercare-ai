import numpy as np
import random

# ------------------------------------------------
# Synthetic Sensor Generator
# ------------------------------------------------

def generate_sensor_data():

    posture = random.choice(["standing", "walking", "sitting", "lying"])

    data = {
        "posture": posture,
        "heart_rate": np.random.normal(75, 8),
        "movement_level": np.random.uniform(0, 1),
        "time_in_posture": np.random.randint(1, 120)  # minutes
    }

    return data


# ------------------------------------------------
# Explainable AI Risk Engine
# ------------------------------------------------

def evaluate_risk(sensor):

    explanations = []
    risk_score = 0

    # --- Prolonged lying detection ---
    if sensor["posture"] == "lying" and sensor["time_in_posture"] > 40:
        explanations.append(
            "Subject has remained lying down for an unusually long duration."
        )
        risk_score += 0.35

    # --- Abnormal heart rate ---
    if sensor["heart_rate"] > 95:
        explanations.append(
            "Elevated heart rate detected beyond normal resting range."
        )
        risk_score += 0.30

    if sensor["heart_rate"] < 55:
        explanations.append(
            "Heart rate lower than expected physiological baseline."
        )
        risk_score += 0.25

    # --- Low movement anomaly ---
    if sensor["movement_level"] < 0.2:
        explanations.append(
            "Minimal body movement observed suggesting inactivity or immobility."
        )
        risk_score += 0.20

    # --- Combined context reasoning ---
    if (
        sensor["posture"] == "lying"
        and sensor["heart_rate"] > 90
        and sensor["movement_level"] < 0.2
    ):
        explanations.append(
            "Posture, cardiac response, and inactivity together indicate potential distress."
        )
        risk_score += 0.40

    risk_score = min(risk_score, 1.0)

    # Final AI conclusion
    if risk_score < 0.3:
        status = "Stable Condition"
    elif risk_score < 0.6:
        status = "Moderate Risk"
    else:
        status = "High Risk — Intervention Recommended"

    return risk_score, status, explanations
