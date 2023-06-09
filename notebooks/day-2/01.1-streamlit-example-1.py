import streamlit as st


    st.title('String List App')

    # Try to load the list from Streamlit's session state
    # If it doesn't exist, create an empty list
    if 'string_list' not in st.session_state:
        st.session_state.string_list = []

    # Display the input field and the add button
    user_input = st.text_input('Add a string:')
    add_button = st.button('Add string')

    # When the add button is clicked, append the string to the list
    if add_button:
        st.session_state.string_list.append(user_input)
        st.text_input('Add a string:', value='')  # clear the text box

    # Display the current list
    st.subheader('String List')
    for string in st.session_state.string_list:
        st.write(string)


if __name__ == '__main__':
    main()
