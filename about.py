
import streamlit as st

st.set_page_config(page_title="About", page_icon="🧑‍💻")

st.title("🧑‍💻 About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/my_picture.png", width=150)

with col2:
    st.info("""
I am a passionate developer who enjoys building systems, websites, and solving real-world problems using technology.
    """)

st.divider()

# ===== EDUCATION =====
st.subheader("🎓 Education")
st.write("""
- BS Computer Science  
- Training in Web Development  
- UI/UX Design Basics  
""")

# ===== GOALS =====
st.subheader("🎯 Goals")
st.success("""
- Become a Full Stack Developer  
- Build real-world systems  
- Improve UI/UX skills  
- Work on impactful projects  
""")

# ===== PERSONAL INFO =====
st.subheader("📌 Quick Info")
st.write("📍 Location: Philippines")
st.write("💼 Role: Student Developer")
st.write("⚡ Focus: Web Development")