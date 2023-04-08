import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""
    
    # Combine all possible characters based on the user's preferences
    all_chars = lowercase + uppercase + numbers + symbols
    
    # Ensure the length of the password is at least 8 characters
    length = max(length, 8)
    
    # Generate the password
    password = "".join(random.choices(all_chars, k=length))
    
    return password

# Streamlit app
def app():
    st.title("Password Generator")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://preview.redd.it/3nb9h6xi0lx61.png?auto=webp&s=79a7a919428bad201cb8785dd8cceb935d3a4791");
             background-attachment: fixed;
             background-color: transparent;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
  
    # Get user preferences
    length = st.slider("Length", min_value=8, max_value=32, value=12)
    include_uppercase = st.checkbox("Include uppercase letters")
    include_numbers = st.checkbox("Include numbers")
    include_symbols = st.checkbox("Include symbols")
    
    # Generate and display the password
    if st.button("Generate"):
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        st.success(f"Your password is: {password}")

if __name__ == "__main__":
    app()
