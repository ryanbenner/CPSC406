# a class for DFAs
# modify as needed
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q              # set of states
        self.Sigma = Sigma      # set of symbols
        self.delta = delta      # transition function
        self.q0 = q0            # initial state
        self.F = F              # final (accepting) states
   
    # print the data of the DFA
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    def run(self, w) :
        current_state = self.q0
        for symbol in w:
            if symbol not in self.Sigma:
                raise ValueError(f"Symbol {symbol} not in the DFA alphabet {self.Sigma}.")
            # look up transition state, if none is defined the word is rejected
            if (current_state, symbol) not in self.delta:
                return False
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.F

    # returns a new DFA that accepts the words that the current DFA refuses and vice versa
    def refuse(self):
        new_F = self.Q - set(self.F)
        return DFA(self.Q, self.Sigma, self.delta, self.q0, new_F)