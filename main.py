import time
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
        key       = input("Enter key (128 bits)    : ")
        plaintext = input("Enter plaintext         : ").encode()
        print("===============")
        print("Key (hex)        : ", key.encode().hex())
        print("Plaintext (hex)  : ", plaintext.hex())
        print("=====RESULT====")
        
        start_time = time.time()

        # Key expansion
        key_expansion = KeyExpansion(key, 16)
        key_expansion.makeRoundKey()
        
        # Split plaintext into 16 bytes chunks
        plaintext_chunks = split_text(plaintext)
        ciphertext = b''
        
        # P-BOX and S-BOX
        p_box = perm.generatePBox(key, 128)
        s_box = sub.generateSBox(key, 256)

        # Encrypt each chunk
        i = 0
        for plaintext in plaintext_chunks:
            
            # Permutation 
            plaintext = perm.permute(plaintext, p_box)
            
            # Round function
            round_function = RoundFunction(plaintext, key_expansion.roundKey, 16, 1)
            round_function.encrypt()
            ciphertext_chunks = round_function.ciphertext
            
            # Substitution
            ciphertext_chunks = sub.substitute(ciphertext_chunks, s_box)
            
            ciphertext += ciphertext_chunks
            print("Cipherblock", i, "   : ",  ciphertext_chunks)
            i += 1
        stop_time = time.time()
        print("Ciphertext (hex) : ", ciphertext.hex())
        print("Ciphertext       : ", ciphertext.decode('IBM866'))
        print("Time             : ", stop_time - start_time, "seconds")
        print("===============")

    elif choice == 2:
        key        = input("Enter key (128 bits)    : ")
        ciphertext = input("Enter ciphertext (hex)  : ")
        print("===============")
        print("Key (hex)        : ", key.encode().hex())
        print("Ciphertext (hex) : ", ciphertext)
        print("=====RESULT====")
        
        start_time = time.time()

        # Key expansion
        key_expansion = KeyExpansion(key, 16)
        key_expansion.makeRoundKey()
        
        # Split ciphertext into 16 bytes chunks
        ciphertext_chunks = split_text(bytes.fromhex(ciphertext))
        plaintext = b''

        # P-BOX and S-BOX
        p_box = perm.generatePBox(key, 128)
        s_box = sub.generateSBox(key, 256)
        
        # Decrypt each chunk
        i = 0
        for ciphertext in ciphertext_chunks:
            
            # Reverse Substitution
            ciphertext = sub.reverse(ciphertext, s_box)
            
            # Round function
            round_function = RoundFunction(ciphertext, key_expansion.roundKey, 16, 0)
            round_function.decrypt()
            plaintext_chunks = round_function.plaintext
            
            # Reverse Permutation
            plaintext_chunks = perm.netralize(plaintext_chunks, p_box)

            plaintext += plaintext_chunks
            print("Plainblock", i, "    : ",  plaintext_chunks)
            i += 1
        stop_time = time.time()
        print("Plaintext(hex)   : ", plaintext.hex())
        print("Plaintext        : ", plaintext.decode('IBM866'))
        print("Time             : ", stop_time - start_time, "seconds")
        print("===============")

    elif choice == 3:
        break

    else:
        print("Invalid choice")
        print("===============")

    print("\n\n")

