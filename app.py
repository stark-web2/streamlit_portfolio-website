import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🔥",
    layout="wide"
)

# ===== HERO SECTION =====
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🔥 Welcome to My Portfolio")
    st.subheader("Crystal M. Bangalisan")
    st.write("💻 Aspiring Full Stack Developer | Tech Enthusiast | UI/UX Learner")

    st.write("""
Explore my digital portfolio where I showcase my skills, projects, and journey in web development.
Use the navigation menu to discover more about me.
""")

    st.success("🚀 Multipage Streamlit App is running!")

# ===== IMAGE FIX =====
img_path = Path("assets/my_picture.png")

with col2:
    if img_path.is_file():
        st.image(str(img_path), caption="My Portfolio Preview")
    else:
        st.warning("⚠ Image not found! Check 'assets/my_picture.png'")

st.divider()

# ===== FEATURES SECTION =====
st.subheader("✨ What You’ll Find Here")

colA, colB, colC = st.columns(3)

with colA:
    st.info("🏠 Home\nOverview of who I am")

with colB:
    st.info("💡 Skills\nMy technical abilities")

with colC:
    st.info("💼 Projects\nMy real work and systems")

colD, colE = st.columns(2)

with colD:
    st.info("🧑‍💻 About\nMy background and goals")

with colE:
    st.info("📞 Contact\nGet in touch with me")

st.divider()

# ===== CTA SECTION =====
st.subheader("🚀 Ready to Explore?")

if st.button("Start Exploring"):
    st.balloons()
    st.success("Use the sidebar to navigate your portfolio!")