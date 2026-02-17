import re
import hashlib

password = input("Enter password: ")

# Strength check
length = len(password) >= 8
upper = re.search(r"[A-Z]", password)
lower = re.search(r"[a-z]", password)
digit = re.search(r"[0-9]", password)
special = re.search(r"[!@#$%^&*()]", password)

score = sum([bool(length), bool(upper), bool(lower), bool(digit), bool(special)])

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Moderate"
else:
    strength = "Strong"

# Hashing
hashed = hashlib.sha256(password.encode()).hexdigest()

print("\nPassword Strength:", strength)
print("SHA-256 Hash:", hashed)
