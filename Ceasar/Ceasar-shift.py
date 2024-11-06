encoded = input("Enter the Caesar-encoded text: ")

# Read words from file and store them in a set for efficient lookup
with open('words.txt', 'r') as file:
    words = set(word.strip().lower() for word in file)

d = {}

for key in range(26):
    decoded = ""
    for s in encoded:
        if s.isalpha():  # Check if character is an alphabet
            pos = ord(s) - key
            if s.islower():
                decoded += chr((pos - ord('a')) % 26 + ord('a'))
            elif s.isupper():
                decoded += chr((pos - ord('A')) % 26 + ord('A'))
        else:
            decoded += s
    # Split decoded string into words and compare with dictionary
    score = sum(1 for word in decoded.split() if word.lower() in words)
    d[decoded] = score

result = max(d, key=lambda k: d[k])
print(result)







