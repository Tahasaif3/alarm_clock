import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Alarm Clock",
    page_icon=":alarm_clock:",
    layout="centered"
)

# Function to play alarm sound
def play_alarm_sound():
    st.audio("alarm_sound.mp3", format="audio/mp3", autoplay=True)
    # pygame.mixer.init()
    # pygame.mixer.music.load("sound.wav")  # Ensure you have an alarm_sound.mp3 file
    # pygame.mixer.music.play()

# Sidebar Navigation
sidebar_selection = st.sidebar.radio("Navigation", ["Home", "Project", "Contact Us", "About Us"])

if sidebar_selection == "Home":
    st.title("Alarm Clock Project")
    st.write("Welcome to the Alarm Clock Project")

elif sidebar_selection == "Project":
    st.title("Alarm Clock Project")
    st.write("Create a personalized alarm clock with date and sound features using Streamlit.")

    # Get user input for the alarm date
    alarm_date = st.date_input("Set alarm date", datetime.today())

    # Set Alarm Time
    alarm_time = st.time_input("Set Alarm Time", datetime.now().time())

    # Combine the selected date and time
    alarm_datetime = datetime.combine(alarm_date, alarm_time)

    # Set Snooze Duration
    snooze_duration = st.slider("Snooze Duration (minutes)", 1, 60, 5)

    if st.button("Start Alarm"):
        st.write(f"Alarm set for {alarm_datetime}")

        # Wait until the alarm time
        while datetime.now() < alarm_datetime:
            time.sleep(1)

        st.success("⏰ Wake up! It's time!")
        play_alarm_sound()

        # Snooze logic
        snooze_time = datetime.now() + timedelta(minutes=snooze_duration)

        while True:
            current_time = datetime.now()

            if current_time >= snooze_time:
                st.warning("⏳ Snooze time's up!")
                play_alarm_sound()
                snooze_time = current_time + timedelta(minutes=snooze_duration)

            time.sleep(1)

elif sidebar_selection == "Contact Us":
    st.title("Contact Us")
    st.write("Made By: Taha Saif")
    st.write("Email: tahasaif454@gmail.com")
    st.write("Contact: 0316-3836744")
    st.write("GitHub: [Tahasaif3](https://github.com/Tahasaif3)")

elif sidebar_selection == "About Us":
    st.title("About Us")
    st.write("Welcome to the Streamlit Alarm Clock project! This application provides a personalized and flexible alarm experience.")
