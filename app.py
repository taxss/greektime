import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="centered")

st.title("🇬🇷 GreekTime Predictor")
st.subheader("Never trust a calendar invite again.")

mode = st.radio("Choose your mode:", [
    "😅 When will the Greek actually arrive?",
    "🧠 When should I invite the Greek so they’re on time?"
])

event_type = st.selectbox("What kind of event is it?", [
    "Casual hangout", "Dinner", "Work meeting", "Serious meeting", "Special event"
])

greek_profile = st.selectbox("What kind of Greek are we dealing with?", [
    "Usually on time", "Slightly late", "Very Greek", "Extremely Greek"
])

lateness_factors = {
    "Casual hangout": 25,
    "Dinner": 18,
    "Work meeting": 10,
    "Serious meeting": 5,
    "Special event": 30
}

punctuality_modifiers = {
    "Usually on time": 0,
    "Slightly late": 7,
    "Very Greek": 15,
    "Extremely Greek": 30
}

base_minutes = lateness_factors[event_type]
mod_minutes = punctuality_modifiers[greek_profile]
total_delay = base_minutes + mod_minutes

if mode == "😅 When will the Greek actually arrive?":
    user_time = st.time_input("Scheduled time")
    if st.button("Predict Arrival"):
        scheduled = datetime.combine(datetime.today(), user_time)
        arrival = scheduled + timedelta(minutes=total_delay)
        st.success(f"🎯 The Greek will probably arrive at **{arrival.strftime('%H:%M')}**.")
        st.caption("...if you're lucky.")
else:
    desired_time = st.time_input("Desired arrival time")
    if st.button("Suggest Invite Time"):
        desired = datetime.combine(datetime.today(), desired_time)
        invite_time = desired - timedelta(minutes=total_delay)
        st.success(f"📩 You should invite the Greek at **{invite_time.strftime('%H:%M')}**.")
        st.caption("They’ll still be 3 minutes late.")

