ENCRYPT = 1
DECRYPT = 0


class RoundFunction():

    def __init__(self, text, key, rounds, mode):
        self.plaintext = bytes(text, 'utf-8') if mode else None
        self.ciphertext = None if mode else bytes(text, 'utf-8')
        self.keyspace = key
        self.key = None
        self.rounds = rounds
        self.mode = mode


    def encrypt(self):
        cipher = self.plaintext
        for i in range(self.rounds):
            self.key = self.keyspace[i+1]
            cipher = self.feistel_round()
        self.ciphertext = cipher


    def decrypt(self):
        plaintext = self.ciphertext
        for i in range(self.rounds):
            self.key = self.keyspace[self.rounds-i]
            plaintext = self.feistel_round()
        self.plaintext = plaintext


    def feistel_round(self):
        if self.mode:
            left_plain = self.plaintext[:len(self.plaintext)//2]
            right_plain = self.plaintext[len(self.plaintext)//2:]
            cipher = right_plain + (self.round_function_enc(right_plain, self.key) ^ left_plain)
            return cipher
        else:
            left_cipher = self.ciphertext[:len(self.ciphertext)//2]
            right_cipher = self.ciphertext[len(self.ciphertext)//2:]
            plain = left_cipher + (self.round_function_dec(left_cipher, self.key) ^ right_cipher)
            return plain


    def round_function_enc(self):
        # permutation (switch odd and even bits)
        cipher = self.switch_bits(self.plaintext)
        # expansion (expand 64 bits to 128 bits)
        cipher = self.expand_bits(cipher)
        # xor with key
        cipher = cipher ^ self.key
        # substitution (s-box)
        cipher = self.substitution(cipher)
        # permutation
        cipher = self.permutation(cipher)
        return cipher


    def round_function_dec(self):
        # inverse permutation
        plain = self.inverse_permutation(self.ciphertext)
        # inverse substitution (s-box)
        plain = self.inverse_substitution(plain)
        # xor with key
        plain = plain ^ self.key
        # inverse expansion (expand 64 bits to 128 bits)
        plain = self.compress_bits(plain)
        # inverse permutation (switch odd and even bits)
        plain = self.switch_bits(plain)
        return plain


    def switch_bits(input):
        # switch odd and even bit pairs
        even_pair = input & 0xCCCCCCCCCCCCCCCC
        odd_pair  = input & 0x3333333333333333
        return (even_pair >> 1) | (odd_pair << 1)


    def expand_bits(self, input):
        # expand 64 bits to 128 bits by XORing adjacent 4-bit chunks and put it between them
        expanded = b''
        input_int = int.from_bytes(input, byteorder='big')
        for i in range(0, input_int.bit_length(), 4):
            chunk1 = (input_int >> i) & 0b1111
            chunk2 = (input_int >> (i-4)%64) & 0b1111
            subtext1 = chunk1
            subtext2 = chunk1 ^ chunk2
            # print("1: ",chunk1, "   | 2: ",chunk2, "   | 3: ",subtext1, "   | 4: ",subtext2)
            expanded += int.to_bytes((subtext1 << 4) + subtext2, 1, byteorder='big')
        expanded = expanded[::-1]
        return expanded
    

    def compress_bits(self, input):
        # compress 128 bits to 64 bits by only taking the first 4 bits of each 8-bit chunk
        compressed = b''
        input_int = int.from_bytes(input, byteorder='big')
        for i in range(0, input_int.bit_length(), 16):
            chunk1 = (input_int >> (i+4)%128) & 0b1111
            chunk2 = (input_int >> (i+12)%128) & 0b1111
            # print("1: ",chunk1, "   | 2: ",chunk2)
            compressed += int.to_bytes((chunk2 << 4) + chunk1, 1, byteorder='big')
        compressed = compressed[::-1]
        return compressed
    

    def substitution(self, input):
        pass


    def inverse_substitution(self, input):
        pass
            
    
    def permutation(self, input):
        pass


    def inverse_permutation(self, input):
        pass



"""
TESTING
"""
roundfunction = RoundFunction('12345678', 0x12345678, 1, 1)
print(b'hellohan')
print(int.from_bytes(b'hellohan', byteorder='big'))
print()

a = roundfunction.expand_bits(b'hellohan')
print("expanded     : ", a)
print("bit length   : ", int.from_bytes(a, byteorder='big').bit_length())
for x in a:
    print(x, end=' ')
print()

b = roundfunction.compress_bits(a)
print("compressed   : ", b)
print("bit length   : ", int.from_bytes(b, byteorder='big').bit_length())
for x in b:
    print(x, end=' ')
print()

# def xor_bytes(b1, b2):
#     # XOR two bytes objects and return a bytes object
#     i1 = int.from_bytes(b1, 'big')
#     i2 = int.from_bytes(b2, 'big')
#     result = i1 ^ i2
#     num_bytes = max(len(b1), len(b2))
#     return result.to_bytes(num_bytes, 'big')

# def str_to_hex(text):
#     return binascii.hexlify(text.encode('utf-8'))

# def hex_to_str(text):
#     return binascii.unhexlify(text).decode('utf-8')

# def hex_to_bin(text):
#     return bin(int(text, 16))[2:].zfill(len(text)*4)

# def bin_to_hex(text):
#     return hex(int(text, 2))[2:].zfill(2)

# def xor (A, B):
#     return bytes([a ^ b for a, b in zip(A, B)])

# def byte_to_binary(byte):
#     return ''.join([bin(b)[2:].zfill(8) for b in byte])