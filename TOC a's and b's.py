class PermutationDFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'q3', 'b': 'q1'},
            'q2': {'a': 'q2', 'b': 'q3'},
            'q3': {'a': 'q4', 'b': 'q3'},
            'q4': {'a': 'q4', 'b': 'q4'}
        }
        self.initial_state = 'q0'
        self.accepting_state = 'q4'

    def is_accepted(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state == self.accepting_state


# Test the DFA
dfa = PermutationDFA()
print(dfa.is_accepted('aaabbb'))  # True
print(dfa.is_accepted('ababab'))  # True
print(dfa.is_accepted('aabb'))    # False
print(dfa.is_accepted('aaab'))    # False
print(dfa.is_accepted('aaabb'))   # False
print(dfa.is_accepted('aaabbbb')) # False