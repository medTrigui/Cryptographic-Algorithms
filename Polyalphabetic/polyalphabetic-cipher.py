# Mohamed Trigui
# 10/17/2024

'''This function takes a set of state abbreviations (possible plaintexts) and a ciphertext as input.'''
'''The goal is to determine which state abbreviation is the correct plaintext, assuming a polyalphabetic cipher with a key of length 1.'''
'''Since the key length is 1, the same character is used to shift both characters in the plaintext. Therefore, the shift applied to the first character of the plaintext must be the same as the shift applied to the second character for it to be a valid match.'''

def poly_alphabetic(lst, cipher):
    dictionary = {}  # Store the state and corresponding shift values

    for state in lst:
        shift = []  # Store the shift values for each character in the state
        dictionary[state] = ""  

        # Loop over each character in the state abbreviation
        for c in state:
            # Calculate the shift required to turn the state character into the corresponding cipher character
            shift.append(((ord(cipher[state.index(c)]) - ord('A')) - (ord(c) - ord('A'))) % 26)
            dictionary[state] = shift  # Store the shift list in the dictionary for the state

    print(dictionary)  # Print the dictionary to see the shift values for each state

    # Check if both characters in the state's shift list have the same shift value
    for state in dictionary:
        if dictionary[state][0] == dictionary[state][1]: 
            print("The Plaintext is: " + state)  # Likely plaintext
           
    
poly_alphabetic({'IL', 'MO', 'NY', 'NJ', 'CA', 'AK', 'MI', 'WV', 'AZ', 'TX'}, 'DF')