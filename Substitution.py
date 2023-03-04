import hashlib

def generateSBox(seed : str, size : int) -> list:
    """
        Generate S-Box menggunakan fungsi hash SHA-256.
        Generate dilakukan juga dengan memastikan bahwa
        element S-Box bernilai unik
    """
    s_box = []
    temp_box = []
    for i in range(size):
        hash = hashlib.sha256(seed.encode() + bytes([i])).hexdigest()
        candidate_elmt = int(hash[:2], 16)
        if (candidate_elmt not in temp_box):
            s_box.append(candidate_elmt)
            temp_box.append(candidate_elmt)

    for i in range(size):
        if(i not in temp_box):
            s_box.append(i)
            temp_box.append(i)
    
    return s_box

def inverseSBox(s_box : list):
    '''
        S-Box inverse dibuat dengan membuat list 
        yang berisi indeks pada S-Box asli
    '''
    s_box_inverse = []
    for i in range(len(s_box)):
        s_box_inverse.append(s_box.index(i))
    
    return s_box_inverse
    

s_box = generateSBox("H-2 Menuju UTS Semangat", 256) #256 karakter ASCII
s_box_inverse = inverseSBox(s_box)
test_text = b"Berserah diri kepada Tuhan"

'''
    Substitusi dilakukan dengan iterasi nilai byte pada teks.
    Dan digunakan sebagai indeks untuk mendapatkan nilai pada
    S-Box
'''

substituted_block = [s_box[b] for b in test_text]
print(s_box)
# print(s_box.index(215))
# print(s_box_inverse)