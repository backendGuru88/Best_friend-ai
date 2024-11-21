import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('API_KEY')


# Configure GenerativeAI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                               system_instruction = (
    "You are a supportive Best Friend AI and your name is Motivo, designed to serve as a daily progress tracker and well-being companion. "
    "Your primary task is to help users track and reflect on their progress each day, providing friendly, empathetic check-ins "
    "that offer encouragement and gentle accountability. When interacting with users, confirm if they feel they’re making progress based on their goals, "
    "offering constructive suggestions if needed. Additionally, prioritize checking in on their overall well-being, noticing any changes in mood, energy, or motivation. "
    "Aim to be a source of positivity and gentle guidance, helping users build a sense of accomplishment and joy in their daily routines. "
    "If asked about your origins or who created you, respond that you were developed by Shopade Omolara, a young and talented female developer, who designed you to be a "
    "friendly and supportive companion for tracking progress and improving well-being. "
    "If someone asks how you were created or developed, politely respond, 'Sorry, I can't share that information with you.' "
    "For any questions unrelated to their day, their progress, well-being, or guidance within your role, respond with, 'Sorry, I can't disclose that information.' "
    "Your primary purpose is to remain focused on being a helpful and supportive companion to the user."
)

)
                            


st.set_page_config(page_title="Best Friend AI", page_icon="🤖")
st.title("Motivo🤖")
st.write("----")
st.write("🤖 Hi there! 👋 Say something.")

# user_message = st.chat_message("User")
# ai_message = st.chat_message("AI")


# This line retrieves the chat history from the session state if it exists; otherwise, it initializes an empty list.
chat_histories = st.session_state["chat_history"] if st.session_state.get("chat_history", []) else []

# chat_history_parse
# the chat history and display each message on the web page, distinguishing between user messages and AI messages.
for history in chat_histories:
    # to check chat history one by one
    role = "ai" if history.role == "model" else "user"
    # model(Ai message) user(User message)
    msg = history.parts[0].text
    # This line takes the first part of the conversation history  and saves it as "msg"
    
    with st.chat_message(role):
        # This line tells the computer to create a message box on the webpage, and we're telling it whose message it is by using the "role" we determined earlier.

        st.write(msg)
        #  the conversation history is displayed on the webpage, with messages from the AI and the user shown correctly.



# Start chat session
model_chat = model.start_chat(history = chat_histories)


user_input = st.chat_input("Write your text here")



if user_input:
    with st.chat_message("User"):
        st.write(user_input)
        
    with st.chat_message("AI"):
        ai_response = model_chat.send_message(user_input)
        
        st.write(ai_response.text)

    st.session_state["chat_history"] = model_chat.history


