# nfa_ex02.py
import dfa as dfa

def __main__():
    # DFA A1 from first lab:
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
    
    # DFA A2 from first lab:
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

    A1 = dfa.DFA(Q1, Sigma1, delta1, q01, F1)
    A2 = dfa.DFA(Q2, Sigma2, delta2, q02, F2)

    # Convert the DFAs into NFAs using the new method.
    N1 = A1.to_NFA()
    N2 = A2.to_NFA()

    words = ['a', 'b', 'ab', 'aa', 'ba', 'aab', 'abb', 'baba']
    new_NFA = [N1, N2]
    for i, X in enumerate(new_NFA, start=1):
        print(f"Testing converted NFA from A{i}:\n")
        print(f"{X.__repr__()}")
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")
    
__main__()