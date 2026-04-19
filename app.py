import streamlit as st
import random

# Initialize session state so the number doesn't change every time you click a button
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("🤖 AI Number Guesser")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# User Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    distance = abs(st.session_state.secret_number - guess)
    
    if guess == st.session_state.secret_number:
        st.balloons()
        st.success(f"Target Acquired! It took you {st.session_state.attempts} tries.")
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
    else:
        # Feedback Logic
        if distance <= 5:
            st.error("🔥 AI: You're burning up!")
        elif distance <= 15:
            st.warning("🌡️ AI: You're getting warm.")
        else:
            st.info("❄️ AI: You're ice cold.")
            
        if guess < st.session_state.secret_number:
            st.write("📈 Aim Higher!")
        else:
            st.write("📉 Aim Lower!")