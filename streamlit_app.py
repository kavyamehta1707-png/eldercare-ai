import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="ElderCare AI Monitoring",
    layout="wide"
)

# -----------------------------
# BLUE LIGHT THEME
# -----------------------------
st.markdown("""
<style>
body {
    background-color:#F8FAFC;
}
.block-container {
    padding-top:2rem;
}
h1,h2,h3 {
    color:#1D4ED8;
}
.metric-box {
    background:#EFF6FF;
    padding:15px;
    border-radius:10px;
    border:1px solid #BFDBFE;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "logs" not in st.session_state:
    st.session_state.logs = []

# -----------------------------
# AI SIMULATION ENGINE
# -----------------------------
def simulate_ai_event():

    heart_rate = random.randint(50,130)
    motion = random.choice(["Normal Movement",
                            "Low Movement",
                            "No Movement",
                            "Sudden Impact"])

    posture = random.choice(["Walking",
                             "Sitting",
                             "Standing",
                             "Lying Down"])

    risk = "Safe"
    explanation = "Normal daily activity detected."

    # --- AI Reasoning Rules ---
    if posture == "Lying Down" and heart_rate > 105:
        risk = "High Risk"
        explanation = "Prolonged lying posture combined with elevated heart rate."

    elif motion == "No Movement" and heart_rate < 55:
        risk = "High Risk"
        explanation = "Extended inactivity with low heart rate indicating possible unconsciousness."

    elif motion == "Sudden Impact":
        risk = "Critical"
        explanation = "Sudden impact followed by posture change suggests fall event."

    elif posture == "Lying Down":
        risk = "Warning"
        explanation = "User stationary for extended duration."

    elif heart_rate > 110:
        risk = "Warning"
        explanation = "Abnormally high heart rate detected."

    elif heart_rate < 52:
        risk = "Warning"
        explanation = "Heart rate below normal resting threshold."

    event = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Heart Rate": heart_rate,
        "Posture": posture,
        "Motion": motion,
        "Risk": risk,
        "Explanation": explanation
    }

    return event

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Screen",
    [
        "Dashboard",
        "Emergency Alert",
        "AI Logs",
        "Health Insights",
        "Device Status"
    ]
)

# ======================================================
# DASHBOARD
# ======================================================
if page == "Dashboard":

    st.title("AI Caregiver Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Hub Status", "Connected")

    with col2:
        st.metric("Pendant Battery", "82%")

    with col3:
        st.metric("Monitoring Mode", "Active")

    st.divider()

    if st.button("Run AI Monitoring Simulation"):

        event = simulate_ai_event()
        st.session_state.logs.insert(0, event)

        st.success("AI Analysis Completed")

        c1, c2, c3 = st.columns(3)

        c1.metric("Heart Rate", event["Heart Rate"])
        c2.metric("Posture", event["Posture"])
        c3.metric("Risk Level", event["Risk"])

        st.info(event["Explanation"])

# ======================================================
# EMERGENCY SCREEN
# ======================================================
elif page == "Emergency Alert":

    st.title("Emergency Response Center")

    if len(st.session_state.logs) == 0:
        st.warning("No events detected yet.")
    else:
        event = st.session_state.logs[0]

        if event["Risk"] in ["High Risk", "Critical"]:
            st.error("Emergency Condition Detected")

            st.subheader("AI Assessment")
            st.write(event["Explanation"])

            col1, col2 = st.columns(2)

            col1.metric("Heart Rate", event["Heart Rate"])
            col2.metric("Posture", event["Posture"])

            st.subheader("Escalation Timeline")

            st.write("1. Voice confirmation initiated")
            st.write("2. Caregiver notified")
            st.write("3. Emergency contact escalation ready")

            if st.button("Simulate Caregiver Response"):
                st.success("Caregiver acknowledged alert.")

        else:
            st.success("No active emergency.")

# ======================================================
# AI LOGS
# ======================================================
elif page == "AI Logs":

    st.title("AI Event Log")

    if len(st.session_state.logs) == 0:
        st.info("No monitoring events yet.")
    else:
        df = pd.DataFrame(st.session_state.logs)
        st.dataframe(df, use_container_width=True)

# ======================================================
# HEALTH INSIGHTS
# ======================================================
elif page == "Health Insights":

    st.title("Health Insights")

    if len(st.session_state.logs) < 3:
        st.info("Generate more events to view trends.")
    else:
        df = pd.DataFrame(st.session_state.logs)

        st.line_chart(df["Heart Rate"])

        avg_hr = int(df["Heart Rate"].mean())

        st.subheader("AI Summary")

        if avg_hr > 100:
            st.warning("Average heart rate elevated over monitoring period.")
        elif avg_hr < 55:
            st.warning("Average heart rate below recommended level.")
        else:
            st.success("Vital patterns within normal range.")

# ======================================================
# DEVICE STATUS
# ======================================================
elif page == "Device Status":

    st.title("Device Diagnostics")

    col1, col2 = st.columns(2)

    col1.metric("Hub Connectivity", "Stable")
    col1.metric("Firmware Version", "v1.0.3")

    col2.metric("Pendant Signal", "Strong")
    col2.metric("Battery Health", "Good")

    st.divider()

    st.write("All systems operating normally.")
