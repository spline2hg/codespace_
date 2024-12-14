import string
import itertools
import hashlib

def generate_rot_mapping(orig_chars, rotated_chars):
    return str.maketrans(orig_chars, rotated_chars)

def check_credentials(username, password):
    # Character substitution mappings
    c1 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    n1 = [5,6,7,8,9,0,1,2,3,4]
    n2 = "0123456789"

    # Target hash from the original JavaScript code
    target_hash = bytes([9,87,39,96,151,202,140,186,120,235,167,229,47,231,6,212,77,205,58,14,248,104,169,79,116,140,236,98,126,26,100,120])

    # Prisoners list from the HTML
    prisoners = [
        "Aurion Flux", "Zyra Talon", "Kryon Vale", 
        "Vex Drakon", "Nyx Solaris", "Lazari Void", 
        "Kael Xypher", "Cypher Lux", "Dax Zenith", 
        "Lyra Quasar"
    ]

    # Generate possible usernames (first names)
    possible_usernames = [p.split()[0] for p in prisoners]

    # Function to apply transformations similar to JS code
    def apply_transformations(username, password):
        # Attempt to mimic the complex JS transformations
        # This is a simplified approximation
        username_trans = ''.join([
            c1[c2.index(c)] if c in c2 else c 
            for c in username
        ])
        
        password_trans = ''.join([
            c1[c2.index(c)] if c in c2 else c 
            for c in password
        ])

        return username_trans, password_trans

    # Brute force approach
    for username in possible_usernames:
        for password_length in range(4, 10):  # Reasonable password length
            for password_chars in itertools.product(string.ascii_letters + string.digits, repeat=password_length):
                password = ''.join(password_chars)
                
                try:
                    # Hash the password using SHA-256
                    password_bytes = password.encode('utf-8')
                    password_hash = hashlib.sha256(password_bytes).digest()
                    
                    # Check if hash matches target
                    if password_hash == bytes(target_hash):
                        print(f"Found match!")
                        print(f"Username: {username}")
                        print(f"Password: {password}")
                        return username, password
                
                except Exception as e:
                    print(f"Error processing {username}:{password} - {e}")
    
    return None, None

def main():
    username, password = check_credentials(None, None)
    if username and password:
        print("Credentials found!")
    else:
        print("No matching credentials found.")

if __name__ == "__main__":
    main()