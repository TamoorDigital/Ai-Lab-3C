# gamemanager.py
import streamlit as st
from logic import FizzBuzz


class GameManager:
    """Manages game state and interactions for the FizzBuzz Quiz."""

    def __init__(self):
        self.fizzbuzz_engine = FizzBuzz()

        # Initialize session state variables
        if 'number' not in st.session_state:
            st.session_state.number = 1
            st.session_state.score = 0
            st.session_state.game_over = False
            st.session_state.history = []

    def get_correct_value(self):
        """Return the correct FizzBuzz value for the current number."""
        return self.fizzbuzz_engine.get_value(st.session_state.number)

    def reset(self):
        """Reset all session state values to start a new game."""
        st.session_state.number = 1
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.history = []
