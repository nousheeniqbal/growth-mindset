import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="⭐")


st.title("Growth Mindset challenge :Web App with Streamlit")

st.header("Welcome to the Growth Mindset Challenge!")
st.write("Embrace challenges, learn mistakes, and unlock your full potentail.this AI-powered app helps you build a growth mindset.")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal. it is the courage to continue that counts.- Winston S. Churchill")

st.header(" What's Your Challenge Today?")
user_input = st.text_area("Describe a challenge you are facing:")

#condition
if user_input:
    st.success(f"you are facing: {user_input}. Keep pushing forward towards your goals!🚀")
else:
    st.warning("Tell us about your challenge to get started.")

    #reflexing
    st.header("Reflect on Your Learning")
    reflection = st.text_area("Write your reflection here:")

    if reflection:
        st.success(f"Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

        #achievements
        st.header(" 🏆 Celebrate Your Achievements")
        achievements = st.text_input("Share something you have recently accomplished:")

        if achievements:
            st.success(f"🎉 Great job! Your achieved: {achievements}")
        else:
            st.info("Celebrate your wins, no matter how small! Share one now.😍")

            #footer
            st.write("- - -")
            st.write("🚀 Keep believeing in yourself. Growth is a journey, not a destination!🌟")
            st.write("⭕ Created by Nousheen Iqbal")
