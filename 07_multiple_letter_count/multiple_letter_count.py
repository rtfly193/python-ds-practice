def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltr_count = {}

    for ltr in phrase:
        ltr_count[ltr] = ltr_count.get(ltr, 0) + 1

    return ltr_count