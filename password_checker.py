import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    messages = []

    if password.lower() in ["password", "123456", "password123", "admin", "qwerty", "letmein"]:
        messages.append("❌ This password is too common.")
        return messages, 0

    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        messages.append("✅ Strong Password!")
    elif score == 3:
        messages.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        messages.append("❌ Weak Password - Improve it using the suggestions above.")

    return messages, score

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and 
            re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password)):
            return password

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter a password", type="password")

if st.button("Check Strength"):
    feedback, score = check_password_strength(password)
    for msg in feedback:
        st.write(msg)

if st.button("Suggest Strong Password"):
    st.success(generate_strong_password())
