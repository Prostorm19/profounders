# Design a Program for creating machine that accepts three consecutive one
class DFA:
    def __init__(self, states, alphabets, transitions, initialstate, finalstate):
        self.states=states
        self.alphabets=alphabets
        self.transitions=transitions
        self.initialstate = initialstate
        self.finalstate = finalstate

    def is_accepted(self, word):
        current_state = self.initialstate
        for symbol in word:
            next_state=self.transitions[current_state][symbol]
            if next_state is None:
                return False
            current_state=next_state
        return current_state in self.finalstate
    

states=["S0","S1","S2"]
alphabets={"0","1"}
transitions= {  "S0": {"0":"S0", "1":"S1"},
                "S1": {"0":"S0", "1":"S2"},
                "S2": {"0":"S0", "1":"S2"} 
              }


initial_state = "S0"
accepting_states = ["S2"]

dfa = DFA(states, alphabets, transitions, initial_state, accepting_states)
string="1010111"
print("String: ",string, "is", dfa.is_accepted(string)) 