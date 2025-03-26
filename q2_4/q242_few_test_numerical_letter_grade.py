def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([0.75, 0.1, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([0.75, 0.1, 0.0]) == ['D', 'D-', 'E']
