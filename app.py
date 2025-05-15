import streamlit as st
import time
import random
from datetime import datetime, timedelta

# ---------- Page Config ----------
st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

# ---------- Global CSS ----------
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .centered {
        text-align: center;
    }
    .stButton > button {
        width: 100%;
        padding: 0.5rem;
        border-radius: 10px;
        font-weight: 600;
    }
    .event-row {
        display: flex;
        justify-content: space-between;
        gap: 0.5rem;
        margin-top: 0.5rem;
    }
    .slider-wrapper {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        background-color: #0D5BA115;
        border-radius: 10px;
    }
    .delay-label {
        font-size: 1.1rem;
        margin-top: 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="centered">
    <img src="https://tzxivjnghmvwnizzfwrh.supabase.co/storage/v1/object/public/pics//output-onlinepngtools.png"
         style="max-width: 180px; margin-bottom: 0.5rem;" />
    <p style="color: gray; font-style: italic;">Advanced Ai Calendar De-Greekifier, for free!</p>
</div>
""", unsafe_allow_html=True)

# ---------- Mode ----------
mode = st.radio("Choose your mode:", [
    "When will the Greek actually arrive?",
    "When to invite a Greek so they’re on time?"
])

# ---------- Event Buttons ----------
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

cols = st.columns(5)
for i, (key, label) in enumerate(event_options.items()):
    with cols[i]:
        if st.button(label):
            st.session_state.event_type = key

event_type = st.session_state.event_type
st.caption(f"**Selected Event:** {event_type}")

# ---------- Greekness Slider ----------
MAX_DELAY_MINUTES = 46
DELAY_VARIANCE = 3

st.markdown("### How Greek is your Greek?")
greekness_score = st.slider("Slide to increase Greekness.", 0, 100, 30, step=1)

# Delay calc
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

st.markdown(f'<div class="delay-label">Estimated Additional Delay Factor: <span style="color:#0D5BA1">{greek_profile}</span> (≈ <strong>{mod_minutes} min</strong>)</div>', unsafe_allow_html=True)

# ---------- Core Logic ----------
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
    joke_lines = ["Tuning the komboloi...", "Adjusting frappe viscosity...", "Charging the GPS..."]
elif greekness_score <= 75:
    joke_lines = ["Consulting yiayia’s calendar...", "Lighting a freddospresso...", "Warming up excuses module..."]
else:
    joke_lines = ["Spinning souvlaki logic cores...", "Recounting last-minute emergencies...", "Greeksplaining traffic to a satellite..."]

st.divider()

# ---------- Input & Result ----------
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
        st.caption("They’ll still be 3 minutes late. And blame traffic.")

st.divider()

# ---------- Technology ----------
st.markdown("## The Technology Behind GreekTime Predictor")
st.markdown("""
GreekTime Predictor is powered by a proprietary delay estimation engine built on bleeding-edge technologies, including:

- **Quantum Probability Modeling** trained on ferry timetables and Greek calendar change density data.  
- **Space-grade Delay Propagation Systems** repurposed from spacecraft reentry systems.  
- **Neural Excuse Networks (NENs)** trained on 87,000+ Greek WhatsApp apologies.  
- **Geolocation Interference Algorithms** factoring in emergency stops, Turk Rants, and tax avoidance data.  
- **Mood-Lag Analytics** adjusting based on how many times they’ve said “malaka” today.

Each prediction is reviewed by our certified support team on Mount Athos.
""")

# ---------- FAQ ----------
st.divider()
st.markdown("## ❓ FAQ")
with st.expander("Why is my Greek coworker always late?"):
    st.markdown("They aren't late — **you're just early in the wrong culture.** Also: there was traffic, an urgent call, and a need for coffee.")
with st.expander("What if they're on time?"):
    st.markdown("It’s a trap, avoid eye contact. Tread carefully.")
with st.expander("Does this work for Cypriots?"):
    st.markdown("Yes, but apply a **+45% regional buffer** and check for political risk.")
with st.expander("Is this scientifically accurate?"):
    st.markdown("More accurate than most weather apps, less accurate than the office gossip. Calibrated to within ±3 souvlakis.")
