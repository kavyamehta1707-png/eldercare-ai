import streamlit as st
from ai_engine import generate_sensor_data, evaluate_risk
import time

# ------------------------------------------------
# Page Setup
# ------------------------------------------------

st.set_page_config(
    page_title="ElderCare AI",
    layout="wide",
    page_icon="🩺"
)

st.title("🩺 ElderCare AI Monitoring System")
st.caption("AI-Powered Elderly Safety & Caregiver Intelligence Platform")

st.divider()

# ------------------------------------------------
# Generate AI Sensor Data
# ------------------------------------------------

sensor = generate_sensor_data()
risk, status, explanations = evaluate_risk(sensor)

# ------------------------------------------------
# Dashboard Layout
# ------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Posture", sensor["posture"].capitalize())
col2.metric("Heart Rate", f"{sensor['heart_rate']:.0f} BPM")
col3.metric("Movement Level", f"{sensor['movement_level']:.2f}")
col4.metric("Time in Posture", f"{sensor['time_in_posture']} min")

st.divider()

# ------------------------------------------------
# AI Risk Section
# ------------------------------------------------

st.subheader("🧠 AI Risk Assessment")

st.progress(risk)

if risk < 0.3:
    st.success(status)
elif risk < 0.6:
    st.warning(status)
else:
    st.error(status)

# ------------------------------------------------
# Explainable AI Output
# ------------------------------------------------

st.subheader("🔎 AI Reasoning")

if explanations:
    for exp in explanations:
        st.write("•", exp)
else:
    st.write("No abnormal behavioural patterns detected.")

st.divider()

# ------------------------------------------------
# Emergency Simulation
# ------------------------------------------------

st.subheader("🚨 Emergency Controls")

colA, colB = st.columns(2)

with colA:
    if st.button("Simulate Fall Event"):
        st.error("🚨 FALL DETECTED — Caregiver Notified")

with colB:
    if st.button("Refresh Monitoring"):
        st.rerun()

# ------------------------------------------------
# Footer
# ------------------------------------------------

st.caption("Prototype demonstration using synthetic sensor intelligence.")
