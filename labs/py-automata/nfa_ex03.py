# nfa_ex03.py
import dfa as dfa
import nfa as nfa

def __main__():
    # Test 1: DFAs from first lab converted to NFAs and back to DFAs
    # DFA A1:
    Q1 = {'1', '2', '3', '4'}
    Sigma1 = {'a', 'b'}
    delta1 = {
        ('1', 'a'): '2',
        ('1', 'b'): '4',
        ('2', 'a'): '2',
        ('2', 'b'): '3',
        ('3', 'a'): '2',
        ('3', 'b'): '2',
        ('4', 'a'): '4',
        ('4', 'b'): '4'
    }
    q01 = '1'
    F1 = {'3'}

    # DFA A2:
    Q2 = {'1', '2', '3'}
    Sigma2 = {'a', 'b'}
    delta2 = {
        ('1', 'a'): '2',
        ('1', 'b'): '1',
        ('2', 'a'): '3',
        ('2', 'b'): '1',
        ('3', 'a'): '3',
        ('3', 'b'): '1',
    }
    q02 = '1'
    F2 = {'3'}

    # create DFAs
    dfa1 = dfa.DFA(Q1, Sigma1, delta1, q01, F1)
    dfa2 = dfa.DFA(Q2, Sigma2, delta2, q02, F2)

    # convert DFAs to an equivalent NFA
    nfa1 = dfa1.to_NFA()
    nfa2 = dfa2.to_NFA()

    # convert NFAs back into DFAs
    dfa1_from_nfa = nfa1.to_DFA()
    dfa2_from_nfa = nfa2.to_DFA()
    dfas = [dfa1_from_nfa, dfa2_from_nfa]

    words = ['a', 'b', 'ab', 'aa', 'ba', 'aab', 'abb', 'baba']

    for i, X in enumerate(dfas, start=1):
        print(f"Testing converted NFA from A{i}:\n")
        print(f"{X.__repr__()}")
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")


    # Test 2: NFA with nondeterminism
    # strings that contain at least one 'a'
    Q3 = {'q0', 'q1'}
    Sigma3 = {'a', 'b'}
    delta3 = {
        ('q0', 'a'): {'q0', 'q1'},
        ('q0', 'b'): {'q0'},
        ('q1', 'a'): {'q1'},
        ('q1', 'b'): {'q1'},
    }
    q03 = 'q0'
    F3 = {'q1'}

    nfa3 = nfa.NFA(Q3, Sigma3, delta3, q03, F3)
    dfa3_from_nfa = nfa3.to_DFA()

    print("\nTesting DFA converted from an NFA (accepting strings containing at least one 'a'):")
    for w in words:
        print(f"  {w}: {dfa3_from_nfa.run(w)}")

    # Test 3: An NFA with unreachable states
    Q4 = {'q0', 'q1', 'q2', 'q3'}
    Sigma4 = {'0', '1'}
    delta4 = {
        ('q0', '0'): {'q1'},
        ('q1', '1'): {'q2'},
        ('q3', '0'): {'q3'}, # q3 is unreachable
        ('q3', '1'): {'q3'},
    }
    q04 = 'q0'
    F4 = {'q2', 'q3'}

    nfa4 = nfa.NFA(Q4, Sigma4, delta4, q04, F4)
    dfa4_from_nfa = nfa4.to_DFA()

    print("\nTesting DFA converted from an NFA:")
    print(f"{dfa4_from_nfa.__repr__()}")
    for w in ['00', '01', '011', '100']:
        print(f"{w}: {dfa4_from_nfa.run(w)}")

__main__()