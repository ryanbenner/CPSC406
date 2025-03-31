# nfa.py
class NFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q          # set of states
        self.Sigma = Sigma  # set of symbols
        self.delta = delta  # non-deterministic transition function
        self.q0 = q0        # initial state
        self.F = F          # set of final states

    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        current_states = {self.q0}
        
        for symbol in w:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.delta:
                    next_vals = self.delta[(state, symbol)]
                    if isinstance(next_vals, str):
                        next_vals = {next_vals}
                    else:
                        next_vals = set(next_vals)
                    next_states.update(next_vals)
                else:
                    # If no transition is defined, nothing happens—keep the state
                    next_states.add(state)
            current_states = next_states
            
            if not current_states:
                break

        return bool(current_states & self.F)
    
    def to_DFA(self):
        from dfa import DFA

        start = tuple(sorted(({self.q0}))) # represents state as unchangeable collection of items
        unprocessed = [start] # queue of DFA states to process
        dfa_states = {start} # set of all DFA states
        dfa_delta = {}

        # process each DFA state
        while unprocessed:
            current = unprocessed.pop(0)
            for symbol in self.Sigma:
                next_state_set = set()
                # for each NFA state in current DFA state, add all reachable states on symbol
                for state in current:
                    if (state, symbol) in self.delta:
                        next_state_set |= self.delta[(state, symbol)]
                # convert to frozenset to use as a DFA state
                next_state = tuple(sorted((next_state_set)))
                dfa_delta[(current, symbol)] = next_state
                if next_state not in dfa_states:
                    dfa_states.add(next_state)
                    unprocessed.append(next_state)

        # find final (accepting) DFA states:
        # a DFA state is final if it has one or more of NFA's final states
        dfa_F = {state for state in dfa_states if set(state) & self.F}

        return DFA(dfa_states, self.Sigma, dfa_delta, start, dfa_F)
