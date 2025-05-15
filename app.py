import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

st.markdown("## 🇬🇷 GreekTime Predictor")
st.markdown("*Never trust a calendar invite again.*")

# Use expander for a cleaner look on mobile
with st.expander("Settings", expanded=True):
    mode = st.radio("Choose your mode:", [
        "When will the Greek actually arrive?",
        "When to invite a Greek so they’re on time?"
    ])

    event_type = st.selectbox("What kind of event is it?", [
        "Casual hangout", "Dinner", "Work meeting", "Serious meeting", "Special event"
    ])

    greek_profile = st.selectbox("What kind of Greek are we dealing with?", [
        "Barely Greek", "Slightly Greek", "Very Greek", "Extremely Greek"
    ])

lateness_factors = {
    "Casual hangout": 23,
    "Dinner": 18,
    "Work meeting": 10,
    "Serious meeting": 5,
    "Special event": 30
}

punctuality_modifiers = {
    "Barely Greek": 0,
    "Slightly Greek": 7,
    "Very Greek": 15,
    "Extremely Greek": 30
}

# Default safe fallback if someone chooses a label not mapped
base_minutes = lateness_factors.get(event_type, 10)
mod_minutes = punctuality_modifiers.get(greek_profile, 0)
total_delay = base_minutes + mod_minutes

st.divider()

if mode == "When will the Greek actually arrive?":
    user_time = st.time_input("🕒 Scheduled time")
    if st.button("📡 Predict Arrival"):
        scheduled = datetime.combine(datetime.today(), user_time)
        arrival = scheduled + timedelta(minutes=total_delay)
        st.success(f"🎯 The Greek will probably arrive at **{arrival.strftime('%H:%M')}**.")
        st.caption("...if you're lucky.")
else:
    desired_time = st.time_input("🕖 Desired arrival time")
    if st.button("📩 Suggest Invite Time"):
        desired = datetime.combine(datetime.today(), desired_time)
        invite_time = desired - timedelta(minutes=total_delay)
        st.success(f"📬 You should invite the Greek at **{invite_time.strftime('%H:%M')}**.")
        st.caption("They’ll still be 3 minutes late.")

# Add some breathing room at the bottom on mobile
st.markdown(" ")
