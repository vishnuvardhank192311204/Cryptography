def bit_padding_demo():
    print("--- ECB/CBC/CFB Padding Demonstration ---")
    
    # Let block size be 8 bytes (64 bits)
    block_size = 8
    
    # Scenario 1: Message is not a multiple
    msg1 = b"HELLO"
    print(f"\nMessage 1: {msg1}")
    
    # Rule: 1 bit (0x80) followed by 0 bits
    pad_len = block_size - (len(msg1) % block_size)
    padding = b'\x80' + b'\x00' * (pad_len - 1)
    padded_msg1 = msg1 + padding
    
    print(f"Padded Message 1 (Hex): {padded_msg1.hex()}")
    
    # Scenario 2: Message is exactly a multiple
    msg2 = b"EXACTBLK"
    print(f"\nMessage 2: {msg2}")
    
    pad_len2 = block_size - (len(msg2) % block_size)
    if pad_len2 == 0: pad_len2 = block_size
    padding2 = b'\x80' + b'\x00' * (pad_len2 - 1)
    padded_msg2 = msg2 + padding2
    
    print(f"Padded Message 2 (Hex): {padded_msg2.hex()}")
    
    print("\nWhy add padding when the length is already a complete multiple?")
    print("If we did not add a padding block to Message 2, the receiver would look at the")
    print("last bytes to strip the padding. If the actual message data happened to end")
    print("with 0x80 0x00 0x00... it would be incorrectly stripped, destroying real data.")
    print("By always appending padding, the receiver unequivocally knows the last bytes")
    print("are padding, resolving ambiguity.")

if __name__ == "__main__":
    bit_padding_demo()
