import re

def password_strength_checker(password):
    # Initialize strength criteria
    criteria = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digits": False,
        "special_chars": False
    }
    
    # Check password length
    if len(password) >= 8:
        criteria["length"] = True
    
    # Check for uppercase, lowercase, digits, and special characters using regex
    if re.search(r'[A-Z]', password):
        criteria["uppercase"] = True
    if re.search(r'[a-z]', password):
        criteria["lowercase"] = True
    if re.search(r'[0-9]', password):
        criteria["digits"] = True
    if re.search(r'[@$!%*?&]', password):
        criteria["special_chars"] = True
    
    # Evaluate the strength
    strength = sum(criteria.values())
    
    # Determine feedback
    feedback = []
    if not criteria["length"]:
        feedback.append("Your password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Your password should include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Your password should include at least one lowercase letter.")
    if not criteria["digits"]:
        feedback.append("Your password should include at least one digit.")
    if not criteria["special_chars"]:
        feedback.append("Your password should include at least one special character (@$!%*?&).")
    
    # Strength feedback
    if strength == 5:
        return "Strong Password!", feedback
    elif strength >= 3:
        return "Moderate Password!", feedback
    else:
        return "Weak Password!", feedback

# Test the function
password = input("Enter a password to check: ")
strength, suggestions = password_strength_checker(password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")