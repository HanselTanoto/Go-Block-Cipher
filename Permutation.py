import hashlib

def generatePBox(seed : str, size : int) -> list:
    """Generate P-Box using SHA-256 hash function."""
    p_box = list(range(size))
    for i in range(size):
        hash = hashlib.sha256(seed.encode() + bytes([i])).hexdigest()
        j = int(hash, 16) % (size-i)
        p_box[i], p_box[i+j] = p_box[i+j], p_box[i]
    
    return p_box

def permute(bit: str, p_box: list):
    permuted_block = ""
    for i in range(len(p_box)):
        permuted_block += bit[p_box[i]-1]
    
    return permuted_block


def netralize(bit: str, p_box: list):
    backagain_block = ["0" for i in range (128)]
    for i in range(len(p_box)):
        backagain_block[p_box[i]-1] = bit[i]
    
    return''.join(backagain_block)
    
p_box = generatePBox("H-2 Menuju UTS Semangat", 128) #128 sesuai dengan jumlah bit
# print(p_box)
test_block = "11010111010010101011101001110100010101010100101010111010011101001101011101001010101110100111010011010111010010101011101001110100"
permuted_block = permute(test_block, p_box)
netralized_block = netralize(permuted_block, p_box)
print("Test Block : \n" + permuted_block)
print("Hasil Permutasi : \n" + permuted_block)
print("Hasil Balikan : \n" + netralized_block )
print("Hasil sama ? ", test_block == netralized_block)

