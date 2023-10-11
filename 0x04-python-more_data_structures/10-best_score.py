#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value"""

    if a_dictionary is None:
        return None
    maximum = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == maximum:
            return k
