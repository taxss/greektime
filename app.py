import streamlit as st
import time
import random
from datetime import datetime, timedelta

# Config
st.set_page_config(page_title="GreekTime Predictor", page_icon="🇬🇷", layout="wide")

# Logo
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

# Event type buttons in grid
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
event_cols = st.columns(5)

for i in range(5):
    key, label = event_labels[i]
    with event_cols[i]:
        if st.button(label, key=key):
            st.session_state.event_type = key

event_type = st.session_state.event_type
st.caption(f"Selected event: **{event_type}**")

# Greekness slider
MAX_DELAY_MINUTES = 46

st.markdown("### How Greek is your Greek?")
greekness_score = st.slider(
    "Slide to increase the probability of delay.",
    min_value=0,
    max_value=100,
    value=30,
    step=1,
    help="0 = Barely Greek, 100 = Spoke to their mom 12 times today"
)

mod_minutes = round((greekness_score / 100) * MAX_DELAY_MINUTES)

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
        "Recounting last-minute family emergencies...",
        "Greeksplaining traffic to a satellite..."
    ]

st.divider()

# Core calculator logic
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
        st.caption("They’ll still be 3 minutes late. And blame traffic caused by a priest's funeral.")

st.divider()

# Tips & Tricks section
st.markdown("## Tips & Tricks to Make Greeks Arrive Sooner")
st.markdown("""
- **Say it’s a nameday and there’s free food.** Instant teleportation.
- **Tell them everyone’s already there.** Greek shame is real.
- **Mention someone is parking in their usual spot.** They’ll storm out.
- **Text: “they’re talking politics without you.”** They'll break speed limits.
- **Say their mom is waiting.** Fear beats inertia.
- **Only Turk joke:** _“Apparently the Turks always arrive on time.”_ Guaranteed panic.
""")

# Tech section
st.markdown("## 🤖 The Technology Behind GreekTime Predictor")
st.markdown("""
GreekTime Predictor is powered by a proprietary delay estimation engine built on bleeding-edge technologies, including:

- **Quantum Probability Modeling**, trained on ferry timetables and Athenian café density data.
- **Space-grade Delay Propagation Systems**, originally developed for spacecraft reentry but retooled to measure cousin-related delays.
- **Neural Excuse Networks (NENs)**, trained on 87,000+ Greek WhatsApp apologies.
- **Geolocation Interference Algorithms**, factoring in bakery stops, soccer rants, and accidental beach detours.
- **Mood-Lag Analytics**, adjusting arrival time based on how many times they've said “malaka” today.

Each result is reviewed by a certified uncle from Thessaloniki with access to a chair, a cigarette, and mystical powers.
""")

# FAQ
st.divider()
st.markdown("## ❓ FAQ")

with st.expander("Why is my Greek coworker always late?"):
    st.markdown("They aren't late — **you're just early in the wrong culture.** Also: there was traffic, a chatty neighbor, and the need for coffee.")

with st.expander("What if they're on time?"):
    st.markdown("It’s either a trap, or their mom made them leave early. Tread carefully.")

with st.expander("Does this work for Cypriots?"):
    st.markdown("Yes, but you’ll need to apply a **+45% regional buffer** and triple-check political sensitivities.")

with st.expander("Is this scientifically accurate?"):
    st.markdown("More accurate than most weather apps, less accurate than your Greek aunt’s gossip. Calibrated to within ±3 souvlakis.")
