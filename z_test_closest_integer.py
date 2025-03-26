def test_closest_integer(closest_integer):
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("14.5.5") == 15
    assert closest_integer("-14.5.5") == -15
    assert closest_integer("14.5.5.5") == 15
    assert closest_integer("-14.5.5.5") == -15
    assert closest_integer("14.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5.5.5") == 15
    assert closest_integer("-14.5.5.5.5.5.5.5.5") == -15
    assert closest_integer("14.5.5.5.5.5.5.5.5") == 15
    # assert closest_integer("-14.5.
