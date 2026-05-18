import streamlit as st
import numpy as np
import random

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="ElderCare AI",
    layout="wide"
)

# -----------------------------
# CUSTOM LIGHT GUI STYLE
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #F8FBFD;
}

.metric-card {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

.big-title {
    font-size:32px;
    font-weight:700;
    color:#0B3C49;
}

.subtitle {
    color:#6c757d;
}
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
