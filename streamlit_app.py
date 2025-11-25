import streamlit as st
import random

# Game settings
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# Generate secret code on new game
if "secret_code" not in st.session_state:
    st.session_state.secret_code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    st.session_state.history = []

st.title("🎯 Mastermind Game")
st.write("Guess the secret combination of 4 colors (R, G, B, Y, W, O)")

# User guess input
guess = st.text_input("Enter your guess (e.g. R G B Y):").upper().split()

# Submit guess button
if st.button("Submit Guess"):
    if len(guess) != CODE_LENGTH:
        st.error(f"Guess must contain {CODE_LENGTH} colors.")
    else:
        # Check result
        exact_matches = sum([1 for i in range(CODE_LENGTH) if guess[i] == st.session_state.secret_code[i]])
        color_matches = sum([min(guess.count(c), st.session_state.secret_code.count(c)) for c in COLORS]) - exact_matches
        
        st.session_state.history.append((guess, exact_matches, color_matches))

        if exact_matches == CODE_LENGTH:
            st.success("🎉 Congratulations! You cracked the code!")
        elif len(st.session_state.history) >= TRIES:
            st.error(f"❌ Out of tries! The correct code was: {st.session_state.secret_code}")
        else:
            st.warning(f"Exact Matches: {exact_matches}, Color Matches: {color_matches}")

# Display history
st.subheader("📜 Guess History")
for idx, (g, exact, color) in enumerate(st.session_state.history):
    st.write(f"**Try {idx+1}** — Guess: {g} | Exact: {exact} | Color only: {color}")

# New Game
if st.button("🔄 New Game"):
    st.session_state.secret_code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    st.session_state.history = []
        st.rerun()

