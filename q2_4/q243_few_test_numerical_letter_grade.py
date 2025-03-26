def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3, 3.5, 0.75, 0.1, 0.0]) == ['A+', 'B', 'A-', 'D', 'D-', 'E']
    assert numerical_letter_grade([4.0, 3, 3.5, 0.75, 0.1, 0.0]) == ['A+', 'B', 'A-', 'D', 'D-', 'E']
