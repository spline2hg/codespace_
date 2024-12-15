import hashlib
from itertools import product

def generate_access_code(cell_names):
    """
    Generate an access code by skipping numbers for "Empty" cells.
    """
    access_code = []
    number = 1
    for name in cell_names:
        if name == "Empty":
            number += 1  # Skip a number for "Empty"
        else:
            access_code.append(str(number))
            number += 1
    return ''.join(access_code)

def hash_code(code):
    """
    Simulate the hashing process to match the expected hash.
    """
    encoded_code = code.encode('utf-8')
    return hashlib.sha256(encoded_code).digest()

def main():
    cell_names = [
        "Aurion Flux", "Zyra Talon", "Kryon Vale", "Vex Drakon",
        "Nyx Solaris", "Lazari Void", "Empty", "Kael Xypher",
        "Cypher Lux", "Empty", "Dax Zenith", "Lyra Quasar"
    ]

    # Generate the access code
    access_code = generate_access_code(cell_names)
    print("Generated Access Code:", access_code)

    # Expected hash from the JavaScript
    expected_hash = bytes([
        9, 87, 39, 96, 151, 202, 140, 186, 120, 235, 167, 229,
        47, 231, 6, 212, 77, 205, 58, 14, 248, 104, 169, 79,
        116, 140, 236, 98, 126, 26, 100, 120
    ])

    # Brute force or verify the hash
    hashed_code = hash_code(access_code)
    if hashed_code == expected_hash:
        print(f"Success! Access Code is: {access_code}")
    else:
        print("Failed to match the expected hash.")

if __name__ == "__main__":
    main()
