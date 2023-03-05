from RoundFunction import RoundFunction
from KeyExpansion import KeyExpansion
import Permutation as perm
import Substitution as sub


def split_text(plaintext):
    # Split plaintext into 16 bytes chunks
    chunks = []
    for i in range(0, len(plaintext), 16):
        chunks.append(plaintext[i:i+16].ljust(16, b'\x00'))
    return chunks

while True:
    print("Go-Block-Cipher")
    print("===============")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("===============")
    choice = int(input("Choose : "))
    print("===============")

    if choice == 1:
        key = input("Enter key (128 bits) : ")
        plaintext = input("Enter plaintext : ").encode()
        print("===============")
        print("Key : ", key.encode().hex())
        print("Plaintext : ", plaintext.hex())
        print("===============")
        
        # Key expansion
        key_expansion = KeyExpansion(key, 16)
        key_expansion.makeRoundKey()
        
        # Split plaintext into 16 bytes chunks
        plaintext_chunks = split_text(plaintext)
        ciphertext = b''
        
        # Encrypt each chunk
        for plaintext in plaintext_chunks:
            
            # Permutation / Substitution 
            # TODO: call permutation and substitution functions
            
            # Round function
            round_function = RoundFunction(plaintext, key_expansion.roundKey, 16, 1)
            round_function.encrypt()
            ciphertext_chunks = round_function.ciphertext
            
            # Permutation / Substitution
            # TODO: call permutation and substitution functions
            
            ciphertext += ciphertext_chunks
            print("Cipherblock : ", ciphertext_chunks)
        print("===============")
        print("Ciphertext (hex): ", ciphertext.hex())
        print("Ciphertext : ", ciphertext.decode('IBM866'))
        print("===============")

    elif choice == 2:
        key = input("Enter key (128 bits) : ")
        ciphertext = input("Enter ciphertext (hex) : ")
        print("===============")
        print("Key : ", key.encode().hex())
        print("Ciphertext : ", ciphertext)
        print("===============")
        
        # Key expansion
        key_expansion = KeyExpansion(key, 16)
        key_expansion.makeRoundKey()
        
        # Split ciphertext into 16 bytes chunks
        ciphertext_chunks = split_text(bytes.fromhex(ciphertext))
        plaintext = b''
        
        # Decrypt each chunk
        for ciphertext in ciphertext_chunks:
            
            # Permutation / Substitution
            # TODO: call permutation and substitution functions
            
            # Round function
            round_function = RoundFunction(ciphertext, key_expansion.roundKey, 16, 0)
            round_function.decrypt()
            
            # Permutation / Substitution
            # TODO: call permutation and substitution functions

            plaintext_chunks = round_function.plaintext
            plaintext += plaintext_chunks
            print("Plainblock : ", plaintext_chunks)
        print("===============")
        print("Plaintext(hex) : ", plaintext.hex())
        print("Plaintext : ", plaintext.decode('IBM866'))
        print("===============")

    elif choice == 3:
        break

    else:
        print("Invalid choice")
        print("===============")

