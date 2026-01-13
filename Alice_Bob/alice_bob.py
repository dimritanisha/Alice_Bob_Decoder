# The letter to code mapping that was provided
letter_code = {
    'A': '._',    'B': '_...',  'C': '_._.',  'D': '_..',
    'E': '.',     'F': '.._.',  'G': '__.',   'H': '....',
    'I': '..',    'J': '.___',  'K': '_._',   'L': '._..',
    'M': '__',    'N': '_.',    'O': '___',   'P': '.__.',
    'Q': '__._',  'R': '._.',   'S': '...',   'T': '_',
    'U': '.._',   'V': '..._',  'W': '.__',   'X': '_.._',
    'Y': '_.__',  'Z': '__..'
}

# Reversing the mapping of letter to code like : code -> letter
# v is for letter and k is for corresponding code
code_letter = {v: k for k, v in letter_code.items()}
# strip will remove any extra whitespace and newline character from input
encrypted = input().strip()
#all the decoded values will stored in the result list
result = []
# then will do backtracking function to find possible combinations
# pos is used for current position in encryptef string
# path is used to store current decoding string
 
def backtrack(pos, path):
    if pos == len(encrypted):
        result.append(path)
        return
    
    # Try all possible code lengths (1 to 4)
    # because maximum length of any code is 4 here
    
    for length in range(1, 5):
        if pos + length <= len(encrypted):
            part = encrypted[pos:pos + length]
            if part in code_letter:
                backtrack(pos + length, path + code_letter[part])

backtrack(0, "")

# Print sorted results
for word in sorted(result):
    print(word)
