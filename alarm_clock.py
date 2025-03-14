import streamlit as st
import datetime
import time
import threading
import winsound

# Global variable to track if the alarm is active
alarm_running = False

def play_alarm():
    for _ in range(5):  # Play sound 5 times
        if not alarm_running:
            break
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
        time.sleep(1)

def alarm(set_alarm_time):
    global alarm_running
    alarm_running = True

    while alarm_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)

        if current_time == set_alarm_time and alarm_running:
            st.session_state.status = "⏰ Alarm Ringing!"
            play_alarm()
            break

    if alarm_running:
        st.session_state.status = "✅ Alarm Completed"
    else:
        st.session_state.status = "🛑 Alarm Stopped"

def set_alarm():
    global alarm_running

    h = st.session_state.hour.zfill(2)
    m = st.session_state.minute.zfill(2)
    s = st.session_state.second.zfill(2)

    if not (h.isdigit() and m.isdigit() and s.isdigit()):
        st.warning("⚠️ Please enter a valid time!")
        return

    set_alarm_time = f"{h}:{m}:{s}"
    st.session_state.status = f"⏳ Alarm set for {set_alarm_time}"

    # Start alarm thread
    alarm_thread = threading.Thread(target=alarm, args=(set_alarm_time,))
    alarm_thread.daemon = True
    alarm_thread.start()

def stop_alarm():
    global alarm_running
    alarm_running = False
    st.session_state.status = "🛑 Alarm Stopped"

# Streamlit UI
st.set_page_config(page_title="Alarm Clock", page_icon="⏰")
st.title("⏰ Alarm Clock")

st.markdown("### Set Alarm Time (24-Hour Format)")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Hour", key="hour", max_chars=2, placeholder="HH")
with col2:
    st.text_input("Minute", key="minute", max_chars=2, placeholder="MM")
with col3:
    st.text_input("Second", key="second", max_chars=2, placeholder="SS")

# Set and Stop buttons
col1, col2 = st.columns(2)
with col1:
    st.button("✅ Set Alarm", on_click=set_alarm)
with col2:
    st.button("🛑 Stop Alarm", on_click=stop_alarm)

# Display status
st.markdown("### Status")
st.info(st.session_state.get("status", "No Alarm Set"))

# Display current time
def update_time():
    while True:
        st.session_state.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)

if "current_time" not in st.session_state:
    st.session_state.current_time = datetime.datetime.now().strftime("%H:%M:%S")
    threading.Thread(target=update_time, daemon=True).start()

st.markdown(f"### Current Time: `{st.session_state.current_time}`")

st.caption("Note: Ensure `sound.wav` is placed in the same directory.")
