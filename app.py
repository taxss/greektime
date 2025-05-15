import streamlit as st
import time
import random
from datetime import datetime, timedelta

# Light theme in .streamlit/config.toml
st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

st.markdown("## 🇬🇷 GreekTime Predictor")
st.markdown("*Never trust a calendar invite again.*")

mode = st.radio("Choose your mode:", [
    "When will the Greek actually arrive?",
    "When to invite a Greek so they’re on time?"
])

event_type = st.selectbox("What kind of event is it?", [
    "Casual hangout", "Dinner", "Work meeting", "Serious meeting", "Special event"
])

greek_profile = st.selectbox("What kind of Greek are we dealing with?", [
    "Minor Greek", "Slightly Greek", "Very Greek", "Extremely Greek"
])

lateness_factors = {
    "Casual hangout": 23,
    "Dinner": 18,
    "Work meeting": 10,
    "Serious meeting": 5,
    "Special event": 30
}

punctuality_modifiers = {
    "Minor Greek": 0,
    "Slightly Greek": 7,
    "Very Greek": 15,
    "Extremely Greek": 30
}

base_minutes = lateness_factors.get(event_type, 10)
mod_minutes = punctuality_modifiers.get(greek_profile, 0)
total_delay = base_minutes + mod_minutes

joke_lines = [
    "Counting souvlakis...",
    "Assembling excuses...",
    "Trying to find parking in Athens...",
    "Double-checking WhatsApp read receipts...",
    "Greeksplaining the delay...",
    "Consulting yiayia’s calendar...",
    "Lighting a frappe and praying for punctuality..."
]

st.divider()

if mode == "When will the Greek actually arrive?":
    user_time = st.time_input("🕒 Scheduled time")
    if st.button("📡 Predict Arrival"):
        with st.spinner(random.choice(joke_lines)):
            time.sleep(2.5)
        scheduled = datetime.combine(datetime.today(), user_time)
        arrival = scheduled + timedelta(minutes=total_delay)
        st.success(f"🎯 The Greek will probably arrive at **{arrival.strftime('%H:%M')}**.")
        st.caption("...if you're lucky.")
else:
    desired_time = st.time_input("🕖 Desired arrival time")
    if st.button("📩 Suggest Invite Time"):
        with st.spinner(random.choice(joke_lines)):
            time.sleep(2.5)
        desired = datetime.combine(datetime.today(), desired_time)
        invite_time = desired - timedelta(minutes=total_delay)
        st.success(f"📬 You should tell the Greek that the event is at **{invite_time.strftime('%H:%M')}**.")
        st.caption("They’ll still be 3 minutes late. Or maybe they’ll call and say ‘I'm five minutes away.’")

