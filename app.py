import streamlit as st
import time
import random
from datetime import datetime, timedelta

# App config
st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

# Logo & Header
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://tzxivjnghmvwnizzfwrh.supabase.co/storage/v1/object/public/pics//output-onlinepngtools.png"
             alt="GreekTime Predictor Logo"
             style="max-width: 220px; margin-bottom: 0.5rem;">
        <p style="font-style: italic; color: gray;">Advanced Ai Calendar De-Greekifier, for free!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Mode selection
mode = st.radio("Choose your mode:", [
    "When will the Greek actually arrive?",
    "When to invite a Greek so they’re on time?"
])

# Event buttons
st.markdown("### What kind of event is it?")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🧃 Casual Hangout"):
        event_type = "Casual hangout"
with col2:
    if st.button("🍽️ Dinner"):
        event_type = "Dinner"
with col3:
    if st.button("💼 Work Meeting"):
        event_type = "Work meeting"
col4, col5 = st.columns(2)
with col4:
    if st.button("📊 Serious Meeting"):
        event_type = "Serious meeting"
with col5:
    if st.button("🎉 Special Event"):
        event_type = "Special event"
if 'event_type' not in locals():
    event_type = "Casual hangout"

# Greekness slider
st.markdown("### How Greek is your Greek?")
greekness_score = st.slider(
    "Slide to increase the probability of delay.",
    min_value=0,
    max_value=100,
    value=30,
    step=1,
    help="0 = Barely Greek, 100 = Dionysus reborn"
)

# Delay scale: 0–30 min
mod_minutes = round((greekness_score / 100) * 30)

# Dynamic profile label
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

st.caption(f"Profile: **{greek_profile}** | Estimated delay: **{mod_minutes} min**")

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

# Spinner jokes based on Greekness level
mild_jokes = [
    "Consulting Greek calendar...",
    "Charging GPS...",
    "Counting ouzos...",
]
moderate_jokes = [
    "Consulting yiayia’s calendar...",
    "Lighting a freddospresso...",
    "Staring at sandals waiting for movement...",
]
extreme_jokes = [
    "Spinning komboloi beads with maximum intention...",
    "Double-checking WhatsApp excuses...",
    "Greeksplaining traffic to a satnav...",
]

if greekness_score <= 25:
    joke_lines = mild_jokes
elif greekness_score <= 75:
    joke_lines = moderate_jokes
else:
    joke_lines = extreme_jokes

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
        st.caption("They’ll still be 3 minutes late. Or say ‘I'm 5 minutes away’ from another country.")

st.divider()

# Tips & Tricks
st.markdown("## 🧠 Tips & Tricks to Make Greeks Arrive Sooner (or Less Late)")
st.markdown("""
- **Blame the Turks.** Doesn’t matter how. “The Turks are never late” often works.
- **Say there's free parking, even if there isn't.** It’s called tactical misinformation.
- **Tell them their ex is already inside.** Rage is more powerful than coffee.
- **Mention “unlimited mezze.”** Greeks have built cities for less.
- **Say the start time was published in a Turkish newspaper.** They will show up 15 minutes early on principle.
""")

# Tech explanation
st.markdown("## 🤖 The Technology Behind GreekTime Predictor")
st.markdown("""
GreekTime Predictor runs on an advanced stack blending AI, quantum computing, and geopolitical databases. Key components include:

- **Quantum Probability Modeling** trained on Cycladic ferry data and Byzantine transcripts.
- **Space-grade Delay Propagation Systems**, originally developed to model time distortion in interstellar travel.
- **Neural Excuse Networks (NENs)** trained on 87,000 Greek text messages containing the words “sorry,” “traffic,” and “you won’t believe this.”
- **Emotional Latency Indexing**, which adjusts arrival times based on mood swings, political arguments, and Mercury retrograde.

Each prediction is independently validated by our dedicated team on Mount Athos.
""")

# FAQ
st.divider()
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("Why is my Greek coworker always late?"):
    st.markdown("They aren't late, **you're just early or wrong.** Also: they needed to stop for a coffee, a phone call, a souvlaki, or an existential crisis.")

with st.expander("What if they're on time?"):
    st.markdown("It's a trap. Remain calm, don't make eye contact, and check your calendar again.")

with st.expander("Does this work for Cypriots?"):
    st.markdown("Yes, but with **+45% delay buffer** and higher risk of political debate on arrival.")

with st.expander("Is it scientifically accurate?"):
    st.markdown("More accurate than your last 3 relationships. Calibrated to within ±3 souvlakis.")
