#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value"""

    if a_dictionary is None:
        return None
    a = sorted(a_dictionary.keys())
    return a[len(a) - 1]
