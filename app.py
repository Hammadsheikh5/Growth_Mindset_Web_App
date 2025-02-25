import streamlit as st
import datetime

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")
    
    st.title("🚀 Growth Mindset Challenge")
    st.subheader("Develop Your Abilities Through Hard Work and Learning")
    
    st.write("""
    A growth mindset is the belief that intelligence and abilities can be developed through effort, learning, and persistence.
    This project helps you track your progress in adopting a growth mindset.
    """)
    
    st.divider()
    
    st.header("📌 Set Your Learning Goals")
    goal = st.text_area("What is your learning goal for this week?")
    deadline = st.date_input("Deadline for this goal:", datetime.date.today())
    if st.button("Save Goal"):
        st.success(f"Goal saved: {goal} (Deadline: {deadline})")
    
    st.divider()
    
    st.header("📈 Track Your Progress")
    progress = st.slider("How confident do you feel about your progress?", 0, 100, 50)
    st.write(f"Current progress: {progress}%")
    
    if st.button("Submit Progress"):
        if progress == 100:
            st.balloons()
            st.success("🎉 Congratulations! You've reached 100% progress!")
        else:
            st.info("Keep going! You're making progress.")
    
    st.divider()
    
    st.header("📝 Daily Reflection")
    reflection = st.text_area("Write about your learning experience today:")
    if st.button("Save Reflection"):
        st.success("Reflection saved successfully!")
    
    st.divider()
    
if __name__ == "__main__":
    main()