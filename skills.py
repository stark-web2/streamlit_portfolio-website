import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💡")

st.title("💡 Skills Dashboard")

# ===== PROGRAMMING =====
st.subheader("💻 Programming Skills")

st.write("Python")
st.progress(85)

st.write("JavaScript")
st.progress(70)

st.write("PHP")
st.progress(75)

st.write("HTML/CSS")
st.progress(90)

st.divider()

# ===== DESIGN =====
st.subheader("🎨 Design Skills")

st.write("UI/UX Design")
st.progress(80)

st.write("Canva")
st.progress(90)

st.divider()

# ===== TOOLS =====
st.subheader("🛠 Tools")
st.success("""
✔ GitHub  
✔ VS Code  
✔ Streamlit    
""")