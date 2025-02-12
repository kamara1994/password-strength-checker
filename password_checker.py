import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase, lowercase, numbers, and symbols
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[\W_]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Output result
    if strength_score == 6:
        return "Strong password ✅", []
    elif strength_score >= 4:
        return "Moderate password ⚠️", feedback
    else:
        return "Weak password ❌", feedback

# Run the program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result, suggestions = check_password_strength(password)
    print(f"\nPassword Strength: {result}")
    if suggestions:
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
