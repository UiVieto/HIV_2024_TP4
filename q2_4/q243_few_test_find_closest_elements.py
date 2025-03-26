def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0, 2.0, 40.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 1231.23, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 40.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 1231.23, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 40.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 1231.23, 2.0]) == (1.0, 2.0)
