from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def block_modes_demo():
    print("--- ECB / CBC / CFB Mode Demonstration ---")
    
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    
    plaintext = b"This is a test message demonstrating block modes."
    print(f"\nPlaintext: {plaintext}")
    
    print("\n--- ECB Mode ---")
    # ECB does not use an IV. It requires padding.
    padded_pt = pad(plaintext, AES.block_size)
    print(f"Padded Plaintext: {binascii.hexlify(padded_pt).decode()}")
    
    ecb_cipher = AES.new(key, AES.MODE_ECB)
    ecb_ct = ecb_cipher.encrypt(padded_pt)
    print(f"ECB Ciphertext: {binascii.hexlify(ecb_ct).decode()}")
    
    # Decrypt
    ecb_dec = unpad(AES.new(key, AES.MODE_ECB).decrypt(ecb_ct), AES.block_size)
    print(f"ECB Decrypted: {ecb_dec}")
    
    print("\n--- CBC Mode ---")
    # CBC uses an IV and requires padding.
    cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
    cbc_ct = cbc_cipher.encrypt(padded_pt)
    print(f"CBC Ciphertext: {binascii.hexlify(cbc_ct).decode()}")
    
    cbc_dec = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cbc_ct), AES.block_size)
    print(f"CBC Decrypted: {cbc_dec}")
    
    print("\n--- CFB Mode ---")
    # CFB turns a block cipher into a stream cipher. It does NOT require padding!
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    cfb_ct = cfb_cipher.encrypt(plaintext)
    print(f"CFB Ciphertext: {binascii.hexlify(cfb_ct).decode()}")
    
    cfb_dec = AES.new(key, AES.MODE_CFB, iv).decrypt(cfb_ct)
    print(f"CFB Decrypted: {cfb_dec}")
    
    print("\nWhy is padding added even when message length is a multiple of block size?")
    print("If a message naturally ends on a block boundary, and we don't pad, the receiver")
    print("doesn't know if the last bytes of the message are padding or actual data.")
    print("By universally appending a padding block in all situations, we eliminate ambiguity.")

if __name__ == "__main__":
    block_modes_demo()
