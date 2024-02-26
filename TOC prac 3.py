#Write a program for generating derivation sequence / language for the given sequence of productions
def generate_language(productions, current_string, index, target_length):
    if index == target_length:
        print(current_string)
        return
    
    for production in productions:
        if current_string.endswith(production[0]):
            generate_language(productions, current_string + production[1], index + 1, target_length)

# Example productions: [('S', 'AB'), ('A', 'aA'), ('A', ''), ('B', 'bB'), ('B', '')]
productions = [('S', 'AB'), ('A', 'aA'), ('A', ''), ('B', 'bB'), ('B', '')]

# Target length of derivation sequence
target_length = 5

# Starting symbol
start_symbol = 'S'

# Generate the language
print("Derivation sequence / Language:")
generate_language(productions, start_symbol, 1, target_length)
