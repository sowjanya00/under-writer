import streamlit as st
from chatbot.intents import handle_user_input
from database.queries import get_user_data, store_user_data
from vector_db.pinecone_client import initialize_pinecone

def main():
    st.title("Gen AI in Insurance Underwriting")
    st.write("Enhancing the Risk Assessment and Policy Personalization")

    # Initialize Pinecone
    initialize_pinecone()

    # User input
    user_input = st.text_input("Ask me anything about insurance underwriting:")

    if st.button("Submit"):
        # Handle user input and get response
        response = handle_user_input(user_input)
        st.write(response)

        # Optionally store user data
        store_user_data(user_input)

        # Retrieve user data for display
        user_data = get_user_data()
        st.write("Previous interactions:", user_data)

if __name__ == "__main__":
    main()