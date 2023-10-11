#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value"""

    if a_dictionary is None:
        return None
    a = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
    return a[0][0]
