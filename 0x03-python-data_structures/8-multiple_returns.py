#!/usr/bin/python3
def multiple_returns(sentence):
    test_tuple = ()
    if len(sentence) == 0:
        test_tuple = 0
        return None
    else:
        test_tuple = len(sentence), sentence[0]
    return test_tuple
