import random
import streamlit as st
from number_selection import grid_options

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
load_css("style.css")


def main():
    st.title('Guess Game')
    st.write('I am thinking of a number between 1 and 30.  \nCan you guess it in less than 5 attempts??')
    
    if "guess_limit" not in st.session_state:
        st.session_state.random_number = random.randint(1, 30)
        st.session_state.guess_counter = 0
        st.session_state.guess_limit = 5
        st.session_state.message = ""
        
    guess = grid_options()

    if st.button('Submit Guess'):
        if guess is not None:
            st.session_state.guess_counter+=1

            # if guess not in range(1,30):
            #     st.session_state.message = 'Value entered is not in range. Enter correct value.'
            #     st.session_state.message = 'GAME OVER!!! Try Again'

            if guess == st.session_state.random_number:
                st.session_state.message = 'Congratulations!! You guessed correctly!!'
                st.session_state.guess_counter = st.session_state.guess_limit       # We are forcefully ending the game after player wins
            
            elif guess < st.session_state.random_number:
                st.session_state.message = 'Too Low!. Guess higher'
            
            elif guess > st.session_state.random_number:
                st.session_state.message = 'Too High!. Guess lower'
            
            if st.session_state.guess_counter > st.session_state.guess_limit: 
                st.session_state.message = f'Sorry. You are out of {st.session_state.guess_limit} attempts.  \nThe number was {st.session_state.random_number}. Try again next time'
        
            st.write(st.session_state.message)

if __name__ == '__main__':
    main()