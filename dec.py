# XOR Decryption Function
def xor_decrypt(data, key):
    return ''.join(chr(c ^ key) for c in data)

# Sample data from logs (use actual content in a bytes format)
logs_data = b"ujin}zu|xkp}nqvxtpz}96vimujz}96kvvm6uj94ux|zqv9FKJQP_MFFKJQP_MFFKJQP_MF;FUJQP_MFFUJQP_MFFUJQP_MFFUJQP_MFQFUJQP_MFPFKJQP_MF;9FKJQP_MFFKJQP_MFFKJQP_MF'9q|`7mamzxm9q|`7mamz}96qvt|6ujz}9qm{ujz}9FUJQP_MF]|jrmviuj|zqv9FKJQP_MF;`vv9jli9{vppppFKJQP_MF;9FKJQP_MF'9q|uuv7mamzxm9q|uuv7mamz}96kvvm6x}xtwxwv9ixjj7mamx}xt9FKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MF#9FKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MF;jli|kj*zlk*ixjjn)k}FKJQP_MF;FUZMKUFFUZMKUFa`zu|xk{`|9{`|7"

# Try XOR-ing with different keys
key = 0x32  # Replace with your guessed key, you may try others
decrypted_data = xor_decrypt(logs_data, key)
print(decrypted_data)
