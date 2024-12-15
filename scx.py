import hashlib

# Hardcoded hash value from the script
target_hash = bytes([9, 87, 39, 96, 151, 202, 140, 186, 120, 235, 167, 229, 47, 231, 6, 212, 
                     77, 205, 58, 14, 248, 104, 169, 79, 116, 140, 236, 98, 126, 26, 100, 120])

# Character set to try (can be optimized based on observations)
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Brute-force length (based on typical access code patterns)
max_length = 8

def generate_hash(input_code):
    # Hash using SHA-256
    return hashlib.sha256(input_code.encode()).digest()

def brute_force():
    from itertools import product
    for length in range(1, max_length + 1):
        for attempt in product(charset, repeat=length):
            code = ''.join(attempt)
            if generate_hash(code) == target_hash:
                return code
    return None

if __name__ == "__main__":
    access_code = brute_force()
    if access_code:
        print(f"Access Code Found: {access_code}")
    else:
        print("Access Code Not Found.")
