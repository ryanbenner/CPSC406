import labs.Week2.dfa as dfa

def __main__() :
    Q1 = {'1', '2', '3'}
    sigma1 = {'a', 'b'}
    delta1 = {
        ('1', 'a') : '2',
        ('1', 'b') : '1',
        ('2', 'a') : '2',
        ('2', 'b') : '3',
        ('3', 'a') : '2',
        ('3', 'b') : '1',
    }
    q01 = '1'
    F = {'3'}
    
    # todo: instantiate accordingly
    A1 = dfa.DFA(...)
    
    # todo: instantiate accordingly
    A2 = dfa.DFA(...)
    
    # todo: instantiate accordingly
    A3 = dfa.DFA(...)

    # todo: instantiate accordingly
    A4 = dfa.DFA(...)

    # todo: instantiate accordingly
    A5 = dfa.DFA(...)

    # todo: instantiate accordingly
    A6 = dfa.DFA(...)

    # todo: instantiate accordingly
    A7 = dfa.DFA(...)
    
    # todo: add appropriate test cases for each of A1 to A7

__main__()