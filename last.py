# # import hashlib
# # import base64
# # import binascii

# # def custom_reduce(funcs, inputs, initial):
# #     result = initial
# #     for func, inp in zip(funcs, inputs):
# #         result = func(result, inp)
# #     return result

# # def custom_transformations(input_str):
# #     c1 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
# #     c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# #     n1 = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
# #     n2 = "0123456789"

# #     transformations = [
# #         # Various string transformations
# #         lambda s: s.split(c)[0],
# #         lambda s: ''.join([c1[c2.index(ch)] if ch in c2 else ch for ch in s]),
# #         lambda s: s[0:4],
# #         lambda s: s.encode('utf-8').hex(),
# #         lambda s: s.replace('-', ''),
# #     ]

# #     for transform in transformations:
# #         input_str = transform(input_str)
    
# #     return input_str

# # def check_credentials(username, password):
# #     # Actual decryption logic from the challenge
# #     challenges = [
# #         [lambda x: x.split(), len],
# #         [lambda x: [(-1 if ch in ['n','q','z','v','a'] else ch) for ch in x], lambda x: x],
# #         [lambda x: x[0:4], len],
# #         [lambda x: x.encode('utf-8'), ord],
# #     ]

# #     # Perform custom reduce operations
# #     for challenge in challenges:
# #         try:
# #             result = custom_reduce(challenge[0], challenge[1:], password)
# #             if not result:
# #                 return False
# #         except:
# #             return False

# #     # SHA-256 verification
# #     password_hash = hashlib.sha256(password.encode()).digest()
# #     expected_hash = bytes([9,87,39,96,151,202,140,186,120,235,167,229,47,231,6,212,77,205,58,14,248,104,169,79,116,140,236,98,126,26,100,120])
    
# #     return password_hash == expected_hash

# # def main():
# #     # Decode username and password using custom transformations
# #     username = custom_transformations("Aurion Flux")
# #     password = custom_transformations("1")

# #     if check_credentials(username, password):
# #         print("Credentials Verified!")
# #         # Add flag retrieval logic here
# #     else:
# #         print("Access Denied")

# # if __name__ == "__main__":
# #     main()





# import hashlib
# import itertools
# import string

# def generate_passwords():
#     # Base characters for generating passwords
#     chars = string.ascii_letters + string.digits + '!@#$%^&*()_+'
    
#     # Generate sequential and pattern-based passwords
#     password_patterns = [
#         # Specific pattern passwords
#         "ncrnt{CellM@nagerAccess%d}",
#         "SpacePrison%d!",
#         "Access%dControl!",
#         "Prison2024%d!",
        
#         # More complex patterns
#         "Warden%d2024!",
#         "Guard%dAccess!",
#         "Security%dCode!",
#     ]
    
#     # Sequential number ranges to try
#     number_ranges = [
#         range(0, 100),
#         range(2020, 2025),
#         range(1, 10),
#         range(100, 1000)
#     ]
    
#     for pattern in password_patterns:
#         for num_range in number_ranges:
#             for num in num_range:
#                 yield pattern % num

# def decrypt_credentials():
#     # Prisoner names from the HTML
#     usernames = [
#         # Full names
#         "Aurion Flux",
#         "Zyra Talon", 
#         "Kryon Vale", 
#         "Vex Drakon", 
#         "Nyx Solaris", 
#         "Lazari Void", 
#         "Kael Xypher", 
#         "Cypher Lux", 
#         "Dax Zenith", 
#         "Lyra Quasar",
        
#         # First names
#         "Aurion", "Zyra", "Kryon", "Vex", "Nyx", 
#         "Lazari", "Kael", "Cypher", "Dax", "Lyra",
        
#         # Last names
#         "Flux", "Talon", "Vale", "Drakon", "Solaris", 
#         "Void", "Xypher", "Lux", "Zenith", "Quasar",
        
#         # Variations
#         "Warden", "Guard", "Admin", "SpacePrison"
#     ]

#     # Expected SHA-256 hash
#     expected_hash = bytes([9,87,39,96,151,202,140,186,120,235,167,229,47,231,6,212,77,205,58,14,248,104,169,79,116,140,236,98,126,26,100,120])

#     # Iterate through usernames and passwords
#     for username in usernames:
#         for password in generate_passwords():
#             try:
#                 # Compute SHA-256 hash of the password
#                 password_hash = hashlib.sha256(password.encode()).digest()
                
#                 # Check if hash matches
#                 if password_hash == expected_hash:
#                     print("Credentials Found:")
#                     print(f"Username: {username}")
#                     print(f"Password: {password}")
#                     return username, password
#             except Exception as e:
#                 # Skip any encoding errors
#                 continue

#     print("No valid credentials found.")
#     return None

# def main():
#     decrypt_credentials()

# if __name__ == "__main__":
#     main()




import hashlib
import itertools

def custom_transform(username, access_code):
    c1 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    n1 = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
    n2 = "0123456789"

    # Combine username and access code for transformation
    combined = username + access_code

    # Perform transformations similar to original JS code
    def transform_step(s):
        # Character substitution
        s = ''.join([c1[c2.index(ch)] if ch in c2 else ch for ch in s])
        
        # Slice and modify
        s = s[:4]
        
        # Additional transformations
        s = s.encode('utf-8').hex()
        s = s.replace('-', '')
        
        return s

    return transform_step(combined)

def decrypt_credentials():
    # Full prisoner names from the HTML
    usernames = [
        "Aurion Flux", "Zyra Talon", "Kryon Vale", "Vex Drakon", 
        "Nyx Solaris", "Lazari Void", "Kael Xypher", "Cypher Lux", 
        "Dax Zenith", "Lyra Quasar"
    ]

    # Expected SHA-256 hash
    expected_hash = bytes([9,87,39,96,151,202,140,186,120,235,167,229,47,231,6,212,77,205,58,14,248,104,169,79,116,140,236,98,126,26,100,120])

    # Try access codes from 1 to 1000
    for access_code in range(1, 1001):
        for username in usernames:
            try:
                # Convert access code to string
                access_code_str = str(access_code)
                
                # Apply transformations
                transformed = custom_transform(username, access_code_str)
                
                # Compute SHA-256 hash of the transformed string
                password_hash = hashlib.sha256(transformed.encode()).digest()
                
                # Check if hash matches
                if password_hash == expected_hash:
                    print("Credentials Found:")
                    print(f"Username: {username}")
                    print(f"Access Code: {access_code_str}")
                    print(f"Transformed: {transformed}")
                    return username, access_code_str
            except Exception as e:
                # Skip any errors
                continue

    print("No valid credentials found.")
    return None

def main():
    decrypt_credentials()

if __name__ == "__main__":
    main()