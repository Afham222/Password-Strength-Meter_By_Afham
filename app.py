import streamlit as st
import re

def calculate_password_score(password):
    """
    Evaluates the strength of a given password based on predefined security rules.
    Returns a score (1-5) and suggestions to improve the password.
    """
    score = 0
    suggestions = []
    
    # Checking minimum length requirement
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters.")
    
    # Checking for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")
    
    # Checking for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")
    
    # Checking for digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit (0-9).")
    
    # Checking for special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")
    
    return score, suggestions

def main():
    """
    Streamlit app that allows users to enter a password and evaluates its strength.
    Provides real-time feedback and suggestions for improvement.
    """
    st.title("🔒 Password Strength Meter - Project 02")
    
    # Display password strength criteria for user guidance
    st.markdown("""
    *Password Strength Criteria:*
    - 🔹 At least *8 characters long*
    - 🔹 Contains *uppercase & lowercase letters*
    - 🔹 Includes at least *one digit (0-9)*
    - 🔹 Has at least *one special character (!@#$%^&)**
    """)
    
    # User input for password
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, suggestions = calculate_password_score(password)
        
        # Display progress bar to indicate password strength visually
        st.progress(score * 20)
        
        # Categorize password strength and display appropriate message
        if score <= 2:
            strength = "Weak"
            st.error(f"⚠ Password Strength: {strength} (Score: {score}/5)")
        elif score <= 4:
            strength = "Moderate"
            st.warning(f"⚠ Password Strength: {strength} (Score: {score}/5)")
        else:
            strength = "Strong"
            st.success(f"✅ Password Strength: {strength} (Score: {score}/5)")
        
        # Provide feedback if password needs improvement
        if suggestions:
            st.subheader("🔍 Suggestions to improve your password:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
    
    # Additional tip for users
    st.markdown("""
    💡 *Tip:* Use a mix of uppercase, lowercase, numbers, and special characters for a secure password!
    """)

if _name_ == "_main_":
    main()