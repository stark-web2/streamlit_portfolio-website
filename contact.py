import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞")

st.title("📞 Contact Me")

st.write("Feel free to send me a message 👇")

# ===== FORM =====
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit = st.form_submit_button("Send Message")

    if submit:
        if name and email and message:
            st.success("✅ Message sent successfully!")
        else:
            st.error("⚠ Please complete all fields.")

st.divider()

# ===== SOCIAL LINKS =====
st.subheader("🔗 Social Links")
st.write("GitHub: https://github.com/stark-web2")
st.write("Facebook: https://www.facebook.com/crystal.bangalisan")