import streamlit as st

def main():
    st.title("Simple Streamlit Web App")
    st.write("Welcome to your first Streamlit app!")
    
    # Input from user
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")
    
    # Number input
    number = st.number_input("Pick a number", min_value=1, max_value=100, step=1)
    st.write(f"You selected: {number}")
    
    # Button example
    if st.button("Click Me"):
        st.write("Button clicked!")
    
    # Checkbox
    agree = st.checkbox("I agree")
    if agree:
        st.write("Thanks for agreeing!")
    
    # Sidebar
    st.sidebar.header("Sidebar Menu")
    choice = st.sidebar.selectbox("Choose an option", ["Home", "About", "Contact"])
    st.sidebar.write(f"You selected: {choice}")
    
if __name__ == "__main__":
    main()
