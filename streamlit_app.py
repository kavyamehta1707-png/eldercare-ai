import streamlit as st
import numpy as np
import random
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="ElderCare AI Monitoring System",
    layout="wide"
)

# -------------------------------------------------
# CLEAN LIGHT UI STYLE
# -------------------------------------------------
st.markdown("""
<style>
.big-title{
    font-size:34px;
    font-weight:700;
    color:#0B3C49;
}
.subtitle{
    color:#6c757d;
    margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown('<div class="big-title">ElderCare AI Monitoring Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered elderly safety and caregiver intelligence system</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# SYNTHETIC SENSOR DATA
# -------------------------------------------------
posture = random.choice(["Standing","Walking","Sitting","Lying"])
heart_rate = np.random.randint(50,120)
movement = round(np.random.uniform(0,1),2)
time_posture = random.randint(1,120)
temperature = round(np.random.normal(36.7,0.5),1)
time_of_day = random.choice(["Morning","Afternoon","Night"])

sensor = {
    "posture": posture,
    "heart_rate": heart_rate,
    "movement": movement,
    "time_posture": time_posture,
    "temperature": temperature,
    "time_of_day": time_of_day
}

# -------------------------------------------------
# DASHBOARD METRICS
# -------------------------------------------------
c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("Posture", posture)
c2.metric("Heart Rate", f"{heart_rate} BPM")
c3.metric("Movement Level", movement)
c4.metric("Time in Posture", f"{time_posture} min")
c5.metric("Body Temperature", f"{temperature} °C")
c6.metric("Time of Day", time_of_day)

st.divider()

# -------------------------------------------------
# EXPLAINABLE AI ENGINE
# -------------------------------------------------
risk = 0
explanations = []

# Individual Signals
if heart_rate > 100:
    explanations.append("Elevated heart rate detected.")
    risk += 0.25

if heart_rate < 55:
    explanations.append("Unusually low heart rate observed.")
    risk += 0.25

if movement < 0.15:
    explanations.append("Very low body movement detected.")
    risk += 0.20

if temperature > 37.8:
    explanations.append("Body temperature indicates possible fever.")
    risk += 0.15

# Contextual AI Combinations

if posture=="Lying" and time_posture>45 and heart_rate>95:
    explanations.append(
        "Prolonged lying combined with elevated heart rate suggests possible distress or fall."
    )
    risk += 0.40

if posture=="Lying" and movement<0.15 and time_posture>40:
    explanations.append(
        "Extended immobility detected. User may be unconscious or unable to move."
    )
    risk += 0.35

if posture=="Lying" and time_of_day=="Afternoon" and movement<0.1:
    explanations.append(
        "Unexpected prolonged rest during active hours detected."
    )
    risk += 0.25

if posture=="Standing" and movement<0.1 and heart_rate<55:
    explanations.append(
        "Standing posture with low cardiac response may indicate dizziness risk."
    )
    risk += 0.30

if heart_rate>105 and movement<0.2:
    explanations.append(
        "Cardiac stress without physical activity detected."
    )
    risk += 0.35

if temperature>38 and movement<0.2:
    explanations.append(
        "High temperature with inactivity suggests illness or fatigue."
    )
    risk += 0.30

risk = min(risk,1.0)

# -------------------------------------------------
# RISK STATUS
# -------------------------------------------------
if risk < 0.3:
    status = "Stable Condition"
elif risk < 0.6:
    status = "Moderate Risk Detected"
else:
    status = "High Risk — Immediate Attention Recommended"

# -------------------------------------------------
# MAIN LAYOUT
# -------------------------------------------------
left,right = st.columns([2,1])

with left:

    st.subheader("AI Risk Assessment")

    st.progress(risk)

    if risk < 0.3:
        st.success(status)
    elif risk < 0.6:
        st.warning(status)
    else:
        st.error(status)

    st.subheader("Explainable AI Reasoning")

    if explanations:
        for exp in explanations:
            st.write(exp)
    else:
        st.write("No abnormal behavioural pattern detected.")

with right:

    st.subheader("Caregiver Actions")

    if st.button("Notify Caregiver"):
        st.success("Caregiver notification sent.")

    if st.button("Request Emergency Assistance"):
        st.error("Emergency response triggered.")

    if st.button("Mark Patient Safe"):
        st.info("Status updated to safe.")

st.divider()

# -------------------------------------------------
# HEALTH TREND GRAPH
# -------------------------------------------------
st.subheader("Health Trend Overview")

data = pd.DataFrame(
    np.random.randn(30,3),
    columns=["Heart Rate Trend","Activity Level","AI Risk Trend"]
)

st.line_chart(data)

st.caption("Prototype demonstration using simulated AI monitoring data.")}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="big-title">🩺 ElderCare AI Monitoring Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered elderly safety & caregiver intelligence system</div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# FAKE SENSOR DATA
# -----------------------------
posture = random.choice(["Standing","Walking","Sitting","Lying"])
heart_rate = np.random.randint(60,110)
movement = round(np.random.uniform(0,1),2)
time_posture = random.randint(1,120)

# -----------------------------
# STATUS BAR
# -----------------------------
col1,col2,col3,col4 = st.columns(4)

col1.metric("🧍 Posture", posture)
col2.metric("❤️ Heart Rate", f"{heart_rate} BPM")
col3.metric("📉 Movement Level", movement)
col4.metric("⏱ Time in Posture", f"{time_posture} min")

st.divider()

# -----------------------------
# AI RISK LOGIC
# -----------------------------
risk = 0
explanations=[]

if posture=="Lying" and time_posture>40:
    explanations.append("Prolonged lying detected.")
    risk+=0.35

if heart_rate>95:
    explanations.append("Elevated heart rate beyond resting level.")
    risk+=0.30

if movement<0.2:
    explanations.append("Minimal movement observed.")
    risk+=0.25

risk=min(risk,1)

# -----------------------------
# MAIN DASHBOARD
# -----------------------------
left,right = st.columns([2,1])

# LEFT SIDE
with left:
    st.subheader("🧠 AI Risk Assessment")

    st.progress(risk)

    if risk<0.3:
        st.success("Stable Condition")
    elif risk<0.6:
        st.warning("Moderate Risk Detected")
    else:
        st.error("⚠ High Risk — Intervention Recommended")

    st.subheader("🔎 Explainable AI Reasoning")

    if explanations:
        for e in explanations:
            st.write("✔",e)
    else:
        st.write("No abnormal behavioural pattern detected.")

# RIGHT SIDE
with right:
    st.subheader("🚨 Emergency Panel")

    st.button("📞 Notify Caregiver")
    st.button("🚑 Call Emergency Service")
    st.button("✅ Mark Safe")

st.divider()

# -----------------------------
# ANALYTICS SECTION
# -----------------------------
st.subheader("📊 Health Trend Overview")

chart_data = np.random.randn(30,2)
st.line_chart(chart_data)

st.caption("Prototype interface using simulated AI monitoring data.")
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
