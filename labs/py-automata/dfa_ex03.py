import dfa

def __main__() :
    
    Q = {1, 2, 3, 4}
    Sigma = {'a', 'b'}
    delta = {
        (1, 'a'): 2,
        (1, 'b'): 4,
        (2, 'a'): 3,
        (2, 'b'): 4,
        (3, 'a'): 3,
        (3, 'b'): 3,
        (4, 'a'): 2,
        (4, 'b'): 3
    }
    q = 1
    F = {2, 4}
    A = dfa.DFA(Q, Sigma, delta, q, F)
    
    # create A0 that accepts the words that A rejects, and vice versa.
    A0 = A.refuse()
    
    # tracks num of test case fails
    failureCount = 0

    # test cases for A and A0:
    test_words = ["", "a", "aa", "ab", "b", "ba", "bb", "aba", "bab"]
    print("Testing DFA A and its complement A0:")
    for word in test_words:
        resultA = A.run(word)
        resultA0 = A0.run(word)
        print(f"Word: '{word}': A -> {resultA}, A0 -> {resultA0}")
        # verify that A0's result is the opposite of A's result.
        if resultA == resultA0:
            print(f"Test failed for '{word}'.")
            failureCount += 1
        
    if failureCount == 0:
        print("All tests passed.")
    else:
        print(f"{failureCount} tests failed.")

if __name__ == "__main__":
    __main__()