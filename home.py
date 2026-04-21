import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

# ===== HERO SECTION =====
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/my_picture.png", width=180)

with col2:
    st.title("Crystal M. Bangalisan")
    st.subheader("💻 Aspiring Full Stack Developer")
    st.write("Tech Enthusiast | UI/UX Learner | Problem Solver")

st.divider()

# ===== HIGHLIGHTS =====
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "3+")

with col2:
    st.metric("Skills", "6+")

with col3:
    st.metric("Experience Level", "Beginner")

st.divider()

# ===== CTA =====
st.subheader("🚀 Welcome Message")

if st.button("Explore Portfolio"):
    st.success("Use the sidebar to navigate through my work!")

st.balloons()