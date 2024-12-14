import hashlib
import itertools

# Target hash from the script
target_hash = bytes([9, 87, 39, 96, 151, 202, 140, 186, 120, 235, 167, 229, 47, 231, 6, 212, 77, 205, 58, 14, 248, 104, 169, 79, 116, 140, 236, 98, 126, 26, 100, 120])

# ROT13 implementation
def rot13(text):
    c1 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(c1[c2.index(c)] if c in c2 else c for c in text)

# Potential guard names
guard_names = [
    "Aurion", "Zyra", "Admin", "Guard1", "Warden", 
    "Kryon", "Vex", "Nyx", "Lazari", "Kael"
]

# Brute force Access Codes
for guard_name in guard_names:
    for access_code in map(''.join, itertools.product("0123456789", repeat=6)):  # 6-digit codes
        # Transform Guard Name and Access Code
        transformed_guard = rot13(guard_name)
        transformed_code = rot13(access_code)
        combined_data = transformed_guard + transformed_code

        # Hash the combined string
        hashed = hashlib.sha256(combined_data.encode()).digest()

        # Check if it matches the target hash
        if hashed == target_hash:
            print(f"Match found! Guard Name: {guard_name}, Access Code: {access_code}")
            exit()
