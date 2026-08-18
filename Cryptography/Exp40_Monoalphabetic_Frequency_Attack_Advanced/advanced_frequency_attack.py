import string
import random

# Simplified simulated annealing attack
# For demonstration, we just define the structure of a hill climbing attack

def evaluate_fitness(text):
    # In a real attack, evaluate n-grams (quadgrams usually work best)
    # We will use a dummy fitness function for educational purposes
    score = 0
    common_words = ["THE", "AND", "THAT", "HAVE", "FOR", "NOT", "WITH", "YOU"]
    for word in common_words:
        score += text.count(word) * len(word)
    return score

def decrypt(ct, key):
    res = ""
    for c in ct:
        if c in string.ascii_uppercase:
            res += key[ord(c)-65]
        else:
            res += c
    return res

def mutate(key):
    key_list = list(key)
    i, j = random.sample(range(26), 2)
    key_list[i], key_list[j] = key_list[j], key_list[i]
    return "".join(key_list)

def advanced_mono_attack():
    print("--- Advanced Monoalphabetic Attack (Hill Climbing) ---")
    ct = input("Enter ciphertext: ").upper()
    
    if len(ct) < 10:
        print("Ciphertext too short for meaningful n-gram attack.")
        return
        
    print("Initial Random Key...")
    parent_key = "".join(random.sample(string.ascii_uppercase, 26))
    parent_score = evaluate_fitness(decrypt(ct, parent_key))
    
    print(f"Starting Hill Climbing for 1000 iterations (Educational Simulation)...")
    
    # Run hill climbing
    for i in range(1000):
        child_key = mutate(parent_key)
        child_text = decrypt(ct, child_key)
        child_score = evaluate_fitness(child_text)
        
        if child_score > parent_score:
            parent_score = child_score
            parent_key = child_key
            
    best_text = decrypt(ct, parent_key)
    print(f"\nBest Key Found: {parent_key}")
    print(f"Score: {parent_score}")
    print(f"Decrypted Text: {best_text}")
    print("\nNote: A full implementation would use quadgram statistics and 10,000+ iterations.")

if __name__ == "__main__":
    advanced_mono_attack()
