import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    BYTE_LENGTH = 4
    compare_bit = 2 ** len(target_string) - 1
    while True:
        nonce = os.urandom(BYTE_LENGTH)
        hash_nonce = hashlib.sha256(nonce)
        if (int(hash_nonce.hexdigest(), 16) & compare_bit) == int(target_string,2):
            return (nonce)




