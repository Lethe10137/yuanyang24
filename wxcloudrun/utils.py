import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

def decode_token(token, key_phrase, salt_phase):
    key = hashlib.sha256(key_phrase).digest()

    if len(token) != 128:
        return None

    iv = binascii.unhexlify(token[:32])
    cipher_text = binascii.unhexlify(token[32:])

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    plaintext = cipher.decrypt(cipher_text)

    print(binascii.hexlify(plaintext))
    
    salt_head = plaintext[:8]
    print(binascii.hexlify(salt_head))
    salt = hashlib.sha256(salt_phase).digest()
    salt_init = salt[:8]
        
    salt_check = hashlib.sha256(salt_init + plaintext[8:]).digest()[:8]

    flag = all(salt_head[i] == salt_check[i] for i in range(8))

    if flag:
        timestamp = int.from_bytes(plaintext[37:45], byteorder='little')
        question_id = int.from_bytes(plaintext[29:37], byteorder='little')
        id_bytes = plaintext[8:29]
        id = binascii.hexlify(id_bytes).decode('utf-8')
        return (id, timestamp, question_id)
    else:
        return None


KEY_PHASE  = b"oikjhfe3ewdsxcvjp8765r4edf";
SALT_PHASE = b"234578okhfdwe57iknbvcde5678";

token = "f5a6ec126d3f24264027a859a7c2e6123b1cae0baf66b0a3e422ac72954a291a30840a81dec20d54b7a69238662c680e0305c9e2621247aa5c4cff784e060dc7"
token = "71ad1c0f5c0682a74001c5f3d6aa8723522a4d53438fc810869c4e9a53dd530301cd10128cc54cb7909afa070a1d8c4b37382d7f2a948d8fc9e4226a6073452a"

# print(decode_token(token, KEY_PHASE, SALT_PHASE))

def trunc_open_id(open_id):
    if len(open_id) == 28:
        return open_id
    if len(open_id) > 28:
        return open_id[-28:]
    if len(open_id) < 28:
        return "0" * (28 - len(open_id)) + open_id