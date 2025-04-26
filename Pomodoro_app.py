import streamlit as st
import time
import random

# عبارات تحفيزية
motivational_quotes = [
    "Great job! Take a short break.",
    "You’re doing amazing!",
    "Stay strong, your goals are near!",
    "Proud of your progress!",
    "Small steps every day lead to big results!"
]

st.title("Pomodoro Motivator")

# مؤقت الجلسة (25 دقيقة) و مؤقت الاستراحة (15 دقيقة) بالثواني
work_time = 25 * 60  # 25 minutes
break_time = 15 * 60  # 15 minutes

# حالة الجلسة
if "session_active" not in st.session_state:
    st.session_state.session_active = False
    st.session_state.is_break = False
    st.session_state.start_time = None

# زر البدء
if st.button("Start" if not st.session_state.session_active else "Reset"):
    if not st.session_state.session_active:
        st.session_state.session_active = True
        st.session_state.is_break = False
        st.session_state.start_time = time.time()
    else:
        st.session_state.session_active = False
        st.rerun()

# عرض المؤقت
if st.session_state.session_active:
    current_time = time.time()
    elapsed_time = current_time - st.session_state.start_time

    if not st.session_state.is_break:
        remaining_time = work_time - elapsed_time
        if remaining_time > 0:
            mins, secs = divmod(int(remaining_time), 60)
            st.subheader(f"Work Time Remaining: {mins:02d}:{secs:02d}")
            time.sleep(1)
            st.rerun()

        else:
            st.success(random.choice(motivational_quotes))
            st.session_state.is_break = True
            st.session_state.start_time = time.time()
            time.sleep(5)
            st.rerun()
    else:
        remaining_time = break_time - elapsed_time
        if remaining_time > 0:
            mins, secs = divmod(int(remaining_time), 60)
            st.subheader(f"Break Time Remaining: {mins:02d}:{secs:02d}")
            time.sleep(1)
            st.rerun()
        else:
            st.success("Break is over! Ready for another session?")
            st.session_state.session_active = False
