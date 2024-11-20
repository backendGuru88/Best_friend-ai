


import streamlit as st

st.title(":mailbox: Feedback Form!")
st.write("Help Us Improve Motivo AI! We value your thoughts and insights! Your feedback is essential in shaping Motivo AI into the most supportive and efficient companion for tracking your progress and enhancing your well-being. Whether it's a suggestion, a feature request, or sharing your experience, we want to hear from you. Please take a moment to fill out this feedback form and help us continue delivering a product that meets your needs. Your input drives innovation and ensures that Motivo AI remains your trusted ally in staying motivated and achieving your goals. Thank you for helping us grow and improve! 😊")
# st.write("Thank you for using our Fake News Detector! We greatly appreciate your feedback as it helps us enhance our service and combat misinformation more effectively. Please take a moment to fill out the form below and share your thoughts with us. Your input is invaluable in our mission to create a more informed online community.")
st.write("---")



feedback_form = """
<form action="https://formspree.io/f/xbljkazw" method="POST">
<input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here!"></textarea>
    <button type="submit">Send</button>
</form>

"""


st.markdown(feedback_form, unsafe_allow_html=True)

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")
