import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter."
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit."
    
    # Check for special characters
    if not any(char in "!@#$%^&*()-_+=<>?/.,:;" for char in password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

# Example usage:
password = input("Enter your password: ")
strength_message = check_password_strength(password)
print(strength_message)
