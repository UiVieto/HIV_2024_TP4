from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair

def test_find_closest_elements():# pragma: no cover
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)# pragma: no cover
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)# pragma: no cover

    # Tests zero shot générés par Salesforce/codet5-large-ntp-py
    assert find_closest_elements([1, 2, 3, 4, 5]) == (1, 2) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6]) == (1, 3) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7]) == (1, 4) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8]) == (1, 8) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (1, 9) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (1, 10) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (1, 11) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (1, 12) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (1, 13) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == (1, 14) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == (1, 15) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == (1, 16) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == (1, 17) # pragma: no cover
    find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == (1, 18) # pragma: no cover

    # Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)  # pragma: no cover

    # Q2.4. Inputs 1 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert find_closest_elements([1.0, 2.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)  # pragma: no cover
    # assert find_closest_elements([1.0, 1.0]) == (1.0, 1.0)  # pragma: no cover

    # Q2.4. Inputs 2 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)  # pragma: no cover
    # assert find_closest_elements([1.0, 1.0]) == (1.0, 1.0)  # pragma: no cover

    # Q2.4. Inputs 3 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    assert find_closest_elements([1.0, 2.0, 40.0, 5.0, 2.2]) == (2.0, 2.2)  # pragma: no cover
    assert find_closest_elements([1.0, 1231.23, 2.0]) == (1.0, 2.0)  # pragma: no cover

    # Test générés avec Qwen2.5-Coder-0.5B-Instruct
    # assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0) # pragma: no cover
