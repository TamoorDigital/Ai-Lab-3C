# app.py
import streamlit as st
import random
from logic import FizzBuzz
from gamemanager import GameManager

# Application title and description
st.title("FizzBuzz Quiz Game")
st.write("Select the correct answer for each number below.")

# Initialize game components
game_controller = GameManager()
fizzbuzz_engine = FizzBuzz()

# Main game logic
if not st.session_state.game_over:
    current_number = st.session_state.number
    correct_output = fizzbuzz_engine.get_value(current_number)

    # Maintain same options until number changes
    if "choices" not in st.session_state or st.session_state.last_number != current_number:
        answer_choices = [correct_output]
        while len(answer_choices) < 3:
            random_choice = random.choice(["Fizz", "Buzz", "Fizz Buzz", str(random.randint(1, 20))])
            if random_choice not in answer_choices:
                answer_choices.append(random_choice)

        random.shuffle(answer_choices)
        st.session_state.choices = answer_choices
        st.session_state.last_number = current_number

    answer_choices = st.session_state.choices

    st.subheader(f"Number: {current_number}")

    # Display option buttons
    columns = st.columns(len(answer_choices))
    for index, choice in enumerate(answer_choices):
        if columns[index].button(choice, key=f"btn_{current_number}_{index}"):
            if choice == correct_output:
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.history.append((current_number, choice, "Correct"))
                st.session_state.number += 1
                if "choices" in st.session_state:
                    del st.session_state.choices
                st.rerun()
            else:
                st.error(f"Wrong! The correct answer was: {correct_output}")
                st.session_state.history.append((current_number, choice, f"Wrong (Correct: {correct_output})"))
                st.session_state.game_over = True
                st.rerun()

# Display score and history
st.subheader("Game Statistics")
st.write(f"Score: {st.session_state.score}")

if st.session_state.history:
    st.write("History")
    for num, ans, result in st.session_state.history:
        st.write(f"Number {num}: You selected '{ans}' → {result}")

# Restart game option
if st.session_state.game_over:
    if st.button("Restart Game"):
        game_controller.reset()
        if "choices" in st.session_state:
            del st.session_state.choices
        st.rerun()
