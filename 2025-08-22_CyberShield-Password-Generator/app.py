import streamlit as st
import random
import string
import pyperclip

# ---------------------------
# Branding / Title
# ---------------------------
st.set_page_config(page_title="Mubasshir's Password Generator", page_icon="🔑", layout="centered")

st.markdown("<h1 style='text-align: center; color: cyan;'>🔑 Mubasshir's Pro Password Generator</h1>", unsafe_allow_html=True)
st.write("### Generate strong, secure passwords instantly! 🚀")

# ---------------------------
# Password Generation Function
# ---------------------------
def generate_password(length: int) -> str:
    password = []
    if length >= 4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        
        for _ in range(length - 4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
        
        random.shuffle(password)
    else:
        for _ in range(length):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    
    return "".join(password)

# ---------------------------
# Password Strength Checker
# ---------------------------
def check_strength(password: str) -> str:
    if len(password) < 8:
        return "❌ Weak"
    elif any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c in string.punctuation for c in password):
        return "✅ Strong"
    else:
        return "⚠️ Medium"

# ---------------------------
# Streamlit UI
# ---------------------------
st.subheader("⚙️ Settings")
length = st.slider("Select password length:", min_value=4, max_value=32, value=12)

if st.button("Generate Password"):
    password = generate_password(length)
    st.session_state["password"] = password

# Display Generated Password
if "password" in st.session_state:
    st.success("🎉 Your password has been generated!")
    st.code(st.session_state["password"], language="text")

    strength = check_strength(st.session_state["password"])
    st.markdown(f"**Password Strength:** {strength}")

    # Copy Button
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(st.session_state["password"])
        st.info("Password copied to clipboard!")

# ---------------------------
# Footer Branding
# ---------------------------
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: gray;'>🔒 Built with ❤️ by Mubasshir Ahmed</h4>",
    unsafe_allow_html=True
)
