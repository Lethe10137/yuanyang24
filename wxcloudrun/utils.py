import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import time
from Crypto.Random import get_random_bytes

KEY_PHASE  = b"oikjhfe3ewdsxcvjp8765r4edfbaimochuan"
SALT_PHASE = b"234578okhfdwe57iknbvcde5678xudong"

def get_token(question_id, openid):
    return build_token(int(question_id), int(time.time() * 1000 * 1000),openid, KEY_PHASE, SALT_PHASE)

def build_token(question_id, timestamp, openid, key_phrase, salt_phrase):
    lower_time = timestamp & 0xFFFFFFFFFFFFFFFF  # Extract lower 64 bits of timestamp

    iv = get_random_bytes(16)

    key = hashlib.sha256(key_phrase).digest()

    salt = hashlib.sha256(salt_phrase).digest()
    salt_init = salt[:8]

    plaintext_u8 = bytearray(48)

    plaintext_u8[:8] = salt_init

    if len(openid) != 42:
        return ""

    try:
        openid_data = bytes.fromhex(openid)
        if len(openid_data) == 21:
            plaintext_u8[8:29] = openid_data
        else:
            return ""
    except ValueError:
        return ""

    plaintext_u8[29:37] = question_id.to_bytes(8, 'little')
    plaintext_u8[37:45] = lower_time.to_bytes(8, 'little')

    salt = hashlib.sha256(plaintext_u8).digest()
    salt_result = salt[:8]

    plaintext_u8[:8] = salt_result

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    cipher_text = cipher.encrypt(bytes(plaintext_u8))

    result = binascii.hexlify(iv).decode('utf-8') + binascii.hexlify(cipher_text).decode('utf-8')

    return result
    

def decode_token(token, key_phrase, salt_phase):
    key = hashlib.sha256(key_phrase).digest()

    if len(token) != 128:
        return None

    iv = binascii.unhexlify(token[:32])
    cipher_text = binascii.unhexlify(token[32:])

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    plaintext = cipher.decrypt(cipher_text)

    # print(binascii.hexlify(plaintext))
    
    salt_head = plaintext[:8]
    # print(binascii.hexlify(salt_head))
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
    
    
if __name__ == "__main__":
    # token = build_token(117029381625775928, int(time.time() * 1000 * 1000), "f234567890123456789012345678901234567890ed", KEY_PHASE, SALT_PHASE)
    token = get_token(117029381625775928, "123456789012345678901234567890123456789012")
    print(token)
    print(decode_token(token, KEY_PHASE, SALT_PHASE))