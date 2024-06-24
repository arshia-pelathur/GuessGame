import streamlit as st


def grid_options():
    if 'selected_number' not in st.session_state:
        st.session_state.selected_number = None

    st.title('Choose your Guess')

    options = list(range(1, 31))     # Options for the numbers
    num_columns = 10     # Number of columns you want in your grid

    # Create the grid layout
    columns = st.columns(num_columns)

    for i, number in enumerate(options):     # Loop through the options and create a button for each number in the grid
        col = columns[i % num_columns]
        if col.button(str(number)):
            st.session_state.selected_number = number

    return st.session_state.selected_number
