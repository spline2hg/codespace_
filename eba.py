encodings = ['utf-8', 'iso-8859-1', 'utf-16', 'windows-1252']

with open('logfile.txt', 'rb') as file:
    file_content = file.read()

for encoding in encodings:
    try:
        decoded_data = file_content.decode(encoding)
        print(f"Decoded with {encoding}:")
        print(decoded_data)
        break  # Exit if you find a readable encoding
    except UnicodeDecodeError:
        print(f"Failed to decode with {encoding}")
