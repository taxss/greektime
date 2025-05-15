import streamlit as st
import time
import random
from datetime import datetime, timedelta

# App config
st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

# Logo & Header
st.markdown("""
<div style="text-align: center;">
    <img src="https://tzxivjnghmvwnizzfwrh.supabase.co/storage/v1/object/public/pics//output-onlinepngtools.png"
         alt="GreekTime Predictor Logo"
         style="max-width: 220px; margin-bottom: 0.5rem;">
    <p style="font-style: italic; color: gray;">Advanced Ai Calendar De-Greekifier, for free!</p>
</div>
""", unsafe_allow_html=True)

# Mode selection
mode = st.radio("Choose your mode:", [
    "When will the Greek actually arrive?",
    "When to invite a Greek so they’re on time?"
])

# Event type buttons
st.markdown("### What kind of event is it?")

if "event_type" not in st.session_state:
    st.session_state.event_type = "Casual hangout"

event_options = {
    "Casual hangout": "🧃 Casual Hangout",
    "Dinner": "🍽️ Dinner",
    "Work meeting": "💼 Work Meeting",
    "Serious meeting": "📊 Serious Meeting",
    "Special event": "🎉 Special Event"
}

event_labels = list(event_options.items())
button_cols = st.columns(len(event_labels))

for i, (key, label) in enumerate(event_labels):
    with button_cols[i]:
        if st.button(label, key=key):
            st.session_state.event_type = key

event_type = st.session_state.event_type
st.caption(f"**Selected Event:** {event_type}")

# Greekness Slider with style
MAX_DELAY_MINUTES = 46
DELAY_VARIANCE = 3

st.markdown("### How Greek is your Greek?")

slider_css = """
<style>
.stSlider > div[data-baseweb="slider"] > div {
    background: linear-gradient(to right, #0D5BA1 0%, #0D5BA1 100%) !important;
}
</style>
"""

st.markdown(slider_css, unsafe_allow_html=True)

greekness_score = st.slider(
    "Slide to increase Greekness.",
    min_value=0,
    max_value=100,
    value=30,
    step=1
)

raw_delay = (greekness_score / 100) * MAX_DELAY_MINUTES
mod_minutes = round(raw_delay + random.uniform(-DELAY_VARIANCE, DELAY_VARIANCE))

if greekness_score == 0:
    greek_profile = "Barely Greek"
elif greekness_score < 25:
    greek_profile = "Lightly Greek"
elif greekness_score < 50:
    greek_profile = "Slightly Greek"
elif greekness_score < 75:
    greek_profile = "Very Greek"
else:
    greek_profile = "Extremely Greek"

st.markdown(f"""
<div style="padding: 0.5rem 0; font-size: 1.1rem;">
<strong>Estimated Additional Delay Factor:</strong> <span style="color:#0D5BA1;"><strong>{greek_profile}</strong></span> (≈ <strong>{mod_minutes} min</strong>)
</div>
""", unsafe_allow_html=True)

# Delay logic
lateness_factors = {
    "Casual hangout": 33,
    "Dinner": 22,
    "Work meeting": 16,
    "Serious meeting": 8,
    "Special event": 30
}
base_minutes = lateness_factors.get(event_type, 10)
total_delay = base_minutes + mod_minutes

# Spinner jokes
if greekness_score <= 25:
    joke_lines = [
        "Tuning the komboloi...",
        "Adjusting frappe viscosity...",
        "Charging the GPS..."
    ]
elif greekness_score <= 75:
    joke_lines = [
        "Consulting yiayia’s calendar...",
        "Lighting a freddospresso...",
        "Warming up excuses module..."
    ]
else:
    joke_lines = [
        "Spinning souvlaki logic cores...",
        "Recounting last-minute emergencies...",
        "Greeksplaining traffic to a satellite..."
    ]

st.divider()

# Core logic
if mode == "When will the Greek actually arrive?":
    user_time = st.time_input("🕒 Scheduled time")
    if st.button("📡 Predict Arrival"):
        with st.spinner(random.choice(joke_lines)):
            time.sleep(3.5)
        scheduled = datetime.combine(datetime.today(), user_time)
        arrival = scheduled + timedelta(minutes=total_delay)
        st.success(f"🎯 The Greek will probably arrive at **{arrival.strftime('%H:%M')}**.")
        st.caption("...if you're lucky.")
else:
    desired_time = st.time_input("🕖 Desired arrival time")
    if st.button("📩 Suggest Invite Time"):
        with st.spinner(random.choice(joke_lines)):
            time.sleep(3.5)
        desired = datetime.combine(datetime.today(), desired_time)
        invite_time = desired - timedelta(minutes=total_delay)
        st.success(f"📬 You should tell the Greek that the event is at **{invite_time.strftime('%H:%M')}**.")
        st.caption("They’ll still be 3 minutes late. And blame traffic.")

st.divider()

# Tips & Tricks
st.markdown("## Tips & Tricks to Make Greeks Arrive Sooner")
st.markdown("""
- **Say it’s a nameday and there’s free food.** Instant teleportation.
- **Tell them everyone’s already there.** Greek shame is real.
- **Text: “they’re talking politics without you.”** They'll break speed limits.
- **Only Turk joke:** _“Apparently the Turks always arrive on time.”_ Guaranteed panic.
""")

# Tech explanation
st.markdown("##The Technology Behind GreekTime Predictor")
st.markdown("""
GreekTime Predictor is powered by a proprietary delay estimation engine built on bleeding-edge technologies, including:

- **Quantum Probability Modeling**, trained on ferry timetables and Athenian café density data.
- **Space-grade Delay Propagation Systems**, originally developed for spacecraft reentry but retooled to measure cousin-related delays.
- **Neural Excuse Networks (NENs)**, trained on 87,000+ Greek WhatsApp apologies.
- **Geolocation Interference Algorithms**, factoring in bakery stops, soccer rants, and accidental beach detours.
- **Mood-Lag Analytics**, adjusting arrival time based on how many times they've said “malaka” today.

Each result is reviewed by our dedicated support team on Mount Athos.
""")

# FAQ
st.divider()
st.markdown("## ❓ FAQ")

with st.expander("Why is my Greek coworker always late?"):
    st.markdown("They aren't late,  **you're just early in the wrong culture.** Also: there was traffic, an ourgent call, and a need for coffee.")

with st.expander("What if they're on time?"):
    st.markdown("It’s a trap, avoid eye contact. Tread carefully.")

with st.expander("Does this work for Cypriots?"):
    st.markdown("Yes, but you’ll need to apply a **+45% regional buffer** and triple-check political sensitivities.")

with st.expander("Is this scientifically accurate?"):
    st.markdown("More accurate than most weather apps, less accurate than the office gossip. Calibrated to within ±3 souvlakis.")
